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

# For password
> We have to have to implement a  `hashing property`

> using bcryptjs npm package for that will salt a text/plain passwd into a hashed password

> To read more about click on this -> [link](https://www.npmjs.com/package/bcrypt)

 
> To install use `npm i bcryptjs`  

### How it's working

> first we will let user enter a passwd then we will salt it and send it to database for `/register part`

> Need to create a json web token in order to user to login 
> For that use [jsonwebtoken](https://npmjs.com/package/jsonwebtoken)
> Login part done !


`Summary` : 
	what have i learned so far, I have create a simple login and register part where i used the register part to create a user with role that role with either be a admin or user they two endpoint `home` & `admin` . The home page can be accessed by the admin and user[`note u have to login first`] but the admin page can only be accessed by admin role user.
	How implemented this used middleware,bcryptjs -> to hash the pasword , jsonwebtoken -> to create a token that can be used to authorized a user to the site so that they can access the page as required. Refenrence to the [page](https://github.com/Dedrknex8/Authenticaion-js)
	At the learning and practicising makes u perfect ! Don't fear face the challenge  
### What after login

> Two options either the user is admin or a normal user if normal user then add some restrictions to it 



## Timestamp

>When `timestamps: true` is specified in a Mongoose schema, it automatically creates two fields in your documents:

1. **`createdAt`**: A `Date` field that stores the timestamp when the document was first created.
2. **`updatedAt`**: A `Date` field that stores the timestamp when the document was last updated.

## Installing bycrypt for node js

## Done with the login part