
# LinearSearch is a technique to find a particular value in a array

```java
import java.util.Scanner;

public class car {

    public static int linearsearch(int[] array, int value){
            for(int i=0; i<array.length; i++){
                if(array[i]==value){
                System.out.println("the value find AT "+ i +" From right");
                }
            }
            return -1;
    }

//linear search itreates through every elements
    public static void main(String[] args) {
        
        int[] array = {2,7,9,8,1,6,3};
        Scanner scan = new Scanner(System.in);
        System.out.println("enter your value u want to search for");
        int value = scan.nextInt();

        int key = linearsearch(array, value);
        
        if(key==-1){
            System.out.println("the value not found 
            "+value);
        }
    }
}


```

# Question Time

>Findig the minumum number number in array using linearsearch

```java
import javax.imageio.IIOException;

  public class car {

      public static void main(String[] args) {

        int[] array = {4,5,9,8,-1,18,24};

        //check if array is empty

        if(array==null || array.length==0){

            throw new IllegalArgumentException("Array can't be empty");
        }

        int min = MinmumNuber(array);

        System.out.println("The minimum number is : "+min);

    }
  
    private static int MinmumNuber(int[] array) {

       int min = array[0];

        for(int i=1;i<array.length;i++){

            if(array[i]<min){

                array[i]=min;

            }    

        }

        return min;

    }
}
```

# Search in Two D-Array

```java
import java.util.Arrays;

  

public class car {

  

    public static void main(String[] args) {

        int[][] array = {

            {1,2,3},

            {4,5,6},

            {7,8,9,10} //intialising of 2D array

        };

  

        int target=9;

        int result[] = search(array,target);

  

        System.out.println("Found at "+Arrays.toString(result)); // to string method cahnnge array into human readable code

    }

  

    private static int[] search(int[][] array, int target) {

  

        for(int i=0;i<array.length;i++){

            for(int j=0; j <array[i].length;j++){

                if (array[i][j]==target) {

                    return new int[]{i,j}; // returni row=i & col=j

                }

            }

        }

        return new int[]{-1,-1}; //if not found then return -1

    }

}

```