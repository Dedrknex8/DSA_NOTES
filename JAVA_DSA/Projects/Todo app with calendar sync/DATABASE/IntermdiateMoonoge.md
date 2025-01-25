# Date 23-01-25 || Rohit Tiwari

## Topic to be covered

- [ ] Understanding the aggregation pipeline
- [ ] Using common aggreagtaion operators
- [ ] understanding document references
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