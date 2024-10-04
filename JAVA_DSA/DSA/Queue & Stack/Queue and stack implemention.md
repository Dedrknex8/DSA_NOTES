
## Implemented queue using stack

```java
import java.util.Stack;  
  
public class QueueUsingStack {  
    public static void main(String[] args) {  
        Stack<Integer> stack = new Stack<>();  
        stack.push(1);  
        stack.push(2);  
        stack.push(3);  
        stack.push(4);  
        System.out.println(stack.peek());  
    }  
    class queues {  
        private Stack<Integer> first;  
        private Stack<Integer> second;  
  
        //call the consstructor  
        public queues(){  
            first = new Stack<>();  
            second = new Stack<>();  
        }  
        public void push(int x){  
            first.push(x);  
        }  
        public int pop(){  
            while (!first.isEmpty()){  
                second.push(first.pop());  
            }  
            int removed = second.pop();  
  
            while (!second.isEmpty()){  
                first.push(second.pop());  
            }  
            return removed;  
        }  
        public int peek(){  
            while (!first.isEmpty()){  
                second.push(first.pop());  
            }  
            int removed = second.peek();  
  
            while (!second.isEmpty()){  
                first.push(second.pop());  
            }  
            return removed;  
        }  
    }  
}
```

## Now some improvement over previous code 
>Added removed efficient code


```java
import java.util.Stack;  
  
public class Queuesefficient {  
    public static void main(String[] args) {  
        queues queue = new queues();  
        queue.push(1);  
        queue.push(2);  
        queue.push(3);  
        queue.push(4);  
        queue.push(5);  
        System.out.println(queue.remove());  
        System.out.println(queue.remove());  
        System.out.println(queue.remove());  
        System.out.println(queue.remove());  
  
  
    }  
    static class queues {  
        private Stack<Integer> first;  
        private Stack<Integer> second;  
  
        //call the consstructor  
        public  queues(){  
            first = new Stack<>();  
            second = new Stack<>();  
        }  
        public void push(int x){  
            while(!first.isEmpty()){  
                second.push(first.pop());  
            }  
            first.push(x);  
            while(!second.isEmpty()){  
                first.push(second.pop());  
            }  
  
        }  
        public int remove(){  
           return first.pop();  
        }  
        public int peek(){  
            while (!first.isEmpty()){  
                second.push(first.pop());  
            }  
            int peeked = second.peek();  
  
            while (!second.isEmpty()){  
                first.push(second.pop());  
            }  
            return peeked;  
        }  
    }  
}
```

## Find max of num [google q's]

```java
import java.util.Arrays;  
import java.util.Scanner;  
  
public class Queuemaxnum {  
    public class TwoStacks{  
        static int twostacks(int x,int[]a,int[]b){  
            return twostacks(x,a,b,0,0)-1;  
        }  
        private static int twostacks(int x,int[]a,int[]b,int sum,int count){  
            if(sum>x){  
                return count;  
            }  
  
            //base case if both arrays are blank  
  
            if(a.length==0 || b.length==0){  
                return count;  
            }  
  
            int ans1=twostacks(x, Arrays.copyOfRange(a,1,a.length),b,sum+a[0],count+1);  
            int ans2=twostacks(x, a,Arrays.copyOfRange(b,1,b.length),sum+b[0],count+1);  
  
            return Math.max(ans1,ans2);  
        }  
    }  
    public static void main(String[] args) {  
        Scanner s = new Scanner(System.in);  
  
        int t = s.nextInt();  
        for (int i = 0; i < t; i++) {  
            int n = s.nextInt();  
            int m = s.nextInt();  
            int x = s.nextInt();  
            int[] a = new int[n];  
            int[] b = new int[m];  
  
            for (int j = 0; j < n; j++) {  
                a[j] = s.nextInt();  
            }  
            for (int j = 0; j < m; j++) {  
                b[j] = s.nextInt();  
            }  
  
            System.out.println(TwoStacks.twostacks(x,a,b));  
        }  
    }  
}
```


# Find largest area of a histogram

```java
class Solution {

    public static int largestRectangleArea(int[] heights) {

        int ns[] = findnextSmaller(heights);

        int ps[] = findpreviousSmaller(heights);

  

        int max = Integer.MIN_VALUE;

        for (int i = 0; i < heights.length; i++) {

            int h  = heights[i]; // hight will be idx value

  

            int w = ns[i] -  ps[i] - 1; //this will get the width

  

            max = Math.max(max, (h*w));

        }

        return max;

  

    }

    public static int[] findnextSmaller(int[] arr){

        int n = arr.length;

        Stack<Integer> stack = new Stack<Integer>();

  

        int result[] = new int[n];

        for(int i=n-1; i>=0; i--){ // i here is idx

            while(!stack.isEmpty() && arr[stack.peek()] >= arr[i]){

                stack.pop();

            }

  

            if(stack.isEmpty()){

                result[i] = n;

  

            }

            else {

                result[i] = stack.peek();

            }

            stack.push(i);

        }

        return result;

    }

    public static int[] findpreviousSmaller(int[] arr){

        int n = arr.length;

        Stack<Integer> stack = new Stack<Integer>();

  

        int result[] = new int[n];

        for(int i=0; i<n; i++){ // i here is idx

            while(!stack.isEmpty() && arr[stack.peek()] >= arr[i]){

                stack.pop();

            }

  

            if(stack.isEmpty()){

                result[i] = -1; // this will make the ps as -1

  

            }

            else {

                result[i] = stack.peek();

            }

            stack.push(i);

        }

        return result;

    }

}
```

## More optimized way of histogram

```java
class Solution {

   public static int largestRectangleArea(int[] heights) {

       Stack<Integer> stack = new Stack<>();

        int n = heights.length;

  

        int max=Integer.MIN_VALUE;

        for(int i=0;i<=n;i++){

            int elements = (i==n)?0:heights[i]; //this will check if elemt is last than 0 will be added a top

            while (!stack.isEmpty() && heights[stack.peek()]>elements) {

                int h = heights[stack.pop()];

                int ps = stack.isEmpty() ? -1 : stack.peek();

                int w = i - ps - 1;

                max = Math.max(max, w * h);

            }

            stack.push(i);

        }

        return (max==Integer.MIN_VALUE?0:max);

   }

}
```

## Minum no of valid string to make complete Faang medium

```java
class Solution {

    public int minAddToMakeValid(String s) {

        Stack<Character> stack = new Stack<>();

  

        for(char ch : s.toCharArray()){

            if(ch==')'){

                if(!stack.isEmpty() && stack.peek()=='('){

                    stack.pop();

                }else{

                    stack.push(ch);

                }

            }else{

                stack.push(ch);

            }

        }

        return stack.size();

    }

}
```