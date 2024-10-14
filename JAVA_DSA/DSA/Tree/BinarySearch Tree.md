
> A BST is a special type of tree in which the node smaller than the root node is arranged in left side and node larger than root is arranged in right side of root

## Implementation

```java
public class BST {  
  
   static class Node {  
       int data;  
       Node left, right;  
  
       public Node(int item) {  
           this.data = item;  
       }  
  
       private Node root;  
   }  
  
   //basic operation  
    public static Node search(Node root, int data){  
        if(root == null || root.data == data){  
            return root;  
        }  
        //if data is greater than root than search right  
        if(root.data < data){  
            return search(root.right, data);  
        }  
        //if data is smaller than root  
            return search(root.left, data);  
  
    }  
  
    public static void main(String[] args) {  
        Node root = new Node(50);  
        root.left = new Node(30);  
        root.right = new Node(70);  
        root.left.left = new Node(20);  
        root.left.right = new Node(40);  
        root.right.left = new Node(60);  
        root.right.right = new Node(80);  
  
  
        System.out.println(search(root, 19) != null  
                ? "Found"  
                : "Not Found");  
        System.out.println(search(root, 80) != null  
                ? "Found"  
                : "Not Found");  
    }  
  
  
}
```



## Traversal techniques in BST

1. Pre-Order traversal : Root -> Left-> Right
- Used for evaluating math
- Used to make copy of binary tree
1. In-Order traversal : Left -> Root-> Right (it will go from leaf node of Left to root) 
   - It is used to visite node in BST  sorted manner 4
2. Post-Order traversal : Left->Right->Root
	- It is used to delete a node in BST

```java
public class BST {  
  
   static class Node {  
       int data;  
       Node left, right;  
  
       public Node(int item) {  
           this.data = item;  
           this.right=this.left=null; //also have to call left and right node  
        }  
   }  
  
   //basic Travsersal operation  
    public static void printInorder(Node root) {  
       if (root == null) {  
           return;  
       }  
       //visite the left node fist  
        printInorder(root.left);  
  
        //this will print the root node  
       System.out.print(root.data + " ->");  
  
       //this will print the right node  
       printInorder(root.right);  
    }  
  
  
    public static void main(String[] args) {  
        Node root = new Node(22);  
        root.left = new Node(12);  
        root.right = new Node(30);  
        root.left.left = new Node(8);  
        root.left.right = new Node(20);  
        root.right.left = new Node(25);  
        root.right.right = new Node(40);  
  
        // Function call  
        System.out.print("Inorder Traversal: ");  
        printInorder(root);  
    }  
  
  
}
```

> Note same thing goes for pre and POST order



## Problem with BST
> For every node in a tree the height should be -1,0,1 