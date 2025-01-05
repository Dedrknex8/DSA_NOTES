
# Date 05-01-25 | Rohit Tiwari

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

## To GET THE OUPUT IN CLI\

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
chachagh