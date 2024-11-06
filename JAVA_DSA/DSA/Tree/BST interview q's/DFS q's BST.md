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

# Flatern BST into linked list using preorder

```java
//START FROM ROOT NODE
TreeNode current = root;

  
		//CHECK IF ROOT NODE IF EMPTY
        while(current !=null){
			// THEN TRAVERSE TO LEFT
            if(current.left!=null){
			//MAKE THE LEFT AS TEMP 
                TreeNode temp = current.left;
				// GO ON TILL FOUND THE .RIGHT AS NULL
                while(temp.right != null){
					
                    temp = temp.right;

                }
				//WHEN FOUND THEN TEMP WILL BE ONE
				//ABOVE MAKE IT'S RIGHT TO CURRENT 
				//RIGHT 
                temp.right = current.right;

                current.right = current.left;
					//MAKE IT LEFT AS NULL
                current.left=null;

            }
			//MAKE CURRENT AS CURRENT RIGHT
            current = current.right;

        }

    }
```

## Check if a binary tree is valid or not

> 1.  TO be a valid it need to have two child 
> 2. It's has to follow min and max rule

```java
public boolean isValidBST(TreeNode root) {

        return helper(root,null,null);

    }

    private boolean helper(TreeNode node,Integer low,Integer high){

        //  IF ROOT IS NULL THAT MEANS  TREE

        if(node == null){

            return true;

        }

  

        //CHECK IF THE LOW IS NOT NULL

        //AND IT'S VAL IS SAME AS LOW

        if(low != null && node.val <=low){

            return false;

        }

        //SAME FOR HIGH VALUE SHOULD BE LOWER THEN LIMIT

        if(high!=null && node.val >=high){

            return false;

        }

  

        boolean leftSubTree = helper(node.left,low,node.val);

        boolean rightSubTree = helper(node.right,node.val,high);

  
  

        //ATLAST BOTH BOTH SHOULD BE TRUE

  

        return leftSubTree && rightSubTree;

    }

}
```