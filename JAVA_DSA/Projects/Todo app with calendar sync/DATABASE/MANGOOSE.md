
## TO install mangoose in CLI

`npm i mangosose`

## First code of mongoose

```node
const mongoose = require('mongoose');
//CONNECT THE MANGOOSE newpasswd
mongoose.connect("mongodb+srv://wwerohitktiwari771:newpasswd@cluster0.kycar.mongodb.net/").then(()=>{console.log('datatbase connected successfully')}).catch((e)=>{console.log('this is erroor',e)});

//CREATE A DATABASE SCHEMA

const userSchema = new mongoose.Schema({

    name : String,

    email : String,

    age : Number,

    isAtcive : Boolean,

    tags : [String],

    createdAt : {type : Date,default : Date.now}

});

//CREATE USER MODEL => table

const user = mongoose.model('user',userSchema);

  async function runQueryExample(){

    try{

        // create a new user

        const newUser = await user.create({

            name : "Redone",

            email : "test@robert.com",

            age : 18,

            isAtcive : true,

            tags : ['dev','tester'],            

        })

        console.log(`Created a new user ${newUser}`);

        //GET ALL USER

        const allusers = await user.find({});

        console.log(allusers)

    }catch(e){

        console.log('Error of the code is ',e)

    }finally{

        await mongoose.connection.close();

    }

}

runQueryExample();
```

## Find users who isActive is false

```node
const mongoose = require('mongoose');

  

//CONNECT THE MANGOOSE newpasswd

mongoose.connect("mongodb+srv://wwerohitktiwari771:newpasswd@cluster0.kycar.mongodb.net/").then(()=>{console.log('datatbase connected successfully')}).catch((e)=>{console.log('this is erroor',e)});

  

//CREATE A DATABASE SCHEMA

const userSchema = new mongoose.Schema({

    name : String,

    email : String,

    age : Number,

    isAtcive : Boolean,

    tags : [String],

    createdAt : {type : Date,default : Date.now}

});

  

//CREATE USER MODEL => table

const user = mongoose.model('user',userSchema);

  

async function runQueryExample(){

    try{

         create a new user

         const newUser = await user.create({

             name : "John DOE",

             email : "test@john.com",

          age : 25,

             isAtcive : false,
	     tags : ['dev'],            

        })

        // console.log(`Created a new user ${newUser}`);

        // //GET ALL USER

        // const allusers = await user.find({});

        // console.log(allusers)

        const userNotActive = await user.find({isAtcive : true});

        console.log(userNotActive);

    }catch(e){

        console.log('Error of the code is ',e)

    }finally{

        await mongoose.connection.close();

    }

}

runQueryExample();
```

### Some more queries command
```node
const mongoose = require('mongoose');

  

//CONNECT THE MANGOOSE newpasswd

mongoose.connect("mongodb+srv://wwerohitktiwari771:newpasswd@cluster0.kycar.mongodb.net/").then(()=>{console.log('datatbase connected successfully')}).catch((e)=>{console.log('this is erroor',e)});

  

//CREATE A DATABASE SCHEMA

const userSchema = new mongoose.Schema({

    name : String,

    email : String,

    age : Number,

    isAtcive : Boolean,

    tags : [String],

    createdAt : {type : Date,default : Date.now}

});

  

//CREATE USER MODEL => table

const user = mongoose.model('user',userSchema);

  

async function runQueryExample(){

    try{

        // create a new user

        // const newUser = await user.create({

        //     name : "John DOE",

        //     email : "test@john.com",

        //     age : 25,

        //     isAtcive : false,

        //     tags : ['dev'],            

        // })

        // console.log(`Created a new user ${newUser}`);

        // //GET ALL USER

        // const allusers = await user.find({});

        // console.log(allusers)

        // const userNotActive = await user.find({isAtcive : true});

        // console.log(userNotActive);

        const selectField = await user.find().select('name email -_id');

        console.log(selectField);

    }catch(e){

        console.log('Error of the code is ',e)

    }finally{

        await mongoose.connection.close();

    }

}

runQueryExample();
```

## To delete a user

```node
 const deletedUser = await user.findByIdAndDelete(newUser._id);
         console.log('User deleted -> ',deletedUser);
```
## Update a user
```node
 const updateUser = await user.findByIdAndUpdate(newUser._id,{

            $set : {age : 100},

            $push : {tags : "updated"},

        },

        {

            new : true //this will push the update

        }

    );

    console.log("User updated sucessfully");
```