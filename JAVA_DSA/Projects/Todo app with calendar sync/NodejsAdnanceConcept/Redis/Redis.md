> It's client for Node js. It is known as remote access database. It sores data in in memory on ram rather than disk. Acessing it very fast.
> 

## How to install radis

> search on your browser redis git install [windows] or any other os if you use.

> For windows go to `C:\Program Files\Redis` and copy that path and add to to envirement path so that u can directly access it from your terminal

## How to use redis in node

> FIrst thing install redis as npm package

`npm i redis`

1. import redis packagae in node js
 `const redis = require('redis);`


#### How to create a redis client

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


#### A function to connect to redis client

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