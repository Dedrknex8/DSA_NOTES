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
 
>For this we need a user with  email,pass,username

### Detail description for our schema

>Username : it will contain name [unique], created at, 
>email: email address [unique], lowercase,
>passwd : strong pass, encrypt.
>role : either be a user or an  admin `use enum for it`,use default to be a user.

### For password
> We have to have to implement a  `hashing property`

> 