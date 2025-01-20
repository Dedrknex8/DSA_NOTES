## Authentication & Authorization

# date : 15-01-25 || Rohit Tiwari

> Authentication and authorization are two very important topics in node js
> Let's first discuss b/w authentication and authorization

> Authentication means proving yourself . For example when u go to airport u give them your identification card like driving license or something
> 

> AUTHORIZATION: means the permission you have like u don't have the permission to be in staff room in a airport .


## Installation and setup for this

> For the installation we need Express, Node, Mongoose, Node mon.

> After installation setup the files and directories.

## Schema 
> For this authentication we have to define the schema.
 
>For this we need a user with  `email,pass,username`

### Detail description for our schema

>Username : it will contain name [unique], created at, 
>email: email address [unique], lowercase,
>passwd : strong pass, encrypt.
>role : either be a user or an  admin `use enum for it`,use default to be a user.

### For password
> We have to have to implement a  `hashing property`

> using bcryptjs npm package for that will salt a text/plain passwd into a hashed password

> To read more about click on this -> [link](https://www.npmjs.com/package/bcrypt)

 
> To install use `npm i bcryptjs`  

### How it's working

> first we will let user enter a passwd then we will salt it and send it to database for `/register part`

> Need to create a json web token in order to user to login 
> For that use [jsonwebtoken](https://npmjs.com/package/jsonwebtoken)
> 



## Timestamp

>When `timestamps: true` is specified in a Mongoose schema, it automatically creates two fields in your documents:

1. **`createdAt`**: A `Date` field that stores the timestamp when the document was first created.
2. **`updatedAt`**: A `Date` field that stores the timestamp when the document was last updated.

## Installing bycrypt for node js

## Done with the login part
