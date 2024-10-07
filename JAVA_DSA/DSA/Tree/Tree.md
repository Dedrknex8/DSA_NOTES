>What is tree

A ****Binary Tree Data Structure**** is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. It is commonly used in computer science for efficient storage and retrieval of data, with various operations such as insertion, deletion, and traversal.

- Each binary tree has 3 tree parts 
	- data (elements that it contain) {int data}
	- ppointer to the left child {Node left}
	- pointer to the right child {Node right}
![[Pasted image 20241007092656.png]]

#### My explaination
-  Think tree as family structure suppose father is  root node and two child  name right and left 
- right stays at right side of father and left on the left

>Why tree ?

- Because tree is efficient it has 0(log n) time complexity
- elements are stored in order


> How  tree  is implemented ?

## Sample code to create a node of a tree

```java
// Class containing left and right child
// of current node and key value
class Node {
    int data;
    Node left, right;
    public Node(int item)
    {
        data = item;
        left = right = null;
    }
}

```

## Let's create a tree with four nodes (2,3,4,5)

```java
public class Tree {  
  
    public static class Node{  
        int data;  
        Node left;  
        Node right;  
  
        public Node(int data){  
            this.data = data;  
            left = null;  
            right = null;  
        }  
    }  
  
    public static void main(String[] args) {  
        //Initialize and allocate memory for noes  
        Node firstnode = new Node(2);  
        Node secondnode = new Node(3);  
        Node thirdnode = new Node(4);  
        Node fourthnode = new Node(5);  
  
        //let's connect the  node to binary tree  
  
        firstnode.left = secondnode;  
        firstnode.right = thirdnode;  
        secondnode.left = fourthnode;  
  
    }  
}
```


> why tree is need and where does it implemented ?

- Are to represent a file system 
- Databases 
- Network routing
- To solve complex mathamatical problems
- Desicion tree
- compression of files *Imp* 



