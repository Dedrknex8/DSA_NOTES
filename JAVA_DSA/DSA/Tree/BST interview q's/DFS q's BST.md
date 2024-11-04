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