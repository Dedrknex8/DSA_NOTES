
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

# Infinite Array

```java
public class car{

    public static void main(String[] args) {

        int[] nums={3, 5, 7, 9, 10, 90,

            100, 130, 140, 160, 170};//whatevr the array is:

        System.out.print(ans(nums, 10));

        //formula to double the size of array = end  - (end - start +1 ) * 2

    }

    static int ans(int[]nums,int target){

        int start = 0;

        int end = 1;

  

        // condition for the target to lie in the range

        while (target > nums[end]) {

            int temp = end + 1; // this is my new start

            // double the box value

            // end = previous end + sizeofbox*2

            end = end + (end - start + 1) * 2;

            start = temp;

        }

        return binarySeach(nums,target,start,end);

    }

    static int binarySeach(int[] nums, int target, int start, int end) {

        while (start <= end) {

            int mid = start +(end-start)/2;

  

            //check if left or right

  

            if (target < nums[mid]) {

                end=mid-1;

  

            }else if (target > nums[mid]) {

                start = mid + 1;

            }else{

            return mid; //ans found

            }

        }

  

        return -1;

    }

}
```


>Summary in this we have to assume that the last index is at infinite or the size of array is infinity
>that mean we cannot use array.length here because we don't know the size  of array

# Mountain Peek

```java
//https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/1264965034/

//https://leetcode.com/problems/find-peak-element/submissions/1264976513/

public class car{

    public static void main(String[] args) {

        int[] nums={0,10,5,2};//whatevr the array is:
       int res = mountainArray(nums);
       System.out.println(res);
    }

    private static int mountainArray(int[]nums) {

        int start = 0;

        int end  = nums.length-1;

        while (start < end) {

            int mid  =  start + (end - start) /2;

            if (nums[mid] > nums[mid + 1]) { // ans lie in left asc

                end = mid; // why this

            }

            else{ // u're in right side desce

                start=mid+1;

            }

        }

        return start;

    }

}
```

# IMP find in mountain array

```java
//https://leetcode.com/problems/find-in-mountain-array/description/

public class car {

  

    public static void main(String[] args) {

        int[] array = {1,2,3,4,5,3,1}; //  3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

        System.out.println(search(array, 6));

    }

    static int search(int []array,int target){

        int peak = findMounntainarray(array);

        int firstTry =  orderAgnostic(array,target,0,peak);

        if (firstTry != -1) {

            return firstTry;

        }else{

            return orderAgnostic(array, target, peak+1, array.length-1);

        }

    }

  

    static int findMounntainarray(int[]array){ // find in mountain peek

        int  start = 0;

        int end = array.length-1;

  

        while (start < end) {

  

            int mid = start + (end - start) / 2;

            if (array[mid] >  array[mid+1]) {

  

                end = mid;

            }else{

                start = mid + 1;

            }

        }

        return end;

    }

    static int orderAgnostic(int[] array, int target, int start, int end) {

        boolean isAsc = array[start] < array[end];

        while (start <= end) {

            int mid = start + (end - start) / 2;

            if (array[mid] == target) {

                return mid; // Found the target element

            }

            if (isAsc) { // If it's ascending

                if (target < array[mid]) {

                    end = mid - 1;

                } else {

                    start = mid + 1;

                }

            } else { // If it's descending

                if (target > array[mid]) {

                    end = mid - 1;

                } else {

                    start = mid + 1;

                }

            }

        }

        return -1; // Target element not found

    }

}
```


# Rotated array BinarySearch

>Rotated binary search is a variation of the binary search algorithm that works on a rotated sorted array. In a rotated sorted array, an array is sorted in ascending order and then rotated at some pivot index. For example, the array `[4, 5, 6, 7, 0, 1, 2]` is a rotated version of `[0, 1, 2, 4, 5, 6, 7]` at pivot index 3 i.e element "7".

`How to Solve`

>`case1` : we know here pivot happen after the highest number element as in example it was 7.
>'mid < mid +1' here mid+1 will be the ans

>`case2`: mid > mid +1 then then mid will be ans

>`case3`: start > mid => the after mid all will be in desc order and mid -1 upto start will be asc order
>eg : `[6,4,5,3,2,1,0]` as here start = 6 and mid = 3 then left to 3 is in des order & right to 3 is asc order then `igonre the upto end = mid - 1 as 5 is greatest element` 

