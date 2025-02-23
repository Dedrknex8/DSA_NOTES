## Post service

## rabbit mq

```node
const amqp = require('amqplib');

const logger = require('./logger');


let connection = null;

let channel = null;

  

const EXCHANGE_NAME = 'Chat_Message' //unique exchange name hook

  

async function connectRabbitMQ(){

    try {

        connection = await amqp.connect(process.env.RABBITMQ_URL);

        channel = await connection.createChannel();

  

        await channel.assertExchange(EXCHANGE_NAME, 'topic',{durable:false})

        logger.info('Connected to RabbitMq');

        return channel;

    } catch (error) {

        logger.error('Error connecting to rabbitMQ Post service',error);

    }

}

  

//publish event handler

async function publishEvent(routingKey,message){

    if(!channel){

        await connectRabbitMQ();

    }

  

    channel.publish(EXCHANGE_NAME,routingKey,Buffer.from(JSON.stringify(message)))

    logger.info(`Event published : ${routingKey}`)  

}

  

module.exports = { connectRabbitMQ,publishEvent}

  

// 753
```

## media service (rabbit mq file)


```node 
const amqp = require('amqplib');

const logger = require('./logger');

  

let connection = null;

let channel = null;

  

const EXCHANGE_NAME = 'Chat_Message' //unique exchange name hook

  

async function connectRabbitMQ(){

    try {

        connection = await amqp.connect(process.env.RABBITMQ_URL);

        channel = await connection.createChannel();

  

        await channel.assertExchange(EXCHANGE_NAME, 'topic',{durable:false})

        logger.info('Connected to RabbitMq');

        return channel;

    } catch (error) {

        logger.error('Error connecting to rabbitMQ Media service',error);

    }

}

  

//publish event handler

async function publishEvent(routingKey,message){

    if(!channel){

        await connectRabbitMQ()

    }

  

    channel.publish(EXCHANGE_NAME,routingKey,Buffer.from(JSON.stringify(message)))

    logger.info(`Event published : ${routingKey}`)  

}

  
  

async function consumeEvent(routingKey,callback){

    if(!channel){

        await connectRabbitMQ();

    }

  

    const q = await channel.assertQueue("",{exclusive  : true})

   await channel.bindQueue(q.queue,EXCHANGE_NAME,routingKey);

    channel.consume(q.queue,(msg)=>{

        const content = JSON.parse(msg.content.toString());

        callback(content);

        channel.ack(msg);

    })

  

    logger.info(`Subscribed to event : ${routingKey}` )

}

  

module.exports = { connectRabbitMQ,publishEvent,consumeEvent}

```
## Event handler

```node 
const Media = require("../modells/Media");

const { deleteMediaCloudinary } = require("../utils/cloudinary");

const logger = require('../utils/logger');

const handlerPostDeleted = async(event)=>{

console.log(event,"eventevent");

  

const {postId,mediaIds} = event;

try {

    const mediaTodelete = await Media.find({_id : {$in: mediaIds}}); //this will give post id

  

    for(const media of mediaTodelete){

        await deleteMediaCloudinary(media.publicId);

        await Media.findByIdAndDelete(media._id);

        logger.info(`Deleted media ${media._id} associated with this post:${postId  }`);

        logger.info('Meida deleted process completed')

    }

  

} catch (error) {

    logger.error('Error ocuuredd while deletion');

}

  

};

  

module.exports =  {handlerPostDeleted};
```

## Servere.js media service

```node 
async function startServer(){

    logger.info('Starting Media service')

    try {

        await connectRabbitMQ();

        //consume all evenents

        await consumeEvent('post.deleted',handlerPostDeleted);

        app.listen(PORT,()=>{

            logger.info('Listing to port sucessFully')

        });

    } catch (error) {

        logger.error('Error starting the server',error);

        process.exit(1);

    }

}

  

startServer();
```