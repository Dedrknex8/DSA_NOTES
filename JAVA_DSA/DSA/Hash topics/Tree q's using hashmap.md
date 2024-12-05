
> Construct a BST using inorder and preorder traversal

```
class Solution {

    int PreOrderIdx = 0;

    //Let's do it hashmap

    HashMap<Integer,Integer> InOrdermap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        //fill the map with inorder idice

        for(int i=0;i<inorder.length;i++){

            //MAP .PUT KEY,,VAL

            InOrdermap.put(inorder[i],i);

        }

        return helper(preorder,0,inorder.length-1);

    }

  

    private TreeNode helper(int[]preorder,int start,int end){

        if (start>end){

            return null;

        }

  

        //Pick the current root from preOrder traversal

        int rootValue = preorder[PreOrderIdx++];

        TreeNode root =  new TreeNode(rootValue);

  

        //FIND THE ROOT IN INORDER

        int inOrderIdx = InOrdermap.get(rootValue);

        //RECURSIVELY CONSTRUCT LEFT AND RIGHT

        root.left  = helper(preorder,start,inOrderIdx-1);

        root.right  = helper(preorder,inOrderIdx+1,end);

  

        return root;

    }

}

```

## Complexity
TIme : o(N) -> same for space complexity


## Vertical tree traversal

```java
class Solution {

    public List<List<Integer>> verticalTraversal(TreeNode root) {

  

      List<List<Integer>> ans = new ArrayList<List<Integer>>();

  

    if (root == null) {

      return ans;

    }

  

    int col = 0;

  

    Queue<Map.Entry<TreeNode, Integer>> queue = new ArrayDeque<>();

    Map<Integer, ArrayList<Integer>> map = new HashMap();

  

    queue.offer(new AbstractMap.SimpleEntry<>(root, col));

  

    int min = 0;

    int max = 0;

  

    while(!queue.isEmpty()) {

      Map.Entry<TreeNode, Integer> removed = queue.poll();

      root = removed.getKey();

      col = removed.getValue();

  

      if(node != null) {

        if(!map.containsKey(col)) {

          map.put(col, new ArrayList<Integer>());

        }

  

        map.get(col).add(root.val);

  

        min = Math.min(min, col);

        max = Math.max(max, col);

  

        queue.offer(new AbstractMap.SimpleEntry<>(root.left, col-1));

        queue.offer(new AbstractMap.SimpleEntry<>(root.right, col+1));

      }

    }

  

    for(int i=min; i <= max; i++) {

      ans.add(map.get(i));

    }

  

    return ans;

  }

}
```