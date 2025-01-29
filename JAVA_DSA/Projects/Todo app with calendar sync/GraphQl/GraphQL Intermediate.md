
# date 28-01-25 || Rohit Tiwari

## What is GraphQL ?
>A graphql is a query language for API's and is developed by facebook. It's similar to REST API but more powerful.

> The main advantages of graphql over REST API is that it can give precise data that mean under fetching which increase performance in a system.

## Requirements

1. npm init -y
2. nodemon
3. appolo server 
4. graphql
5. graphql-tag

Command -> `npm i @apollo/server graphql graphql-tag nodemon --save-dev`

## apollo sever

>**Apollo Server is an [open-source](https://github.com/apollographql/apollo-server), spec-compliant GraphQL server** that's compatible with any GraphQL client, including [Apollo Client](https://www.apollographql.com/docs/react). It's the best way to build a production-ready, self-documenting GraphQL API that can use data from any source.



## ALL CRUD COMMANDS


# Schema /routers

```
// this is the structure for the DB

const {gql} = require('graphql-tag');

  

const typeDefs = gql`

    type Product {

    id : ID!

    title : String!

    category : String!

    price: Float!

    instock: Boolean!

    }

    #TO GET QUERY ITEM BY ID

    type Query {

    products : [Product!]! #GET ALL THE PRODUCTS

    product(id: ID!): Product # GET SINGLE PRODUCT

    }

  

    type Mutation {

        createProduct(

            title: String!

            category: String!

            price: Float!

            instock: Boolean!

        ): Product

        deleteProduct(id : ID!) : Boolean

        updateProduct(

            id:ID!

            title  : String

            category  : String

            price :  Float

            instock  : Boolean

        ): Product

    }

`;

  

module.exports = typeDefs;
```
# reslovers /controllers

```node
// methods like routes

  

const product = require('../data/production');

const products = require('../data/production');

  

const resolvers  = {

    Query : {

        products:()=> products,

        product: (_, { id }) => products.find((item) => item.id === id),

    },

    Mutation : {

        createProduct : (_, { title,category,price,instock }) => {

            const newlyCreatedProduct = {

                id : String(products.length +1),

                title,

                category,

                price,

                instock

            }

            products.push(newlyCreatedProduct);

            return newlyCreatedProduct;

        },

  

        deleteProduct : (_,{id}) =>{

            const idx = products.findIndex(item =>item.id === id);

            if(idx === -1){

                return false;

            }

  

            products.splice(idx,1);

  

            return true;

        },

        updateProduct : (_,{ id, ...updates}) =>{

            const Idx = products.findIndex(items => items.id === id);

  

            if(Idx === -1){

                return null

            };

  

            const updateProduct  ={

  

                ...products[Idx], ...updates

            }

  

            product[Idx] = updateProduct;

  

            return updateProduct

  
  
  
  

        }

    }

}

  

module.exports = resolvers;
```
