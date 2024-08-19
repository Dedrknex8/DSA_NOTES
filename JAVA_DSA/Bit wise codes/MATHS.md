# prime no

```<>
public class Primeno {

    public static void main(String[] args) {

            boolean res= isprme(5);

            System.out.println(res);

    }    

    private static boolean isprme(int n){

        for(int i=2;i<n;i++){

            if (n%i ==0) {

                System.out.println("No is not prime");

                return false;

            }

        }

        System.out.println("Is prime");

        return true;

    }

}
```

## optimised way

```<>
public class Primeno {

    public static void main(String[] args) {

            boolean res= isprme(20);

            System.out.println(res);

    }    

    private static boolean isprme(int n){

        if (n<=1) {

            return false;

        }

  

        int c=2;

        boolean isprme = true; // assume n is prime until proven

        while (c*c<=n) {

            System.out.println(c);

            if (n%c ==0) {

                System.out.println("The c current is"+c);

                isprme = false;

            }

            c++;

        }

        return true;

    }

}
```