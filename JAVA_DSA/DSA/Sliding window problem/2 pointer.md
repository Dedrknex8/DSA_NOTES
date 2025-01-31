
# Finding maxSum using two pointer

```java
public class Main {  
    public static void main(String[] args) {  
        int[] Array = {-1,2,3,3,4,5,-1};  
        int target =2;  
        int left=0;  
        int right = target-1;  
        int result = findmaxSum(left, right,Array,target);  
        System.out.println(result);  
    }  
    static int findmaxSum(int left, int right,int[]array,int target) {  
        //finding sum  
        int sum=0;  
        for (int i = 0; i < target ; i++) {  
            sum  += array[i];  
        }  
        int maxSum = 0;  
        while(right < array.length-1){  
            sum = sum - array[left];  
            left++;  
            right++;  
            sum = sum + array[right];  
            maxSum = Math.max(maxSum,sum);  
        }  
  
            return maxSum;  
    }  
}
```