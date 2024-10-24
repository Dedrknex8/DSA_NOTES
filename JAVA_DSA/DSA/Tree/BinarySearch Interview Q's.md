
# BFS (breadth first search)

> BFS means traversing the tree in level by level.

```java
import java.util.ArrayList;  
import java.util.LinkedList;  
import java.util.List;  
import java.util.Queue;  
  
public class Bigint {  
    public static void main(String[] args) {  
        Node root  = new Node(1);  
        root.left = new Node(2);  
        root.right = new Node(3);  
        root.left.left = new Node(4);  
        root.left.right = new Node(5);  
  
        List<List<Integer>> levelOrderResult = levelOrder(root);  
  
        System.out.println(levelOrderResult);  
  
  
  
    }  
    public static class  Node {  
        int val;  
        Node left;  
        ;  
        Node right;  
  
        Node(int val) {  
            this.val = val;  
        }  
  
        Node(int val, Node left, Node right) {  
            this.val = val;  
            this.left = left;  
            this.right = right;  
        }  
  
        private Node root;  
    }  
  
  
    //Defination of tree like node root etc  
    public static List<List<Integer>> levelOrder(Node root) {  
        List<List<Integer>> result = new ArrayList<>();  
  
        //if tree is empty  
        if (root == null){  
            return result;  
        }  
        //Use a queue for level order traversal  
        Queue<Node> queue = new LinkedList<>();  
        queue.add(root); //start with root node  
  
        while (!queue.isEmpty()){  
            List<Integer> level = new ArrayList<>();  
  
            int size = queue.size(); //hold the no of nodes in current level  
            for (int i = 0; i < size; i++) {  
                Node cur = queue.poll(); //remove node from queue  
  
                //add the current node's val level to current quele                level.add(cur.val);  
  
                // if left child exist add  
                if (cur.left != null){  
                    queue.add(cur.left);  
                }  
                if (cur.right != null){  
                    queue.add(cur.right);  
                }  
            }  
            //add the overall node value here  
            result.add(level);  
        }  
  
  
        return result;  
    }  
}
```
