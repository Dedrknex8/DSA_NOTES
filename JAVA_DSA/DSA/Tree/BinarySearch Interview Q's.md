
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

## Zig zag

```java


class Solution {

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();

  

        // If the tree is empty

        if (root == null) {

            return result;

        }

  

        // Use a queue for level order traversal

        Queue<TreeNode> queue = new LinkedList<>();

        queue.add(root); // Start with the root node

        boolean reverse = false;

  

        while (!queue.isEmpty()) {

            List<Integer> level = new ArrayList<>();

            int size = queue.size(); // Number of nodes at the current level

  

            for (int i = 0; i < size; i++) {

                TreeNode cur = queue.poll(); // Remove the node from the queue

  

                // Add node values in normal or reversed order based on `reverse`

                if (reverse) {

                    level.add(0, cur.val); // Add at the beginning for reverse order

                } else {

                    level.add(cur.val); // Add at the end for normal order

                }

  

                // Always add left and right children in the same order to the queue

                if (cur.left != null) {

                    queue.add(cur.left);

                }

                if (cur.right != null) {

                    queue.add(cur.right);

                }

            }

  

            // Add the current level to the result list

            result.add(level);

  

            // Toggle the reverse flag for the next level

            reverse = !reverse;

        }

  

        return result;

    }

}
```

# Level order traversal ll

Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

```java
/**

 * Definition for a binary tree node.

 * public class TreeNode {

 *     int val;

 *     TreeNode left;

 *     TreeNode right;

 *     TreeNode() {}

 *     TreeNode(int val) { this.val = val; }

 *     TreeNode(int val, TreeNode left, TreeNode right) {

 *         this.val = val;

 *         this.left = left;

 *         this.right = right;

 *     }

 * }

 */

class Solution {

    public List<List<Integer>> levelOrderBottom(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();

  

        //if tree is empty

        if (root == null) {

            return result;

        }

        //Use a queue for level order traversal

        Queue<TreeNode> queue = new LinkedList<>();

        queue.add(root); //start with root node

  

        while (!queue.isEmpty()) {

            List<Integer> level = new ArrayList<>();

  

            int size = queue.size(); //hold the no of nodes in current level

            for (int i = 0; i < size; i++) {

                TreeNode cur = queue.poll(); //remove node from queue

  

                //add the current node's val level to current quele

                level.add(cur.val);

  

                // if left child exist add

                if (cur.left != null) {

                    queue.add(cur.left);

                }

                if (cur.right != null) {

                    queue.add(cur.right);

                }

            }

            //add the overall node value here from beg

            result.add(0, level);

        }

  
  

        return result;

    }

}
```


## Right side view 

>Leetcode  : `https://leetcode.com/problems/binary-tree-right-side-view/submissions/1435983246 `

```java
List<Integer> result = new ArrayList<>();

  

        if(root == null){

            return result;

        }

  

        Queue<TreeNode> queue = new LinkedList<>();

  

        queue.add(root); //starts from root

  

        while(queue.isEmpty()){

            List<Integer> level = new ArrayList<>();

            int size = queue.size(); //hold the current no of nodes

            for(int i =0; i < size;i++){

                TreeNode curr = queue.poll();

                if(i == size - 1){

                    result.add(curr.val);

                }

                if(curr.left!=null){

                    queue.add(curr.left);

                }

                if(curr.right!=null){

                    queue.add(curr.right);

                }

            }

        }

         return result;

    }
```