```java
//What is recursion  
//It's a way of calling a function from a function  
//Why recusrion : because it's help us in solve big and complex  
//problem in a simple way  
//Recursion starts when base class == true
  
public class Recursion {  
    public static void main(String[] args) {  
        print(1);  
    }  
    static  void print(int n) {  
        //base upto which the num will print  
        if (n == 5){  
            System.out.println(5);  
            return;  
        }  
        System.out.println(n);  
        print(n + 1);  
  
    }  
  
}
```


## TO count no of dig 

```java
public class car {

  

    public static void main(String[] args) {

        int num=9;

        int steps=numofstep(num);

        System.out.println(steps);

    }

    public static int numofstep(int num){

        return helper(num,0);

    }

    static int helper(int num,int steps){

        if (num==0) {

            return steps;

        }

        if (num%2==0) {

            return helper(num/2, steps+1);

        }

        return helper(num-1, steps+1);

    }

}
```

## To rever a num

```java
public class Primeno {

    public static void main(String[] args) {

        rev1(1234);

        System.out.println(sum);

    }

    static int sum = 0;

    static void rev1(int n){

        if (n==0) {

            return;

        }

        int reminder = n %10;

        sum = sum *10 + reminder;

        rev1(n/10);

}

}
```