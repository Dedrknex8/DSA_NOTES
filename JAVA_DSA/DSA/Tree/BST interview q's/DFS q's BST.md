# Diameter of tree with height

```java

    public int diameterOfBinaryTree(TreeNode root) {

        // FIRST LET'S GET THE HEIGHT OFTHE TREE

       if(root == null){

        return 0;

       }

  

       int leftHeight = height(root.left);

       int rightHeight = height(root.right);

  

       int ldiameter = diameterOfBinaryTree(root.left);

       int rdiameter = diameterOfBinaryTree(root.right);

  

      return Math.max(leftHeight + rightHeight, Math.max(ldiameter, rdiameter));

    }

    private int height(TreeNode root){

        if (root == null)

            return 0;

  

        // If tree is not empty then height = 1 +

        // max of left height and right heights

        return 1 + Math.max(height(root.left), height(root.right));

    }
```


## Invert of binary tree [easy q's]

```java
public TreeNode invertTree(TreeNode root) {

        if (root == null){

            return null;

        }

  

        TreeNode left =  invertTree(root.left);

        TreeNode right =  invertTree(root.right);

  

        root.left = right;

        root.right = left;

  

        return root;

    }

}
```

## Sorted array to BST

```java
 public TreeNode sortedArrayToBST(int[] nums) {

        //LET'S CREATE A BINARY TREE

        return recusrion(nums,0,nums.length-1);

    }

  

    private TreeNode recusrion(int[] nums,int start,int end){

        if(start > end){

            return null;

        }

  

        //Lets find mid

        int mid = start + (end -start) / 2;

  

        //CREATE ROOT NODE

  

        TreeNode root = new TreeNode(nums[mid]);

  

        //CREATE LEFT AND RIGHT SUBTREE

  

        root.left = recusrion(nums,start,mid-1);

        root.right = recusrion(nums,mid+1,end);

  

        return root;

    }
```