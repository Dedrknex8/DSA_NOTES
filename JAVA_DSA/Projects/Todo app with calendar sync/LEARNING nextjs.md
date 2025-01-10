
# Date 05-01-25 | Rohit Tiwari

# Topics to be covered

 - [ ] Installation
 - [ ] Node module system
 - [ ] Path module
 - [ ] File System
 - [ ] Http module
 - [ ] calllbacks and callback hell
 - [ ] Promises
 - [ ] Async Await
 - [ ] Event emitter
 - [ ] 


## Installation

> Started my first day with installation of node js 
> And learning it from the scratch as have no idea about it
### Node js module export

> Okay so module export it just like components in react js 

```node js
//CREATE FILE AS app,js
module.export = "My_New_module";

//create a another file name as index.js

const Name = require("./app"); //REUQIRE IS LIKE IMPORT FUNCTION IN REACT JS
console.log(Name);
```


### Exporting a function to another file

1. Create a file arithmatic.js
```node
function add(a,b){
return a+b;
}
function subtract(a,b){
return a-b;
}
function Multiply(a,b){
return a*b;
}

module.export = {
add,substract,multiply
};
```

2. Create a new Index.js

```node

const maths = require("./arithmatic");

console.log(arithmatic.add(1.2));
```

## To GET THE OUPUT IN CLI

1. open terminal in same dir
2. node index.js
3. Output : 3

## Error catch code

> Supoose in above function i have a divide function that try to divide with zero which will give error

```node 
function divide(a,b){
if(b ===0){
console.log("Dividing with zero is not allowed");

}
return a/b;
}
```

```node
const functions = require('./arithmatic');

try{ //this will first try to divide
console.log('trying to divide with zero);
let result = functions.divide(10,0);
console.log(result);
}catch(error){ //this will try to catch the error 
console.log("caught an error",error.message);
}
```


## Module Wrapper Function

>Under the hood, NodeJS does not run our code directly, it wraps the entire code inside a function before execution. This function is termed as Module Wrapper Function.

>Before a module’s code is executed, NodeJS wraps it with a function wrapper that has the following structure:

```node
(
function (exports,require,module,__filename,__dirname){
//Module code here
});
```

## NPM manager

>To load other depencies like magod.express.js

1. Need to install npm first
2. cli `npm install`
3. give entery index like index.js {every code will render from here like index.html}
4. Done

## Path module

> Path modules provides utility to work with path and directories 

#### Now the q's arise what is the utitlity here?
> To answer this the utility nothing more of a function which provide the dir realted command and queries

> Let's try to console the current path 

```node
const { dir } = require('console');

const path = require('path');

//LET'S PRINT CURRENT DIR NAME  

console.log("Current dir path is : ",path.dirname(__filename));

console.log("Current file name is : ",path.basename(__filename));

//LET'S PRINT THE CURRENT FILE EXTENSION NAME  

console.log("Current file ext : ",path.extname(__filename))
//LET'S TRY TO JOIN PATH OF DIR

const pathToBejoined = path.join('/Dummy',"/blob","/root","root.txt")


console.log(path.join(pathToBejoined)); // THIS WILL JOIN THE GIVEN DIR TO THE PATHS
```



## installed and run some command in nodejs 

> tommorow finfish whole nextjs course of 11 hour target


## File system

> It's is a way to create a file or read a file in node js

```node
//FILE SYSTEM

const fs = require('fs');

const path = require('path');
  
const  subdir = 'subdir';

const filename = 'test.txt';

const content = 'Hi there! A sample text here';

//CREATE THE FULL PATH FOR THE FILE

const filePath = path.join(__dirname,subdir,filename);

//CREATE THE DIR FIRST

fs.mkdir(path.join(__dirname,subdir), {recursive:true}, (err)=>{
    if (err){

        console.log(`error in creating the file $(err)`);

    } //RECUSVE : TRUE ENSURE THAT ROOT DIR EXISTS

  
//CREATE AND WRITE THE FILE


fs.writeFile(filePath,content,(err)=>{

    if (err){

        console.log("error wirting file",err);

    }else{

        console.log(`file created successfully at $(filepath)`)

    }

})

});
```

> FLOW OF THE CODE EXECUTED HERE
1. It will join the path
2. it will create the subdir fast 
3. Then i will create.txt file 
4. then write the content

## Read file in node

```node
const fs = require('fs');

const path = require('path');

const subdir = 'subdir';

const filename = 'test.txt';

const filePath = path.join(__dirname,subdir,filename);

//READ THE FILE

fs.readFile(filePath, 'utf8',(err,data)=>{

    if(err){

        console.log('error reading file: ',err);

    }else{

        console.log('File content',data);

    }

});
```
