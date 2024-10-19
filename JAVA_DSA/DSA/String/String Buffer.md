
While String is immutable the String Buffer is mutable means the assinged value can be changed without creating a object every time

# Sample Code

```java
public class StringBufferExample {
    public static void main(String[] args)
    {
        StringBuffer sb = new StringBuffer();
        sb.append("Hello");
        sb.append(" ");
        sb.append("world");
        String message = sb.toString();
        System.out.println(message);
    }
}

```


## Advatages of Sting Buffer

1. It is muatble
2. Efficient 
3. Thread safe  : when one object is created then other object wait it to finish fist