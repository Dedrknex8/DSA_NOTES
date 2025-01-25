# Date 23-01-25 || Rohit Tiwari

## Topic to be covered

- [x] Understanding the aggregation pipeline
- [x] Using common aggreagtaion operators
- [x] understanding document references
- [ ] Populating referenced documents


## Agregation concept

> Means simply to group or filter out result from DB

```node
const Product = require('../Modells/product');

  

const insertProduct = async(req,res)=>{

    try {

        const sampleProducts = [

        {

        Product : "Laptop",

        category : "Electornics",

        price : 499,

        instock : true,

        tags : ["laptop","gaming"]

        },

        {

        Product : "Mobile",

        category : "Electornics",

        price : 299,

        instock : true,

        tags : ["Mobile","Android"]

        },

        {

        Product : "Console",

        category : "Gaming",

        price : 399,

        instock : false,

        tags : ["ps5","gaming"]

        },

        ];

  

        const result = await Product.insertMany(sampleProducts);

        res.status(201).json({

            sucess :  true,

            data : `The Product ${result.length} added successfully`

        });

  

    } catch (error) {

        console.log(error);

        res.status(500),json({

            success : false,

            message : "Some went wrong in adding products"

        });

        }

}

  

const getAllProduct = async(req,res)=>{

    try{

    const result = await Product.aggregate([

        {

            $match : { //macthes the product with instock true

                instock : true,

                price : {

                    $gte : 100, //price greate than

                }

            },

        },

        {

            $group : {

                _id : "Electornics",

                avgPrice : {

                    $avg : "$price",

                },

                count : {

                    $sum : 1,

                }

                }

        },

    ]);

  

    res.status(200).json({

        success : true,

        message : "Product found",

        data : result

    });

    }catch(e){

        console.log(e);

    }

}

  

const productAnalysis = async(req,res) =>{

    try {

        const result = await Product.aggregate([

        {

            $match: {

                'category': 'Electornics' // Use the correct path to match nested fields

            },

        },

        {

        $group : { //group some constrains to filter result

            _id  :null,

                totalRevenue : {

                $sum : "$price",

  

                },

                avgPrice : {

                    $avg : "$price"

                },

                maxPrice : {

                    $max : "$price",

                },

                minPrice: {

                    $min : "$price"

                }

        }

        },

        {

        $project : { // projection is used for `=> include or exclude 0 => exclude

            _id : 0,

            totalRevenue : 1,

            maxPrice : 1,

            minPrice : 1,

            avgPrice : 1,

            priceRange : {

                $subtract : ["$maxPrice","$minPrice"],

            }

        }

        }

    ]);

        console.log(result);

        res.status(200).json({

            message : `Product found ${result.length}`,

            data : result,

        })

    } catch (error) {

        console.error(error);

        res.status(500).json({

            message : "something went wrong in product analysis"

        })

    }

}

  
  

module.exports  =  { insertProduct,getAllProduct,productAnalysis };
```

## Document referencing

> For a document to be referenced we have crated two models one book and other author
> The author will ref the book section i.e using book we can find the author of that book


### auhtor.js

```node
const mongoose = require('mongoose');

  

const AuthorSchema = new mongoose.Schema({

    name : String,

    bio : String,

});

  

module.exports = mongoose.model("Author",AuthorSchema);
```
### book.js

```node
const mongoose = require('mongoose');

const Author = require('./author');

const bookSchema = new mongoose.Schema({

    title : String,

    author : {

        type : mongoose.Schema.Types.ObjectId, // auhtor id

        ref : 'Author' //this will refer to the author

    }

})

  

module.exports = mongoose.model('Book',bookSchema);
```

## controllers 
> For creating author,book, and getiing author by books

```node
const Author = require('../Modells/author');

const Book = require('../Modells/book');

  
  

const createAuthor = async(req,res) =>{

    try {

        //get author deatils from req.body and appened it

  

        const author = new Author(req.body);

        await author.save(); //save in DB

        res.status(200).json({

            sucess : true,

            message : "New author added sucessfully",

            data : author,

        });

    } catch (error) {

        console.error(error);

        res.status(500).json({

            sucess : false,

            message : "somethin went wrong when Auhtor"

        })

    }

}

const createBook = async(req,res) =>{

    try {

        const book = new Book(req.body);

        await book.save(); //save in DB

        res.status(200).json({

            sucess : true,

            message : "New book added sucessfully",

            data : book,

        });

    } catch (error) {

        console.error(error);

        res.status(500).json({

            sucess : false,

            message : "somethin went wrong when Book"

        })

    }

}

  

const getbookAuthor = async(req,res)=>{

    try {

        //Find the bookl

        const book = await Book.findById(req.params.id).populate('author');

        //.populate means the book id will ref to the author
  

        if(!book){

            return res.status(400).json({

                sucess : false,

                message : "No book exists for this id",

            });

        }

         res.status(200).json({

            sucess : true,

            message : "book found",

            data : book,

        })

    } catch (error) {

        console.error(error);

        res.status(500).json({

            sucess : false,

            message : "somethin went wrong when Book"

        })

    }

}

module.exports = { createAuthor,createBook,getbookAuthor };
```

## Book routes

```node
const express = require('express');

  

const { createAuthor,createBook,getbookAuthor } = require("../controllers/book-controller");

  

const router = express.Router();

  

router.post('/author',createAuthor);

router.post('/book',createBook);

router.get('/:id',getbookAuthor);

  

module.exports = router;
```