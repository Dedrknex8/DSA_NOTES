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