>`case4: start < mid` `[2,3,4,5,6,2,1,3]` then igone alement left to mid so start = mid + 1 upto end which length of array - 1 

```java
public class car {

  

    public static void main(String[] args) {

        int[] arr = {4,5,6,7,0,1,2};

        System.out.println(findpivot(arr));

    }

  

    static int findpivot(int [] arr){

        int start = 0;

        int end = arr.length-1;

        //4 cases

        while (start <=  end) {

            int mid = start + (end - start)/ 2;

        //case 1

        if (mid<end && arr[mid]>arr[mid+1]) {

            return mid;

        }

        if (mid > start &&arr[mid]<arr[mid- 1 ]) { // case 2

            return mid-1;

        }

        if (arr[mid] <= arr[start]) {

            end = mid-1;

        }else{

            start = mid+1;

        }

        }

        return -1;

    }

}
```

## okay now find the solution for leetcode 

>  The question that is given in leetcode is to find a target 
>  

>`case2` : if return - 1 that mens it not roated search simple binary search 
   `case1` : if target == pivot then return pivot ans
>`case2` if target > start , then ans lie in pivot - 1 the also check for outbound error
>`case3` if target < start then pivot +1 will be ans

solved  solution:

```java
//https://leetcode.com/problems/search-in-rotated-sorted-array/
static int search(int[]nums,int target){

        int pivot = findpivot(nums);

        if (pivot == -1) {

            return binarysearch(nums, target, 0, nums.length - 1);

        }

        if (target == nums[pivot]) { //case 1

            return pivot;

        }

        //case 2

        if (target >= nums[0] ) {

            return binarysearch(nums, target, 0, pivot-1);

        }

        return binarysearch(nums, target, pivot+1, nums.length-1);

    }

    static int binarysearch(int[]nums,int target,int start,int end){

        while (start <= end) {

            int mid = start + (end - start)/ 2;

            if (target < nums[mid]) {

                end = mid - 1;

            }else if(target > nums[mid]){

                start = mid+1;

            }else{

                return mid; //ans found

            }

            }

            return -1;

    }

    static int findpivot(int [] nums){

        int start = 0;

        int end = nums.length-1;

        //4 cases

        while (start <=  end) {

            int mid = start + (end - start)/ 2;

        //case 1

        if (mid<end && nums[mid]>nums[mid+1]) {

            return mid;

        }

        if (mid > start &&nums[mid]<nums[mid- 1 ]) { // case 2

            return mid-1;

        }

        if (nums[mid] <= nums[start]) { //case 3

            end = mid-1;

        }else{ //case 4

            start = mid+1;

        }

        }

        return -1;

    }

```

## Remove duplicay in roation

```java
public class car {

  

    public static void main(String[] args) {

        int[] nums = {2,5,6,0,0,1,2};

        System.out.println(search(nums, 0));

    }

    static int  search(int[]nums,int target){

        int pivot = findpivot(nums);

        if (pivot == -1) {

            return binarysearch(nums, target, 0, nums.length - 1);

        }

        if (target == nums[pivot]) { //case 1

            return pivot;

        }

        //case 2

        if (target >= nums[0] ) {

            return binarysearch(nums, target, 0, pivot-1);

        }

        return binarysearch(nums, target, pivot+1, nums.length-1);

    }

    static int binarysearch(int[]nums,int target,int start,int end){

        while (start <= end) {

            int mid = start + (end - start)/ 2;

            if (target < nums[mid]) {

                end = mid - 1;

            }else if(target > nums[mid]){

                start = mid+1;

            }else{

                return mid; //ans found

            }

            }

            return -1;

    }

    static int findpivot(int [] nums){

        int start = 0;

        int end = nums.length-1;

        //4 cases

        while (start <=  end) {

            int mid = start + (end - start)/ 2;

        //case 1

        if (mid<end && nums[mid]>nums[mid+1]) {

            return mid;

        }

        if (mid > start &&nums[mid]<nums[mid- 1 ]) { // case 2

            return mid-1;

        }

       //what is start , mid , end are equal then

       if (nums[start]==nums[mid]) {

        if (start > start+1) { // this will check if skip is pivot

            return start;

        }else{

        start++;

        }

        if (nums[end] > nums[end -1]) { // willl check if skip is pivot

            return end;

        }

        end--;

    }

    //if start  < mid that means lie in right side then pivot right

    else if(nums[start] <= nums[mid] || (nums[start]==nums[mid] && nums[mid]> nums[end]) ) {

         start+=mid;

       }else{

        end = end -1;

       }

    }

        return -1;

    }

}
```

