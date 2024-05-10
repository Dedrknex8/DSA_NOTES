
# What is array?

>- Array is a collection of objects stored in heap memory. An array should have same data types in it

```
Syntax

int [] arr = new int[size of array]

#int defines the data type [] -> is an array, new is a keyboard of making objects or say initializing objects 


```

> 2D array which also known as 2 dimensional array in which array is stored in rows and columns
> 
```
#syntax

int[][] arr = new int[size of rows][size  of column]

#size of row must be define but column


```

> [!NOTE]
> > ==## How it's working behind the Scence==

> Let's say we created a 2D array like

int arr[][][] = {1,2,3},
         {4,5,6},
         {7,8,9};
```
#Now here it's working like int arr[][]=[a,b,c] where a={1,2,3} and b={4,5,6} and so on 
```

# ARRAYLIST V/S Array?

>So when we creat an Array we have to delcare it's capacity but in arrayList it automatically adjust the capacity. It's helpfull when u dont know how much object has to be insert in an array

```java

int[] array = new int[size has to be mentioned];

// But in Arraylist

ArrayList<Integer> array = new ArrayList<"size doesn't matter">();
```

<> -> this in Arraylist is known as wrapper class

```
In Java, a wrapper class is a class that wraps a primitive data type and provides additional functionality. Wrapper classes are used to convert primitive data types into objects, which can then be used in object-oriented programming.

Wrapper classes are also used to represent primitive data types in collections. For example, the ArrayList class can only store objects, so if you want to store primitive data types in an ArrayList, you must first convert them to wrapper objects
```

want to know more about watch this ==https://www.youtube.com/watch?v=NbYgm0r7u6o&ab_channel=CodingwithJohn==

