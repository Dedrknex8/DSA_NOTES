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