> EJS stands for `Embedded javascript templating`.

# What  EJS does ?

> EJS is used to render html tags in a express or node.js file
> It's like rendering html in java script



### Installation and setup

1. Install node js if not installed 
2. Under the same dir as your express or node js code 
3. Open terminal and install `npm install ejs`
4. Refer the [docs](https://ejs.co/#docs) if you learn more about other than this notes
5. Refer the tags section which is import in ejs docs

### CREATING FRIST CODE OF EJS

#### Index.js
```node
const express = require('express')

const app = express()

const path = require('path')

  

//SET THE VIEW ENGINE AS EJS

  

app.set('view engine','ejs');

  

//SET THE DIR NAME

app.set('views',path.join(__dirname,'views'));

  

//SOME DUMMY DATDA

const products = [

    {

        'id' : 1,

        'product' : "zebra"

    },

    {

        'id' : 1,

        'product' : "horse"

    },

    {

        'id' : 1,

        'product' :"dog",

    }

];

  

//ROUTING

app.get('/',(req,res)=>{

    res.render('home',{title : 'Home',products : products})

}) //THE TITLE PASS HERE CAN BE USED IN HEADER.EJS TO DYNAMICALLY UPDATE THE HEADER

app.get('/about',(req,res)=>{

    res.render('about',{title : 'about'});

})

  

const port = 2929;

  

app.listen(port,()=>{

    console.log(`Server is runing on ${port}`)

})
```

#### Home.ejs

```node
<%- include('header.ejs') %>

<h1>Welcome to homepage</h1>

<label>List of products</label>

<ul>

    <% products.forEach(product => { %>

        <li><%= product.product %></li>

    <% }) %>

</ul>
```

#### about.ejs

```node
<%- include('header.ejs') %>

<h1>This is our about page</h1>
```

#### Header.ejs

```html 
<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title><%= title %></title> <!-- this is used to pass values dynamically-->

</head>

<body>

    <h1>THis is a common header for all  views</h1>

</body>

</html>
```

> Note 
> Here the title is used to pass dynamically in both home and about by modifying it into header file