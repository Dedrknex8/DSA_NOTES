```java
import java.util.Arrays;

public class car {

  

    public static void main(String[] args) {

        int arr[][]={{10,20,30,40},

                    {11,23,33,44},

                    {12,29,34,45}};

  

        System.out.println(Arrays.toString(search(arr,29 )));

    }

    static int[] search(int [][] arr,int target){

        int r=0; // intially r <0

        int c = arr.length-1; // column array end i.e 40

  

        //initialy row=10 and col 40

  

        while (r<arr.length && c >=0) {

            if (arr[r][c] == target) { // if 40 == target

	                return new int[]{r,c};

            }

            if (arr[r][c] < target) { //40 < target r++

                r++;

            }else{

                c--;

            }

        }

        return new int[]{-1,-1};

    }

}
```

