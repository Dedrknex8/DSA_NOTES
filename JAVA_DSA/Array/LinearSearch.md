
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

