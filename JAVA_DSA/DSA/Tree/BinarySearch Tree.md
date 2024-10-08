
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