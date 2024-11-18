```java
import java.util.Arrays;  
  
public class Radix {  
    //UTITLITY TO GET MAX VALUE IN ARRAY  
    static int getMax(int nums[],int exp){  
        int max = 0;  
        for(int i = 0;i < nums.length;i++){  
            if(nums[i]>max){  
                max = nums[i];  
            }  
        }  
        return  max;  
    }  
  
    static void countSort(int nums[],int n,int exp){  
        int[] output = new int[n];  
        int i;  
        int count[] = new int[10];  
        Arrays.fill(count,0);  
  
        //THIS WILL STORE THE OCCURENCE OF ELEMENT IN COUNT  
        for(i = 0;i < n;i++) {  
            count[(nums[i] / exp) % 10]++;  
        }  
            //CHANGE THE COUNT[I] SO THAT  
            //IT CONTAINS ACTUAL POS IN DIGIT OUTPUT            //GIVES CUMMALITVE FREQ            for (i = 1; i <10 ; i++) {  
                count[i] += count[i - 1];  
            }  
            //BUILD THE OUTPUT ARRAY  
            for (i=n-1;i>=0;i--) {  
                output[count[(nums[i]/exp)%10] - 1] = nums[i];  
                count[(nums[i]/exp)%10] --;  
            }  
  
            //copy the ouput array to nums[] so that  
            //it contains the sorted array        for ( i = 0; i < n; i++) {  
            nums[i] = output[i];  
        }  
    }  
  
    static void radixsort(int[]nums,int n){  
        int m = getMax(nums,n);  
  
        for (int exp = 1; m / exp > 0; exp *= 10) {  
            countSort(nums, n, exp);  
        }  
    }  
    static void print(int nums[], int n)  
    {  
        for (int i = 0; i < n; i++) {  
            System.out.print(nums[i] + " ");  
        }  
    }  
  
    public static void main(String[] args) {  
        int nums[] = { 170, 45, 75, 90, 802, 24, 2, 66 };  
        int n = nums.length;  
        radixsort(nums,n);  
        print(nums,n);  
    }  
}
```