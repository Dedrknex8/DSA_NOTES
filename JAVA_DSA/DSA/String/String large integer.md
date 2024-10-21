1. Big integer  - > used for store or perfome a=math in big interger i.e very large integer

```JAVA
import java.math.BigInteger;  
  
public class Bigint {  
    public static void main(String[] args) {  
        int a = 30;  
        int b = 67;  
        BigInteger A = BigInteger.valueOf(33);  
        BigInteger B = BigInteger.valueOf(34565);  
        //String  
        BigInteger C = new BigInteger("35449411215484555");  
  
        //Addition  
        BigInteger s = A.add(C);  
  
  
        System.out.println(s);  
    }  
  
}
```

