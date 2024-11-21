### It is an algorithm used for query search as as a range q's like addition of of num from 1 to 6 in array

> It's complexity is 0(sqrt(N))

`Steps`
1. Divide the array into block of size root n
2. Compute ans for every block
3. GIven a query for L to R,combine the box that contain this

Let array  = {1,3,5,2,7,6,1,4,8} , sizeArr=9 (Divide into 3 blocks)

1. newarr = [{1,3,5},{2,7,6},{1,4,8}]
2. Compute : {9,15,8}

```java
import java.util.Arrays;  
  
public class Rangeq {  
  
    public static void main(String[] args) {  
        int[] arr = { 1,3,5,2,7,6,3,1,4,8 };  
  
        int n = arr.length;  
  
        int sqrt = (int) Math.sqrt(n);  
        int block_id = -1;  
  
        //CREATING BLOCKS OF SQRT SIZE  
        int[] blocks = new int[sqrt+1];  
  
        for (int i=0; i<n; i++) {  
           // NEW BLOCK IS STARTING  
            if (i % sqrt == 0) {  
                block_id++;  
            }  
            //ADD THE ELEMENT IN CURRENT BLOCK  
            blocks[block_id] += arr[i];  
        }  
        update(blocks,arr,4,8,sqrt);  
        System.out.println(query(blocks,arr,sqrt,2,7));  
    }  
  
    public static int query(int[] blocks,int[] arr,int sqrt,int l,int r ){  
        int ans =0;  
  
        //LEFT PART  
        while(l%sqrt !=0 && l<r && l!=0){  
            ans += arr[l];  
            l++;  
        }  
  
      //Middle part  
        while(l+sqrt<=r){  
            ans += blocks[l/sqrt];  
            l += sqrt;  
        }  
        while(l<=r){  
            ans += arr[l];  
            l++;  
        }  
  
        return ans;  
    }  
  
    //UPADATE PART  
  
    public static void update(int[]blocks,int[]arr,int i,int val,int sqrt){  
        int block_id = i / sqrt;  
  
        //UPDATE THE OVERALL VAL IN THE BLOCK  
        blocks[block_id] += val - arr[i];  
        arr[i] =val; //UPDATE THE VAL TO THAT IDX  
    }  
  
}
```