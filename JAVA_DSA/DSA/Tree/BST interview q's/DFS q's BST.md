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
## kth smallest node in BST

```java
public int kthSmallest(TreeNode root,int k){
return helper(root,k).val;
}
private TreeNode  helper(TreeNode root,int k){
if(root ==null ){
return null;
}

//CHECK FOR LEFT SIDE

TreeNode left = helper(root.left,k);

if(left!=null){
return root;
}
//INCRASE THE COUNTER
count ++;

//AND CHECK IF THAT COUNT == K

if(COUNT == K){
return root;
}

//CHEK FOR LEFT SIDE AND RETURN

return helper(root.right,k);


}
```


## Construct a binary tree using inorder and preorder

```java
class Solution {

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        if(preorder.length ==0 ){

            return null;

        }

        //GETTING THE FIRST ELEMENT AS ROOT

        int value= preorder[0];

        int index = 0;

        //RUN A LOOP  INORDER TO FIND THE ROOT

  

        for(int i=0;i<inorder.length;i++){

            if(inorder[i]==value){

               index = i;

            }

        }

        //GETTING THE VALUE FOR RECCURSION ALSO

        TreeNode node = new TreeNode(value);

        //LEFT SIDE START FROM LEFT SIDE OF PREORDER

        node.left = buildTree(Arrays.copyOfRange(preorder,1,index+1),Arrays.copyOfRange(inorder,0,index));

  

        // FOR RIGHT SIDE THE RECUSRION CALL WILL  START AFTER THE ROOT NODE

        node.right = buildTree(Arrays.copyOfRange(preorder,index+1,preorder.length),Arrays.copyOfRange(inorder,index+1,inorder.length));

  

        return node;

    }

}

```


## Serilization && Deserilization of BST

```java
public String serialize(TreeNode root) {

        //IF ROOT IS NULL RETURN NULL

        if(root == null ){

            return null;

        }

        //OTHERWISE CREATE A STACK TO STORE THE VAL

        Stack<TreeNode> s = new Stack<>();

        s.push(root);

  

        //CREATE A LIST OUT OF Arraylist

        List<String> l = new ArrayList<>();

  

        while(!s.isEmpty()){

            TreeNode t = s.pop();

  

            //IFF CURRENT NODE IS NULL, STORE MARKER

                if (t == null){

                    l.add("#");

                }else{

                    //STORE THE CURRENT NODE

                    //rECURSION FOR ITS CHILD

                    //PUSHING  RIGHT BECAUSE LEFT WLL COME FIRST OUT

                    l.add(""+ t.val);

                    s.push(t.right);

                    s.push(t.left);

                }

        }

        //ATLAST IN FILE SPARATE BY ,

        return String.join(",",l);

    }

  

    int t;

    // Decodes your encoded data to tree.

    public TreeNode deserialize(String data) {

        if (data == null){

            return null;

        }

        t = 0;

        String[] arr = data.split(",");

        return helper(arr);

    }

    private TreeNode helper(String[]arr){

        if(arr[t].equals("#")){

            return null;

        }

  

        //CREATE THE NODE WITH THIS ITEM

        //RECUR FOR CHILD

        TreeNode root = new TreeNode(Integer.parseInt(arr[t]));

        t++;

        root.left = helper(arr);

        t++;

        root.right = helper(arr);

        return root;

  

    }

}
```


## max bst path sum

```java
class Solution {

    int ans = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {

        helper(root);

        return ans;

    }

    private int helper(TreeNode root){

        if(root == null){

            return 0;

        }

        //RESCURSION FOR LEFT AND RIGHT

        int left = helper(root.left);

        int right = helper(root.right);

  

        ///THIS WILL IGNORE NEGATIVE VAL

        left = Math.max(0,left);

        right = Math.max(0,right);

  

        //THIS WILL GIVE MAX VALUE FROM THAT CURRENT  NODE FROM LEFT AND RIGHT

        int pathSum = left + right  + root.val;

  

        //MAX OVERALL ANS

        ans = Math.max(ans,pathSum);

  

        return Math.max(left,right)+root.val;

    }

}
```

## Path sum

```java
class Solution {

    public boolean hasPathSum(TreeNode root, int targetSum) {

        if(root == null) {

            return false;

        }

  

        //IF THE CURRENT NODE IS LEAF NODE

        //AND VAL == TARGETSUM

        if(root.val == targetSum && root.left == null && root.right == null){

            return true;

        }

  

        //REURSION FOR LEFT AND RIGHT

        return hasPathSum(root.left,targetSum-root.val) || hasPathSum(root.right,targetSum-root.val);

    }

}
```

## Sum root to leaf

```java
class Solution {

    public int sumNumbers(TreeNode root) {

        return helper(root,0);

    }

    private int helper(TreeNode root,int sum){

        if(root == null){

            return 0;

        }

  

        //SUM = PREV SUM *10 + CURRENT VALUE

        sum = sum * 10 + root.val;

  

        if(root.left == null && root.right == null){

            return sum;

        }

  

        //ATLAST RETURN LEFT + RIGHT

  

        return helper(root.left,sum)+ helper(root.right,sum);

  

    }

}
```
## PATH SUM II

```JAVA
class Solution {

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {

        List<List<Integer>> result = new ArrayList<>();

        List<Integer> path = new ArrayList<>();

        helper(root,targetSum,result,path);

        return result;

    }

  

    private void helper(TreeNode node,int targetSum,List<List<Integer>>result,List<Integer> path){

        if(node == null){

            return;

        }

  

        //ADD THE CURRENT VAL TO THE PATH

        path.add(node.val);

  

        //IF TARSUM EQ TO CURRENT VAL ADD TO RESULT

        if(node.left == null && node.right == null  && targetSum ==node.val){

            result.add(new ArrayList<>(path));

        }else{

            //RECUR FOR LEFR AND RIGHT

            helper(node.left,targetSum - node.val ,result,path);

            helper(node.right,targetSum - node.val ,result,path);

        }

        //BACKTRACK IF SUM IS NOT EQ TO TARSUM

        path.remove(path.size()-1);

    }

}
```