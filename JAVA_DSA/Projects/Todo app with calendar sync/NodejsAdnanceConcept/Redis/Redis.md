> It's client for Node js. It is known as remote access database. It sores data in in memory on ram rather than disk. Acessing it very fast.
> 

## How to install radis

> search on your browser redis git install [windows] or any other os if you use.

> For windows go to `C:\Program Files\Redis` and copy that path and add to to environment path so that u can directly access it from your terminal

## How to use redis in node

> FIrst thing install redis as npm package

`npm i redis`

1. import redis package in node js
 `const redis = require('redis);`


#### How to create a Redis client

```node
const client = redis.createClient({

    host : 'localhost',

    port : 6379 //Default Port

});
```


#### Add a error event 

```node
const client = redis.createClient({

    host : 'localhost',

    port : 6379

});

  

//Error event

client.on('Error', (error)=> console.log(error)

);
```


#### A function to connect to Redis client

```node
const redis = require('redis');

const client = redis.createClient({

    host : 'localhost',

    port : 6379

});

//Error event

client.on('Error', (error)=> console.log(error)

);

async function redisConnection(){

    try {

        await client.connect();

        console.log("connect to redis successfully");

    } catch (error) {

        console.log(error);

    }finally{

        await client.quit(); // To close any unwanted connection

    }

}

redisConnection();
```


## Set key and value and some basic operations

```node
const redis = require('redis');

  

const client = redis.createClient({

    host : 'localhost',

    port : 6379

});

  

//Error event

client.on('Error', (error)=> console.log(error)

);

  

async function redisConnection(){

    try {

        await client.connect();

        console.log("connect to redis successfully");

        //Set key and value

        await client.set("name","Dedrknex");

  

        const extractValue = await client.get("name");

        console.log(extractValue);

        //To delete a key

  

        const delvalue  = await client.del("name");

        console.log("this will",delvalue); //this will return count of del value

  

        const NewUpdatedValue  = await client.get("name");

        console.log(NewUpdatedValue); //This will return null as no value is associated with it

  

    } catch (error) {

        console.log(error);

    }finally{

        await client.quit();

    }

}

  

redisConnection();
```

> To set keys and values use mset and mget 

```node
await client.mSet(["user:email", "xyz@.com","user:name", "dedrknex","user-passwd","gobi"]);

	const [email,name,passwd] = await client.mGet(["user:email","user:name","user:passwd"]);
cosole.log(email,name,passwd);

```


## Lists

```node
//List -> LPUSH, LRANGE,LPOP,RPOP

        await client.del("notes");

  

        await client.lPush("notes",["note 1","note 2","note 3"])

        const extractAll = await client.lRange("notes",0,-1);

        console.log(extractAll);
```

## Sets

```node
// sets -> SADD , SMEMBERS, SISMEMBER,SREM
        // await client.sRem("user:name");
        await client.sAdd("user:name",["varun","Rahul","randomeNickName"]);
   const extractSetName = await client.sMembers("user:name");
        console.log(extractSetName);

        //check if varun is a meber of set or not return true if present and false if not present

        const isVarunIsOneOfUserNickName = await client.sIsMember("user:name","varun");
        console.log(isVarunIsOneOfUserNickName);

        const removeName = await client.sRem("user:name","Rahul");

        console.log(removeName);

        const getUpdatedUserName = await client.sMembers("user:name");

     console.log(getUpdatedUserName);
``` 

## Pub/Sub

>**Pub/Sub (short for publish/subscribe)** is a messaging technology that facilitates communication between different components in a distributed system

>It's mainly used to communicate b\w two different components without have to form a direct connection

Example :  Two location A & B want to share products b\w A and B u can't send directly to B but can use a delivery agent to send your package to point B

```node
const redis = require('redis');

const client = redis.createClient({

    host:'localhost',

    port:6379

});

  client.on("error",(error)=>{

    console.log("error connecting to redis client");

});

async function testAdditonalFeatures(){

    try {

        await client.connect();

  

        const subsriber =  client.duplicate(); //create a new client with same config

        await subsriber.connect(); // connect to resis sevre for the subscriber

        await subsriber.subscribe("dummy-channel",(message, channel) =>{

            console.log(`recived messsage form ${channel} : ${message}`);

        })

        //publish message to dummy-channel

        await client.publish('dummy-channel','Some dummy data from publisher');
        //ensure that message are recived before unsubscribing

        await new Promise((resolve)=> setTimeout(resolve,1000));

        await subsriber.unsubscribe('dummy-channel');

        await subsriber.quit();

        console.log('connection exits');

    } catch (error) {

        console.log(error);

    }finally{

        await client.quit()

    }

}
testAdditonalFeatures();
```

