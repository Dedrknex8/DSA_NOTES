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


## get single items form the products 

> Get product/id from here

```node
const express = require('express')
const app = express();
app.get("/products",(req,res)=>{

    const products = [

        {

            id : 1,

            name: 'new product'

        },

        {

            id : 2,

            name: 'two product'

        },

        {

            id : 3,

            name: '3 product'

        }

    ]

    res.json(products);

})
//LET'S GET SINGLE PRODUCT AS /product/?id=1

app.get('/products/:id',(req,res) =>{

    const productId = parseInt(req.params.id);

    const products = [

        {

            id : 1,

            name: 'new product'

        },

        {

            id : 2,

            name: 'two product'

        },

        {

            id : 3,

            name: '3 product'

        }]

        const getSingleProduct = products.find(product => product.id === productId);

  

        if(getSingleProduct){

            res.json(getSingleProduct)

        }else{

            res.status(404).send('product is not found');

        }

})

const port = 2929;
app.listen(port, ()=>{

    console.log("Server is runnig on port 2929");

})
```

## App module in express js

>The `app.use()` method in Express.js is used to **register middleware functions** or **mount middleware** at specific paths for your application. Middleware functions are functions that have access to the request (`req`), response (`res`), and the next middleware function (`next`) in the application's request-response cycle.

```noed
i will update the code later on
```