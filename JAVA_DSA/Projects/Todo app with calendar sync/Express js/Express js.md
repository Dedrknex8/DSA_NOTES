> What is express js
> -> express is a framework for node js just like react js is a framework for javascript.


## Hello world in express js

1. First install express in node js `node install express`


```node
const express = require('express')

const app = express() //CREATES A EXPRESS APP

  

app.get('/',(req,res) =>{

    res.send("Hello world")

  

     //THIS IS THE MESSAGE

})
const port = 2929;

app.listen(port,()=>{

    console.log(`listinin on port ${port}`)

})

```
## Basic routing in express js

```node
const express = require('express')

const app = express() //CREATES A EXPRESS APP

  

app.get('/',(req,res) =>{

    res.writeHead(200, {"Content-Type": "text/plain"});

  

     //THIS IS THE MESSAGE

  

    res.end("HI there welcome to my first http server!")

})

  

//TRY TO GET SOME PRODUCTS AS JSON

  

app.get('/products',(req,res) =>{

    const products = [

        {

            id : 1,

            name : "product 1"

        },

        {

            id : 2,

            name : "product 2"

        },

        {

            id : 3,

            name : "product 3"

        }

    ]

    res.json(products)

})

  

const port = 2929;

app.listen(port,()=>{

    console.log(`listinin on port ${port}`)

})
```

