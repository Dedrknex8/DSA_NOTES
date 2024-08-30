
# Find all permuation of a string

```java
public class Permuation {  
    public static void main(String[] args) {  
        Perm("","abc");  
        int ans = PermCount("","abcd");  
        System.out.println(ans);  
  
  
    }  
  
    private static void Perm(String p, String up) {  
    if (up.isEmpty()){  
        System.out.println(p);  
        return;  
    }  
  
    Character ch = up.charAt(0);  
  
    for (int i=0;i<=p.length();i++){  
        String f= p.substring(0,i);  
        String s = p.substring(i,p.length());  
        Perm(f+ch+s,up.substring(1));  
    }  
  
    }  
    private static int PermCount(String p, String up) {  
        if (up.isEmpty()){  
            return 1;  
        }  
  
        Character ch = up.charAt(0);  
        int count=0;  
        for (int i=0;i<=p.length();i++){  
            String f= p.substring(0,i);  
            String s = p.substring(i,p.length());  
            count= count + PermCount(f+ch+s,up.substring(1));  
        }  
    return count;  
    }  
  
}
```

## Maze problems

```java
public class Backtracking {  
    public static void main(String[] args) {  
//        System.out.println(Countway(3,3));  
//        PrintWays("",3,3);  
//        MoveInDiagonal("",3,0,3);  
        boolean[][] board ={  
                {true,true,true},  
                {true,false,true},  
                {true,true,true}};  
            MoveWithRes("",board,0,0);  
    }  
  
    private static int Countway(int r, int c) {  
        if (r==1 || c==1) {  
            return 1;  
        }  
        int left = Countway(r-1,c);  
        int right = Countway(r,c-1);  
        return left+right;  
    }  
    static void PrintWays(String p,int r, int c) {  
        if (r==1 && c==1) {  
            System.out.println(p);  
            return;  
        }  
        if (r > 1) {  
            PrintWays(p+"R", r - 1, c);  
        }  
        if (c > 1 ){  
            PrintWays(p+"D",r,c-1);  
        }  
    }  
    static void MoveInDiagonal(String p,int r,int d, int c) {  
        if (r == 1 && c == 1) {  
            System.out.println(p);  
            return;  
        }  
        if (r > 1 && c > 1) {  
            MoveInDiagonal(p + "Di", r-1, d , c-1);  
        }  
        if (r > 1) {  
            MoveInDiagonal(p + "Row", r - 1, d, c);  
        }  
        if (c > 1) {  
            MoveInDiagonal(p + "Down", r, d,c - 1);  
        }  
    }  
    static void MoveWithRes(String p,boolean[][]maze,int r, int c) {  
        if (r == maze.length-1 && c == maze[0].length-1) {  
            System.out.println(p);  
            return;  
        }  
        if (!maze[r][c]){  
            return;  
        }  
  
  
        if (r < maze.length-1) {  
            MoveWithRes(p + "rigo",maze, r + 1, c);  
        }  
        if (c < maze[0].length-1) {  
            MoveWithRes(p + "Dogo", maze,r, c +1);  
        }  
    }  
}
```