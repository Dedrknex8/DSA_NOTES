>**middleware** refers to functions that are executed during the lifecycle of an HTTP request to the server. Middleware functions can modify the request and response objects or end the request-response cycle.

### **How Middleware Works**

Middleware is executed **in the order it is defined**. It is like a pipeline where each middleware function decides whether to:

1. Pass the request to the next middleware using `next()`.
2. Send a response to the client and end the pipeline.

>In short middleware is just like helper in doing your work before it's done.Each helper has some job to do like getting header make req to the server and so on.

> To learn more about it go through this [doc](https://expressjs.com/en/guide/using-middleware.html#using-middleware)by express

### A simple code for middleware

```node 
const express = require('express')

const app = express()

const myFirstMiddleware = (req,res,next) =>{

    console.log("this middleware will run every time")

     next(); //if not next then other app .get will not work

};

  

app.use(myFirstMiddleware);

//LET'S MAKE TO FUNCTION HOMEPAGE AND UPDATE

app.get('/',(req,res,next)=>{

    res.send("Home page")

});

app.get('/about',(req,res,next)=>{

    res.send("About page")

});

  

const port = 2929;

  

app.listen(port,()=>{

    console.log(`the server is runnng on port ${port}`)

});
```