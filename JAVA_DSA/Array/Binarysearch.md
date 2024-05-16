
Best case 0(1)
worst case log(n)


# BinarySearch

```java
import java.util.Scanner;

public class car {

    public static int binarsearch(int[] array, int value){
            int low = 0;
            int high  = array.length-1;
            
            while(low<=high){
               int mid = low  + (high-low)/2;

                if(value==array[mid]){
                    System.out.println("eleemt found at "+ mid);
                    return  mid;
                }
                else if(array[mid]<value){
                    low = mid+1;
                }
                else { 
                    high = mid-1;
                }
            }
            System.out.println(value+"can notbe found");
            return -1;
           
            
    }


    public static void main(String[] args) {
        
        int[] array = {1,2,3,4,5,6,7};
        Scanner scan = new Scanner(System.in);
        System.out.println("enter your value u want to search for");
        int value = scan.nextInt();

        int key = binarsearch(array, value);
        
        scan.close();
    }
}



```
# ORDER Agnostic way

```java

public class car {

  

    public static void main(String[] args) {

        int[] array = {9,8,7,6,5,4,3,1};

        int ans = orderAgnostic(array, 7);

  

        System.out.println("Array found at "+ans);

    }

  

    static int orderAgnostic(int[]array,int target){

        int start = 0;

        int end = array.length-1;

  
  

        //check out if array is ascending or descending

        boolean isAsce;

        if (array[start] < array[end]) {

            isAsce= true;

        }

        else{

            isAsce = false;

        }

  

        while (start <= end) {

        int mid = start + (end -start)/2;

        if (array[mid]==target) {

            return mid;

        }

  

        if (isAsce) { //if asceding

        if (target < array[mid]) {

                end = mid-1;

        }

        else{

            start = mid+1;    

        }

        }else{

        if (target > array[mid]) { // if not ascending

            end = mid-1; // then end mid -1 and start mid +1

        }else{

            start=mid+1;

        }

        }

        }        

        return -1;

    }

}
```

# Ceiling of number
```java
public class car {


    public static int binarsearch(int[] array, int value){

            int low = 0;

            int high  = array.length-1;

            int mid = low  + (high-low)/2;

  

            while(low<=high){

               int mid = low  + (high-low)/2;

  

                if(value==array[mid]){

                    return  mid;

                }

                else if(array[mid]<value){

                    low = mid+1;

                }

                else {

                    high = mid-1;

                }

            }

            return low; // return low which become end < start after loop break

    }

  
    public static void main(String[] args) {

        int[] array = {1,2,3,4,5,7};

  

        int key = binarsearch(array, 6);

        System.out.println(key);

    }

}
```

# celling updated

>when we will not find the target instead of returning -1 will return array[0] index
>here to do that will do  array[low % array/length]

```java
import java.util.Scanner;

public class car {

    public static int binarsearch(int[] array, int value){

            int low = 0;

            int high  = array.length-1;

            while(low<=high){

               int mid = low  + (high-low)/2;


                if(array[mid]<value){

                    low = mid+1;

                }

                else {

                    high = mid-1;

                }

            }

            return array[low % array.length]; // return low which become end < start after loop break

    }

  
public static void main(String[] args) {

        int[] array = {1,2,3,4,5,7};

  

        int key = binarsearch(array, 8);

        System.out.println(key);

    }

}
```


# Find occurence using BinarySearch
```java
public class car {

    public static int[] searchRange(int[] nums, int target) {

        int[] ans = {-1, -1};

        ans[0] = isCheked(nums, target, true);

        ans[1] = isCheked(nums, target, false);

        return ans;

    }

  

    public static int isCheked(int[] nums, int target, boolean isSearched) {

        int ans = -1;

        int low = 0;

        int high = nums.length - 1;

  

        while (low <= high) {

            int mid = low + (high - low) / 2;

  

            if (nums[mid] > target) { // here target is smaller than mid

                high = mid - 1;

            } else if (nums[mid] < target) {

                low = mid + 1;

            } else {

                ans = mid;

                if (isSearched) {

                    high = mid - 1;

                } else {

                    low = mid + 1;

                }

            }

        }

        return ans;

    }

  

    public static void main(String[] args) {

  

        int[] nums = {5, 7, 7, 8, 8, 10};

  

        int[] key = searchRange(nums, 8);

        System.out.println("First occurrence: " + key[0]);

        System.out.println("Last occurrence: " + key[1]);

    }

}
```

# Find smallest num than greatest
```java
public class Solution {

  

    public static char nextGreatestLetter(char[] letters, char target){

            int low = 0;

            int high  = letters.length-1;

  

            while(low<=high){

               int mid = low  + (high-low)/2;

  

                if(letters[mid]<target){

                    high = mid-1;

                }

                else {

                    low = mid+1;

                }

            }

            return letters[low % letters.length];

    }

}
```