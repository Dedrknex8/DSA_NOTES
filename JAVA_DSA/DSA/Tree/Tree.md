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

## Types of tree


1.  On the basis of NUm of child
	- Full binary tree : tree with 0,1,2 child
	- degenetate  :  only 1 child
	- Skewed binary tree: tree in which all the nodes have only either 1 child or 0 child.

2. On The basis of completness of level
	- Complete Binary tree : all level are filled execpt the lowest node 
		- Application: Heap sort & heap-sort based dsa
	- Perefect Binary Tree: all the leaf nodes are at the same depth, and all non-leaf nodes have two children
	- Balanced Binary tree : A binary tree is balanced if the height of the tree is ****O(Log n)**** where n is the number of nodes.
- ****On the basis of Node Values:****
    - [Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
    - [AVL Tree](https://www.geeksforgeeks.org/introduction-to-avl-tree/)
    - [Red Black Tree](https://www.geeksforgeeks.org/introduction-to-red-black-tree/)
    - [B Tree](https://www.geeksforgeeks.org/introduction-of-b-tree-2/)
    - [B+ Tree](https://www.geeksforgeeks.org/introduction-of-b-tree/)
    - [Segment Tree](https://www.geeksforgeeks.org/segment-tree-data-structure/)



## Binary insertion operations

```java
import java.util.Scanner;  
  
public class Tree {  
  
    public static class Node {  
        int data;  
        Node left;  
        Node right;  
  
        public Node(int data) {  
            this.data = data;  
            left = null;  
            right = null;  
        }  
    }  
  
    static Node root;  // Static root node for the tree  
  
    public static void insert(Scanner sc) {  
        System.out.println("Enter the data: ");  
        int value = sc.nextInt();  
        root = new Node(value);  // Use the class field 'root', no local declaration  
        insert(sc, root);  
    }  
  
    private static void insert(Scanner sc, Node node) {  
        System.out.println("Do you want to enter to the left of " + node.data + "? (true/false)");  
        boolean left = sc.nextBoolean();  
        if (left) {  
            System.out.println("Enter the data: ");  
            int value = sc.nextInt();  
            node.left = new Node(value);  
            insert(sc, node.left);  // Recursively insert in the left subtree  
        }  
  
        System.out.println("Do you want to enter to the right of " + node.data + "? (true/false)");  
        boolean right = sc.nextBoolean();  
        if (right) {  
            System.out.println("Enter the data: ");  
            int value = sc.nextInt();  
            node.right = new Node(value);  
            insert(sc, node.right);  // Recursively insert in the right subtree  
        }  
    }  
  
    public static void display() {  
        display(root, "");  
    }  
  
    public static void display(Node node, String indent) {  
        if (node == null) {  
            return;  // Base case: stop when we reach a null node  
        }  
        System.out.println(indent + node.data);  // Display the current node's data  
        display(node.left, indent + "  ");  // Recur for the left subtree  
        display(node.right, indent + "  ");  // Recur for the right subtree  
    }  
  
    public static void main(String[] args) {  
        Scanner sc = new Scanner(System.in);  // Create a scanner to take user input  
        Tree tree = new Tree();  // Create an instance of Tree  
        tree.insert(sc);  // Insert nodes into the tree  
        tree.display();  // Display the tree structure  
    }  
}
```

