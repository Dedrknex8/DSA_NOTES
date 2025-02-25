
## Date 25-02-25 || Rohit Tiwari

## Logical && and logical ||

1. Logical && : Check if both true => true
			if 1st false then doesn't check for 2nd value.
2. Logical || : if one true return => true
## Object Destructuring

```node

const id = 1;
const productname = "This is a electronic const product=  "mobile phone";
rating = 5;
}

const product2= {
description:"this is product 2 description",
productname,
id,
rating
};

const {id.productname,description} = product2 // this will desctructure the product 2 deatils
```

## Default param

> Deafult param take by default param in a function if no parameter is given during function call

```javascript
function multiplicaton(num1 , num2){
return num1 * num2;
}

//calling the function without parameter

multiplication();

--> output => NaN (not defined)

//FUCNTION WITH DEFAULT PARAM
function multiplicaton(num1=5 , num2=2){
return num1 * num2;
}

//calling the function with default parameter

multiplication();

--> output => 10
// FUNCTION WIH DEAFULT PARAM BUT OVERLOAD WITH ANOTHER PARAM DURING FUNC CALL
function multiplicaton(num1 , num2){
return num1 * num2;
}

//calling the function without parameter

multiplication(6,2);

--> output => 12
```

## spread operator 
>Used to spread a value in stead rewritting it

```node
const arr = [2,3,4];

console.log([...arr]) // 3 dot to spread
```

## REST PARAM
 >Using the same concept of spread operator
 >we can use spread operator in rest param
 
 ```node
 function usingRestParm(a,b,...c){
 console.log(a,b,c);
 console.log('Rest param end here!');
 }
usingRestParam(1,2,3,4,45,6,7,8,9);

// output => 1,2,[3,4,45,6,7,8,9]
			 //Rest param end here!
			
```


## Map fucntion

>Map is callback function that is use to map objects and return it's value

```javascript
const singlePerson = [{name='a',age=12,place=india},{name='b',age=15,place=china},{name='c',age=18,place=usa}];

let getAllName = singlePerson.map((getname,index)=>{
return ${getname.name};
});

log(getAllName)
```

## Find FUNCTION
>Find is a function that map object and returns the first value that match the conditon

```node
let getAllName = singlePerson.find((getname,index)=>{
return getname.place = india;
});

log(getAllName) // return 01

```

## Filter FUNCTION

> Filter is a function that match and returns all the value that match with the condition

## Some
> Check a function for a condition and return true if valid or else return false

## Every

>Check if all the objects in a function statisfy the condition or not.

```node
const singlePerson = [
{
name='a',age=12,place=india
},
{name='b',age=15,place=china
},
{
name='c',age=18,place=usa
}];

let getAllName = singlePerson.every((getname,index)=>{
return ${getname.age > 19};
});

log(getAllName) //return false 
```

## includes 
> Check if some object is available in array or not