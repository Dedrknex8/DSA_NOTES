
# Find all permuation of a string

```java
public class Permuation {  
    public static void main(String[] args) {  
        Perm("","abc");  
        int ans = PermCount("","abcd");  
        System.out.println(ans);  
  
  
    }  
  
    private static void Perm(String p, String up) {  
    if (up.isEmpty()){  
        System.out.println(p);  
        return;  
    }  
  
    Character ch = up.charAt(0);  
  
    for (int i=0;i<=p.length();i++){  
        String f= p.substring(0,i);  
        String s = p.substring(i,p.length());  
        Perm(f+ch+s,up.substring(1));  
    }  
  
    }  
    private static int PermCount(String p, String up) {  
        if (up.isEmpty()){  
            return 1;  
        }  
  
        Character ch = up.charAt(0);  
        int count=0;  
        for (int i=0;i<=p.length();i++){  
            String f= p.substring(0,i);  
            String s = p.substring(i,p.length());  
            count= count + PermCount(f+ch+s,up.substring(1));  
        }  
    return count;  
    }  
  
}
```