## Roation with boolean and outbound solved
```java
//https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

public class car {

  

    public static void main(String[] args) {

        int[] nums = {1,0,1,1,1};

        System.out.println(search(nums, 0));

    }

    static boolean  search(int[]nums,int target){

        int pivot = findpivot(nums);

        if (pivot == -1) {

            return binarysearch(nums, target, 0, nums.length - 1);

        }

        if (target == nums[pivot]) { //case 1

            return true;

        }

        //case 2

        if (target >= nums[0] ) {

            return binarysearch(nums, target, 0, pivot-1);

        }

        return binarysearch(nums, target, pivot+1, nums.length-1);

    }

    static boolean binarysearch(int[]nums,int target,int start,int end){

        while (start <= end) {

            int mid = start + (end - start)/ 2;

            if (target < nums[mid]) {

                end = mid - 1;

            }else if(target > nums[mid]){

                start = mid+1;

            }else{

                return true; //ans found

            }

            }

            return false;

    }

    static int findpivot(int[] nums) {

        int start = 0;

        int end = nums.length - 1;

        while (start < end) {

            int mid = start + (end - start) / 2;

            if (mid < end && nums[mid] > nums[mid + 1]) {

                return mid;

            }

            if (mid > start && nums[mid] < nums[mid - 1]) {

                return mid - 1;

            }

            if (nums[start] == nums[mid] && nums[mid] == nums[end]) {

                // If start, mid, and end are all equal, we need to search both sides

                if (nums[start] > nums[start + 1]) {

                    return start;

                }

                start++;

                if (nums[end] < nums[end - 1]) {

                    return end - 1; // beacuse desc order

                }

                end--;

            } else if (nums[start] <= nums[mid]) {

                start = mid + 1;

            } else {

                end = mid - 1;

            }

        }

        return start; // If pivot not found, return start

}

}
```

# find number of roation

```java

public class car {
    public static void main(String[] args) {

        int[] nums = {1,0,1,1,1};

        System.out.println(search(nums, 0));

    }
    static int countroation(int[]nums){
	    int pivot = findpivot(nums);
	    return pivot+1;
    }
    static int findpivot(int[] nums) {

        int start = 0;

        int end = nums.length - 1;

        while (start < end) {

            int mid = start + (end - start) / 2;

            if (mid < end && nums[mid] > nums[mid + 1]) {

                return mid;

            }

            if (mid > start && nums[mid] < nums[mid - 1]) {

                return mid - 1;

            }

            if (nums[start] == nums[mid] && nums[mid] == nums[end]) {

                // If start, mid, and end are all equal, we need to search both sides

                if (nums[start] > nums[start + 1]) {

                    return start;

                }

                start++;

                if (nums[end] < nums[end - 1]) {

                    return end - 1;

                }

                end--;

            } else if (nums[start] <= nums[mid]) {

                start = mid + 1;

            } else {

                end = mid - 1;

            }

        }

        return start; // If pivot not found, return start

}
```

# Split array

```
public class car {

     public static void main(String[] args) {

        int[] nums = {7,2,5,10,8};

        System.out.println(splitArray(nums,2));

    }

    static int splitArray(int[]nums,int m){

        int start = 0;

        int end = 0;

  

        for(int i=0;i<nums.length;i++){

            start = Math.max(start, nums[i]); // it will change the start and end

            end+=nums[i];

        }

        //calcaulte how many pieces

        while (start < end) {

        //think mid as potential ans

        int mid = start + (end - start) / 2; //will get mid

        int sum=0;

        int pieces=1; // piece 1 beacuse it has 1 array alreaday

        for(int num:nums){

            if (num+sum> mid) {

                //you can't add more create new subarray sum=num which in case = 32

            sum=num;

            pieces++; // p = 2

            }else{

                sum +=num;

            }

        }

        if (pieces > m) {

            start = mid+1;

        }else{

            end=mid;

        }

    }

    return end;

}

}
```
## insertion if not found

> `arr[0,1,3,4,5]` want to add 2 what will we do
> `case:1` if target  <= mid then target = mid -1
> `case 2:` target mid +1 