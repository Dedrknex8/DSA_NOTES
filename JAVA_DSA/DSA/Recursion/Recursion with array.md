# Check if a array is sorted or not

```java
public class car {

  

    public static void main(String[] args) {

        int[] arr = {1,2,3,8,5};

        System.out.println(sorted(arr, 0));

    }

  

    static boolean sorted(int[]arr,int idx){

        if (idx==arr.length-1) {

            return true;

        }

        return arr[idx]<arr[idx+1] && sorted(arr, idx+1);

    }

}
```

## LinearSearch Using recursion

```java
public class car {

  

    public static void main(String[] args) {

        int[] arr = {5,4,3,2,1};

        System.out.println(LinerSearch(arr, 0, 41));

        System.out.println(FindIdx(arr, 2, 0));

    }

  

    static boolean LinerSearch(int[]arr,int idx,int target){

        if (idx == arr.length) {

            return false;

        }

        return arr[idx]==target || LinerSearch(arr, idx+1, target);

    }

    static int FindIdx(int[] arr,int target,int idx){

        if (idx==arr.length) {

            return -1;

        }

        if (arr[idx]==target) {

            return idx;

        }else{

        return FindIdx(arr, target,idx+1);

        }

    }

}
```

## Finding all idx using Array List

```java
import java.util.ArrayList;

  

public class car {

  

    public static void main(String[] args) {

        int [] arr={2,4,5,5,8,8,6};

        FindAllIdx(arr, 6, 0);

        System.out.println(List);

    }

    static ArrayList<Integer> List = new ArrayList<>();

    static int FindAllIdx(int[] arr,int target,int idx){

        if (idx == arr.length) {

            return -1;

        }

        if (arr[idx]==target) {

            List.add(idx);

        }

        return FindAllIdx(arr, target, idx+1);

    }

}
```

# Print pattern

```java
public class Pattern {  
    public static void main(String[] args) {  
        triangle(4, 0);  
    }  
  
    static void triangle(int n, int c) {  
        if (n == 0) {  
            return;  
        }  
        if (c < n) {  
            System.out.print("*");  
            triangle(n, c + 1);  
        } else {  
            System.out.println();  
            triangle(n - 1, 0);  
        }  
    }  
}
```

# Bubble sort and selection sort

>Bubble

```java
import java.util.Arrays;  
  
public class Bubble {  
    public static void main(String[] args) {  
        int[] arr = {4, 3, 2, 1};  
        bubbleSort(arr, arr.length - 1, 0);  
        System.out.println(Arrays.toString(arr));  
    }  
  
  
    static void bubbleSort(int[] arr, int r, int c) {  
        if (r == 0) {  
            return;  
        }  
        if (c < r) {  
            //swap  
            if (arr[c] > arr[c + 1]) {  
                int temp = arr[c];  
                arr[c] = arr[c + 1];  
                arr[c + 1] = temp;  
            }  
            bubbleSort(arr, r, c + 1);  
        } else {  
            bubbleSort(arr, r - 1, 0);  
        }  
    }  
}
```

# Selection sort

```java
import java.util.Arrays;  
public class selection{  
        public static void main(String[] args) {  
            int[] arr = {4, 3, 2, 1};  
            Selctionsort(arr, arr.length, 0,0);  
            System.out.println(Arrays.toString(arr));  
        }  
  
  
        static void Selctionsort(int[] arr, int r, int c,int max) {  
            if (r == 0) {  
                return;  
            }  
            if (c < r) { // got the max element  
                if (arr[c] > arr[max]) {  
                    Selctionsort(arr, r, c+1,c);  
                }else{  
                    Selctionsort(arr,r,c+1,max);  
                }  
            }  
            else {  
                int temp=arr[max];  
                arr[max]=arr[r-1];  
                arr[r-1]=temp;  
                Selctionsort(arr, r-1,0,0); //r basically means pass or iteration  
            }  
  
        }  
    }
```

## Merge sort using Recusrion

