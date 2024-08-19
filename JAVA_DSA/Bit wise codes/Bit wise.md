
TO get wheter a num is even or odd in using bit operator

```java
public class car {

  

    static void Even(int n){

     if ( n&1 == 1) {

        System.out.println("The given "+n+"is odd");

     }else{

        System.out.println("GIven num is even"+n);

     }

    }

        public static void main(String[] args) {

        Even(67);

    }

}
```

## To check if a num contain non repesting element

```java
public class car {

  

    static int Even(int[] arry){

     int unq = 0; //initialize with 0

  

     for(int i:arry){

        unq ^=i;

     }

     return  unq;

     }

        public static void main(String[] args) {

        int arr[]={1,2,3,2,3,1,6};

        System.out.println(Even(arr));

    }

}
```

>Explaination
>1. **Initialization**:
    
    - `int unique = 0;` initializes the result to `0`.
2. **XOR Operation**:
    
    - The loop `for (int num : arr)` iterates over each element in the array.
    - `unique ^= num;` XORs the current element `num` with `unique`. After processing all elements, `unique` will hold the value of the unique number in the array.
3. **Result**:
    
    - After the loop, `unique` contains the unique number that does not have a duplicate.

### Example:

Given the array `{2, 3, 5, 4, 5, 3, 4}`:

- **Step-by-step XOR**:
    - `unique = 0 ^ 2 = 2`
    - `unique = 2 ^ 3 = 1`
    - `unique = 1 ^ 5 = 4`
    - `unique = 4 ^ 4 = 0`
    - `unique = 0 ^ 5 = 5`
    - `unique = 5 ^ 3 = 6`
    - `unique = 6 ^ 4 = 2`

The result after XORing all elements is `2`, which is the unique number in the array.


## Find ith bit

```java
public class car {

  

    public static void main(String[] args) {

        int a=12;

        int i = 4;

        findibit(a,i);

    }

  

    private static void findibit(int a, int i) {

        int mask= 1 << i-1;

        if ((a & mask)!= 0 ) {

            System.out.println("1");

        }else{

            System.out.println("0");

        }

    }

}
```

## Set ith bit
>means turn bit bit 0 to 1 by using OR

```java
public class car {

  

    public static void main(String[] args) {

        int a=12; //binary 1100

        int i=2; // 2th  bit of 12 is 0

  

        int result = setIthBit(a,i);

        System.out.println("Bit after "+i+" is "+result);

    }

    static int setIthBit(int a ,int i){

        int mask = i << i-1;

        int bit=0;

        if ((a|mask) !=0) { //a | mask

            bit=1;

        }else{

            bit=0;

        }

  

        return bit; // a or with mask

    }

}
```

## Resest bit

```java
public class car {

  

    public static void main(String[] args) {

        int a=12; //binary 1100

        int i=3; // 2th  bit of 12 is 0

  

        int result = setIthBit(a,i);

        System.out.println("Bit after "+i+" is "+result);

    }

    static int setIthBit(int a ,int i){

        int mask = ~(i << i-1); //compliment of bit beacuse & with 0 gives 0 but with 1 reamin same

        int bit=0;

        if ((a&mask) !=0) {

            bit=0;

        }else{

            bit=0;

        }

  

        return bit; // a or with mask

    }

}
```


## Find num rep 3 times

```<>
public class car {

  

    public static void main(String[] args) {

        int nums[]={1,2,3,1,2,1,2};

  

        int unq = findUnqiue(nums);

        System.out.println(unq);

  

    }

  

    private static int findUnqiue(int[] nums) {

       int bitCount[]= new int[32]; // Array to store count of 1s

  

       for(int num:nums){

        for(int i=0;i<32;i++){

            if ((num&(1<<i))!=0) { // check if ith bit is set or not

                bitCount[i]++; //if the the ith bit is not zero

            }

        }

       }

  

       int res = 0;

       for(int i=0;i<32;i++){

        if (bitCount[i] %3 !=0) {

            res|=(1<<i);

        }

       }

       return res;

    }

}
```