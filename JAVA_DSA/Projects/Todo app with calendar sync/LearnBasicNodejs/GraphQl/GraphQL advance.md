> In this am gonna add DB like mongoose to work with.

> Firstly install mongoose and do all the config like 

### Create new productschema

```node
const mongoose = require('mongoose');
const ProductSchema = new mongoose.Schema({

    title : {

        type : String,

        required : true,

    },

    category : {

        type : String,

        required : true,

    },

    price : {

        type : Float,

        required : true,

    },

    instock : {

        type : Boolean,

        required : true,

    },

})

  

module.exports = mongoose.model("Product",ProductSchema);
```



## simply in serve.js connect the new DB method

```node
require('dotenv').config()

const connecTodb = require('./database/db');

const { ApolloServer } = require("@apollo/server");

const { startStandaloneServer } = require("@apollo/server/standalone");

const typeDefs = require("./graphql/schema");

const resolvers = require("./graphql/resolver");

  

async function startServer() {

  await connecTodb()

  const server = new ApolloServer({

    typeDefs,

    resolvers,

  });

  const { url } = await startStandaloneServer(server, {

    listen: { port: process.env.PORT },

  });

   console.log(`Server ready at: ${url}`);

}

startServer();
```


## Now change the path in resolver to new modells instead of dummy data used previously

That's it now we can use crud commands to learn more 

[link](https://github.com/Dedrknex8/AdvanceGraphqlwithMongo)
