
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

# Backtracking of the maze problem in all dir

```java

public class Backtracking {  
    public static void main(String[] args) {  
        boolean[][] board ={  
                {true,true,true},  
                {true,true,true},  
                {true,true,true}};  
            int[][] path = new int[board.length][board[0].length]; //same size as borad  
            MoveWithbacktack("",board,0,0,path,1);
    }
static void MoveWithbacktack(String p,boolean[][]maze,int r, int c,int[][]path,int step) {  
    if (r == maze.length-1 && c == maze[0].length-1) {  
    path[r][c] = step;  
        for (int[] arr : path){  
            System.out.println(Arrays.toString(arr));  
        }  
        System.out.println(p);  
        System.out.println();  
  
        return;  
    }  
  
    if (!maze[r][c]){  
        return;  
    }  
    maze[r][c] = false;  
    path[r][c] = step; //this will add the current step to path  
  
    if (r < maze.length-1) {  
        MoveWithbacktack(p + "D",maze, r + 1, c,path,step+1);  
    }  
    if (c < maze[0].length-1) {  
        MoveWithbacktack(p + "R", maze,r, c +1,path,step+1);  
    }  
    if (r>0){  
        MoveWithbacktack(p+"U",maze,r-1,c,path,step+1);  
    }  
    if (c>0){  
        MoveWithbacktack(p+"L",maze,r,c -1,path,step+1);  
    }  
  
    maze[r][c] = true;  
    path[r][c] = 0;  
}
```

## N queen problem

```java
public class Nqueens {
    public static void main(String[] args) {
        int n = 4;
        boolean[][] board = new boolean[n][n];
        int solution=queens(board, 0);
        System.out.println(solution);
    }

    static int queens(boolean[][] board, int row) {
        if (row == board.length) {
            display(board);
            System.out.println();

            return 1;
        }
        //Now checking if can be place at row and col
        int count = 0;
        for (int col = 0; col < board.length; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = true;
                count += queens(board, row + 1);
                board[row][col] = false;
            }
        }
        return count;
    }


    static boolean isSafe(boolean[][] board, int row, int col) {
        // Check vertical column
        for (int i = 0; i < row; i++) {
            if (board[i][col]) {
                return false;
            }
        }

        // Check left diagonal
        for (int i = 0; i <= row && col - i >= 0; i++) {
            if (board[row - i][col - i]) {
                return false;
            }
        }

        // Check right diagonal
        for (int i = 0; i <= row && col + i < board.length; i++) {
            if (board[row - i][col + i]) {
                return false;
            }
        }

        return true;
    }


    static void display(boolean[][] board) {
        for (boolean[] row : board) {
            for (boolean element : row) {
                if (element) {
                    System.out.print("Q");
                } else {
                    System.out.print("X");
                }
            }
            System.out.println();
        }
    }
}

```

## K night Problem

```java
public class Nknight {  
    public static void main(String[] args) {  
        int n=4;  
        boolean[][] board = new boolean[n][n];  
         Knight(board,0,0,4);  
  
    }  
    static void Knight(boolean[][] board,int row,int col,int knight) {  
        if (knight ==0){  
            display(board);  
            return;  
        }  
        //check if they are out of bound or not  
        if (row == board.length-1 && col == board.length){  
            return;  
        }  
        if (row == board.length && col == 0) {  
            Knight(board,row+1,0,knight+1);  
            return;  
        }  
  
        if (col == board.length) {  
            Knight(board, row + 1, 0, knight);  
            return;  
        }  
        if (isSafe(board,row,col)){  
            board[row][col] = true;  
            Knight(board,row,col+1,knight-1);  
            board[row][col] = false;  
        }  
        Knight(board,row,col+1,knight);  
    }  
    static boolean isSafe(boolean[][] board, int row, int col) {  
        //check for vertical  
  
        if (isvalid(board,row-1,col+2)){  
            if (board[row-1][col+2]){  
                return false;  
            }  
        }  
        if (isvalid(board,row-1,col-2)) {  
            if (board[row-1][col-2]){  
            return false;  
        }  
        }  
        if (isvalid(board,row+2,col-1)){  
            if (board[row+2][col-1]){  
                return false;  
            }  
        }  
        if (isvalid(board,row+2,col+1)){  
            if (board[row+2][col+1]){  
                return false;  
            }  
        }  
        return true;  
    }  
    static boolean isvalid(boolean[][] board, int row, int col) {  
        if (row >= 0 && row < board.length && col >= 0 && col < board.length){  
            return true;  
        }  
        return false;  
    }  
  
        static void display(boolean[][] board){  
        for (boolean[] row : board) {  
            for (boolean element : row) {  
                if (element){  
                    System.out.print("K");  
  
                }  
                else {  
                    System.out.print("X");  
                }  
            }  
            System.out.println();  
        }  
    }  
}
```

> If want to return count create a var a count =0 in body and return count