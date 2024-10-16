#  Since Binary search tree has limitation to solve this avl tree is introduced

# An avl tree is a self balanced tree which balances itself to obtain height of  For every node in a tree the height should be -1,0,1


>Code for  inserstion and balancing of node

```java
 public class AVL {  
    static class Node {  
        int data;  
        Node left, right;  
        int height;  
  
        public Node(int item) {  
            this.data = item;  
            this.right = this.left = null;//also have to call left and right node  
            height = 1;  
        }  
    }  
  
    // a function to get the height of tree  
    static int height(Node node) {  
        if (node == null)  
            return 0;  
        return node.height;  
    }  
  
    public static Node insert(Node node, int data) {  
        if (node == null) {  
            return new Node(data);  
        }  
        if (data < node.data) {  
            node.left = insert(node.left, data);  
        } else if (data > node.data) {  
            node.right = insert(node.right, data);  
        }  
  
  
        //update the height of node  
        node.height = 1 + Math.max(height(node.left), height(node.right));  
  
        return roate(node);  
    }  
  
    private static Node roate(Node node) {  
        if (height(node.left) - height(node.right) > 1) {  
            //means left is getting unblanced so two left cases  
  
            //LL case            if (height(node.left) - height(node.right) > 0) {  
                return rightRotate(node);  
            }  
            if (height(node.left) - height(node.right) < 0) {  
                node.left = roateLeft(node.left);  
                return rightRotate(node);  
            }  
        }  
        if (height(node.left) - height(node.right) < -1) {  
            // right heavy  
            if (height(node.right.left) - height(node.right.right) < 0) {  
                // right right case  
                return roateLeft(node);  
            }  
            if (height(node.right.left) - height(node.right.right) > 0) {  
                // left right case  
                node.right = rightRotate(node.right);  
                return roateLeft(node);  
            }  
        }  
        return node;  
    }  
  
    //rotation function  
  
    private static Node rightRotate(Node p) {  
        Node c = p.left;  
        Node t = c.right;  
  
        c.right = p;  
        p.left = t;  
  
        p.height = Math.max(height(p.left), height(p.right) + 1);  
        c.height = Math.max(height(c.left), height(c.right) + 1);  
  
        return c;  
  
    }  
  
    public static Node roateLeft(Node c) {  
        Node p = c.right;  
        Node t = p.left;  
  
        p.left = c;  
        c.right = t;  
  
        p.height = Math.max(height(p.left), height(p.right) + 1);  
        c.height = Math.max(height(c.left), height(c.right) + 1);  
        return p;  
    }  
    public static void printPreorder(Node root) {  
        if (root == null) {  
            return;  
        }  
  
        //this will print the root node  
        System.out.print(root.data + " ->");  
  
        //visite the left node fist  
        printPreorder(root.left);  
  
        //this will print the right node  
        printPreorder(root.right);  
    }  
  
    public static void main(String[] args) {  
        Node root = null;  
  
        // Constructing tree given in the above figure  
        root = insert(root, 10);  
        root = insert(root, 20);  
        root = insert(root, 30);  
        root = insert(root, 40);  
        root = insert(root, 50);  
        root = insert(root, 25);  
  
        System.out.println("Preorder traversal : ");  
        printPreorder(root);  
  
    }  
}
```