```java
import java.util.Arrays;  
  
public class MergeSort {  
    public static void main(String[] args) {  
        int[] arr = {8,3,4,12,5,6};  
        arr = Merge(arr); // the stored arry is assinged back  
        System.out.println(Arrays.toString(arr));  
    }  
    static int[] Merge(int[] array){  
        if (array.length == 1){  
            return array;  
        }  
        int mid = array.length/2;  
        int[] leftarr=Merge(Arrays.copyOfRange(array,0,mid)); //this will copy original array upto range in new arr  
        int[] rightarr=Merge(Arrays.copyOfRange(array,mid, array.length));  
  
        return Conq(leftarr,rightarr);  
    }  
  
    private static int[] Conq(int[] first, int[] second){  
        int[] mix= new int[first.length+second.length];  
        int i =0;  
        int j=0;  
        int k=0;  
  
        //check between left and right array and merge  
  
        while(i<first.length && j<second.length){  
        if (first[i] < second[j]){  
            mix[k]=first[i];  
            i++;  
        }else {  
            mix[k] = second[j];  
            j++;  
        }  
        k++;  
        }  
  
        //what if and array pointer finishes first then second aarray then coppy  
        while (i < first.length){  
            mix[k] = first[i];  
            i++;  
            k++;  
        }  
  
        while (j < second.length){  
            mix[k] = second[j];  
            j++;  
            k++;  
        }  
  
        return mix;  
    }  
}
```

## Merge sorrt in place

```java
import java.util.Arrays;  
  
public class MergeSort {  
    public static void main(String[] args) {    
        MergeInplace(arr,0, arr.length);  
        System.out.println(Arrays.toString(arr));  
    }  
  
  
    static void MergeInplace(int[] array,int s,int e){  
        if (e-s <= 1){  
            return;  
        }  
        int mid = (s+e)/2;  
        MergeInplace(array,s,mid); //this will copy original array upto range in new arr  
        MergeInplace(array,mid,e);  
  
        MergeSortInplace(array,s,mid,e);  
    }  
  
    private static void MergeSortInplace(int[]array,int s,int mid,int e){  
        int[] mix= new int[e - s];  
        int i =s;  
        int j=mid;  
        int k=0;  
  
        //check between left and right array and merge  
  
        while(i<mid && j<e){  
            if (array[i] < array[j]){  
                mix[k]=array[i];  
                i++;  
            }else {  
                mix[k] = array[j];  
                j++;  
            }  
            k++;  
        }  
  
        //what if and array pointer finishes first then second aarray then coppy  
        while (i < mid){  
            mix[k] = array[i];  
            i++;  
            k++;  
        }  
  
        while (j < e){  
            mix[k] = array[j];  
            j++;  
            k++;  
        }  
  
        for (int l=0;l<mix.length;l++){  
            array[s+l] = mix[l];  
        }  
    }  
}
```

## Quick sort

```java
import java.util.Arrays;  
  
public class Quick {  
    public static void main(String[] args) {  
        int arr[]={5,4,3,2,1};  
        Quicksort(arr,0,arr.length-1);  
        System.out.println(Arrays.toString(arr));  
    }  
  
    static void Quicksort(int[] arr, int low, int hi) {  
        if(low > hi){ //if array conatin ine elelemt  
            return;  
        }  
        int s=low;  
        int e=hi;  
        int m = s+(e-s)/2;  
  
        int pivot = arr[m];  
  
        while (s <= e){  
            //when s > p < e sort  
            while (arr[s] < pivot){  
                s++;  
            }  
            while (arr[e] > pivot) {  
                e--;  
            }  
  
            //swap  
            if (s <=e){  
                int temp=arr[s];  
                arr[s]=arr[e];  
                arr[e]=temp;  
                s++;  
                e--;  
            }  
        }  
        // when my element s will less then e  
        Quicksort(arr,low,e);  
        Quicksort(arr,s,hi);  
  
    }  
}
```
