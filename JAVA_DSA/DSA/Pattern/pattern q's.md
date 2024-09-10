
# Printing num pyramid

```
public class car {

  

    public static void main(String[] args) {

        pattern(4);

    }

    static void pattern(int n){

        for(int row=1; row <= n; row++){

            for(int col=1;col <= row;col++){

                System.out.print(col + " ");

            }

            System.out.println();

        }

    }

}
```

### output
```
1 
1 2
1 2 3
1 2 3 4
```

# Pattern 2

```
public class car {

  

    public static void main(String[] args) {

        pattern(5);

    }

    static void pattern(int n){

        for(int row=0; row <= 2 * n; row++){

            int toltalNumrows = row > n ? 2 * n - row  :row;

            for(int col=1;col <= toltalNumrows;col++){

                System.out.print("* ");

            }

            System.out.println();

        }

    }

}
```

#### Output
```
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```

