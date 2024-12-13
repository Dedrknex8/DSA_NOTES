
## Maximum points from a card

>Approach : Take to pointer left and right sum and a maxSum
```java
class Solution {

    public int maxScore(int[] cardPoints, int k) {

        int left = 0;

        int right =0;

        int sum =0;

        int maxSum=0;

        for(int i=0;i<k;i++){

            left = left+cardPoints[i];

            //UPDATE MAX SUM

            maxSum = left;

        }

        int n = cardPoints.length;

        int rightIdx = n-1;

        //REMOVE THE 1 ELMENT FROM LEFT AND ADD RIGHT ELEMENT

        for(int i=k-1;i>=0;i--){

            left = left-cardPoints[i];

            right = right+cardPoints[rightIdx];

            rightIdx--;

            maxSum = Math.max(maxSum,left+right);

        }

        return maxSum;

    }

}
```

## Longest Substring without repetting

# Problem : Longest substring 

### My approach : Run a loop of i & j

2. check if the current element is present in the hashset or not 
3. if not then add , or break the loop and increase i pointer for it
4. complexity is not good as o(n ^ 2) and space o(k)

```code
 int maxLength =0;
          for(int i=0;i<s.length();i++){

             HashSet<Character> hashSet = new HashSet<>();

            for(int j=i;j<s.length();j++){

                char current = s.charAt(j);

            //LET'S CHECK IF REPEATING

            if(hashSet.contains(current)){

                break;

            }

  

            hashSet.add(current);

  

            maxLength = Math.max(maxlength,j-i+1);

            }

        }

        return maxLength;
```

### Optimization  : create  a hashset to contain unique elements in it `  HashSet<Character> hashSet = new HashSet<>();`

2. take two pointer left AND right move right the pointer and add the elements to the hashset  ` hashSet.add(currentChar);`
3. if found duplicate the remove the element from the hashset and increate the left pointer unitl it passes the duplicate element
```java
 HashSet<Character> hashSet = new HashSet<>(); // To store unique characters

        int maxLength = 0;

        int i = 0; // Left pointer of the sliding window

        // Iterate through the string with the right pointer

        for (int j = 0; j < s.length(); j++) {

            char currentChar = s.charAt(j);


            // If the character is already in the set, move the left pointer

            while (hashSet.contains(currentChar)) {

                hashSet.remove(s.charAt(i)); // Remove the leftmost character

                i++; // Shrink the window

            }

  

            // Add the current character to the set

            hashSet.add(currentChar);
            
            // Update the maximum length

            maxLength = Math.max(maxLength, j - i + 1);

        }

  

        return maxLength;

    }
```
