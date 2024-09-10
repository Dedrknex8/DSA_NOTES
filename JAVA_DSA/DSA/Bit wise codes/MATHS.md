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

## Check which no are prime b/w  40

```<>
public class Primeno {

  

    public static void main(String[] args) {

        int n=40;

  

        boolean[] prime = new boolean[n+1];

        Seive(n,prime);

    }

    //Assume every int in array is prime --> false

    private static void Seive(int n, boolean[] prime) {

        for(int i=2;i*i<=n;i++){

            if(!prime[i]){ // if prime not equal to true

                for(int j=i*2;j<=n;j+=i){

                    prime[j] = true; // set mutltiples to true

                }

            }

        }

        for(int i=2;i<=n;i++){

        if(!prime[i]){

            System.out.println("Is prime "+i);

        }

    }

  

    }

  

}
```