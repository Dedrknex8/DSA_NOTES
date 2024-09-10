
```<>
import java.util.Arrays;

  

public class car {

  

    public static void main(String[] args) {

        int[] nums  = {10,4,8,1,3,5,9};

        // System.out.println(nums.length[]);

        selectionSort(nums);

        System.out.println(Arrays.toString(nums));

    }

    static void selectionSort(int[] nums){

        for(int i=0;i<nums.length;i++){

            int end = nums.length-i-1;

            int maxItem = getMax(nums,0,end);

            swap(nums, maxItem, end);

        }

    }

    //find the max element

    static int getMax(int[]nums,int start,int end){

        int max = start;

  

        for(int i=start; i<=end; i++){

            if (nums[max] < nums[i]) {

                max = i;

            }

        }

        return max;

    }

  

    static void swap(int[]nums,int first, int second){

            int temp = nums[first];

            nums[first] = nums[second];

            nums[second]= temp;

        }

  

    static void bubbleSort(int[] nums){

         boolean swapped; // this will check in first iteration if alrady sorted

        for(int i=0; i < nums.length; i++){

            swapped=false; // here sorted initially false

            for(int j=1; j< nums.length-i-1;j++){

                if (nums[j-1]>nums[j]) {

                    int temp = nums[j];

                    nums[j]=nums[j-1];

                    nums[j-1]=temp;

                    swapped=true; // if swapped made it will  change swap to true

                }

            }

            // if  element found to be sorted already

            if (!swapped) {

                break; // break the loop ch

             }

        }

    }

}
```

# Insertion sort

```<>
import java.util.Arrays;

  

public class car {

  

    public static void main(String[] args) {

        int[] nums  = {10,4,8,1,3,5,9};

        // System.out.println(nums.length[]);

        InseretionSort(nums);

        System.out.println(Arrays.toString(nums));

    }

    static void InseretionSort(int[]nums){

        for(int i=0;i < nums.length-1;i++){

            for(int j=i+1; j > 0; j--){

                if (nums[j] < nums[j-1] ) {

                    //swapping

                    int temp = nums[j];

                    nums[j]=nums[j-1];

                    nums[j-1]=temp;

                }else{

                    break;

                }

            }

        }

    }

}
```

# Find missing numbers

```<>
import java.util.Arrays;

  

public class car {

  
public static void main(String[] args) {

int[] arr = {3,0,1};

  

System.out.println(sort(arr));

}

static int sort(int[] arr){

int i=0;

while (i<arr.length) {

int currentidx = arr[i];

if (arr[i] < arr.length && arr[i] != arr[currentidx]) { // aray[i] <arr.length to skip

swap(arr,i,currentidx);

}else{

i++;

}

}

//search for missing num after sorting

  

for(int idx=0; idx<arr.length; idx++){

if (arr[idx]!=idx) {

return idx;

}

}

return arr.length;

}

private static void swap(int[] arr, int first, int last) {

int temp =  arr[first];

arr[first] = arr[last];

arr[last] = temp;

}

}
```


# Find all missing num

```<>
import java.util.ArrayList;

import java.util.List;

  
public class car {

  

    public static void main(String[] args) {

        int[] arr = {4,3,2,7,8,2,3,1,9,11};

  

        System.out.println(sort(arr));

    }

    static List<Integer> sort(int[] arr){

        int i=0;

        while (i<arr.length) {

            int currentidx = arr[i] - 1;

  

        if (currentidx >= 0 && currentidx < arr.length && arr[i] != arr[currentidx]) {

                swap(arr,i,currentidx);

            }else{

                i++;

            }

        }

        //search for missing num after sorting

        ArrayList<Integer> missingNumber = new ArrayList<>();

        for(int idx=0; idx<arr.length; idx++){

            if (arr[idx]!=idx+1) {

                missingNumber.add(idx+1);

            }

        }

        return missingNumber;

    }

    private static void swap(int[] arr, int first, int last) {

        int temp =  arr[first];

        arr[first] = arr[last];

        arr[last] = temp;

    }

}
```

# Find duplicates in cycleSort

```<>
import java.util.numsayList;

import java.util.List;

public class car {

  

    public static void main(String[] args) {

        int[] nums = {1,3,4,2,2};

  

        System.out.println(Duplicates(nums));

    }

    static int Duplicates(int[]nums){

        int i=0;

        while (i < nums.length) {

            if (nums[i]!=i+1) { // if nums[0] = 1 then 0+1 = 1 check            

            int currentIdx = nums[i] -1; // currentIdx 1-1 = 1 i.e 1 should be a 0 IDX

            if (nums[i] != nums[currentIdx]) {

                swap(nums, i, currentIdx);

            }else{

                return nums[i];

            }

        }else{

            i++;

        }

        }

        return -1;

    }

    static void swap(int[] nums, int first, int last) {

        int temp =  nums[first];

        nums[first] = nums[last];

        nums[last] = temp;

    }

}
```


# Find all duplicates  using linked list

```<>
import java.util.ArrayList;

import java.util.List;

public class car {

    public static void main(String[] args) {

        int[] nums = {4,3,2,7,8,2,3,1};

        System.out.println(Duplicates(nums));

    }

    static List<Integer> Duplicates(int[]nums){

        int i=0;

        while (i < nums.length) {

            int currentIdx = nums[i] -1; // currentIdx 1-1 = 1 i.e 1 should be a 0 IDX

            if (nums[i] != nums[currentIdx]) {

                swap(nums, i, currentIdx);

            }else{

                i++;

                }

        }

        ArrayList<Integer> duplicates = new ArrayList<>();

  

        for(i=0;i<nums.length;i++){

            if (nums[i] !=i+1) {

                duplicates.add(nums[i]);

            }

        }

        return duplicates;

    }

    static void swap(int[] nums, int first, int last) {

        int temp =  nums[first];

        nums[first] = nums[last];

        nums[last] = temp;

    }

}
```

# Find setMismatch

```<>
import java.util.ArrayList;

import java.util.Arrays;

import java.util.List;

  

public class car {

  

    public static void main(String[] args) {

        int[] nums = {1,2,2,4};

        int[] res = Duplicates(nums);  

        System.out.println(Arrays.toString(res));

    }

    static int[] Duplicates(int[]nums){

        int i=1;

        while (i < nums.length) {

            int currentIdx = nums[i] -1; // currentIdx 1-1 = 1 i.e 1 should be a 0 IDX

            if (nums[i] != nums[currentIdx]) {

                swap(nums, i, currentIdx);

            }else{

                i++;

                }

        }

        for(i=0;i<nums.length;i++){

            if (nums[i] != i+1) {

                return new int[]{nums[i],i+1}; // duplicated = i miss = +1

            }

        }

        return new int[]{-1,-1};

    }

    static void swap(int[] nums, int first, int last) {

        int temp =  nums[first];

        nums[first] = nums[last];

        nums[last] = temp;

    }

}
```

# Find Positive missing number 

```<>
class Solution {

    public int firstMissingPositive(int[] nums) {

     int i=0;

        while (i < nums.length) {

            int currentIdx = nums[i]-1;

            if (nums[i]>0 && nums[i] <= nums.length && nums[i] != nums[currentIdx]) {

                swap(nums, i, currentIdx);

            }else{

                i++;

                }

        }

  

        // search for first missing number

         for(int idx=0;idx<nums.length;idx++){

            if (nums[idx] != idx+1) {

                 return idx+1;

            }

        }

        return nums.length+1;

    }

    static void swap(int[] nums, int first, int last) {

        int temp =  nums[first];

        nums[first] = nums[last];

        nums[last] = temp;

    }

}
```

