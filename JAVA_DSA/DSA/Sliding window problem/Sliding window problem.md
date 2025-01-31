## Longest Subarray

```java
public class LongestSubarray {  
    public static void main(String[] args) {  
        int[] arr = {2,5,1,7,10};  
        int target = 14;  
  
        int res = findLongestSum(arr,target);  
        System.out.println(res);  
    }  
  
    //Bruteforce Update  
//    static int findLongestSum(int[] arr, int target) {  
//        int maxSum = Integer.MIN_VALUE;  
//  
//        for (int i = 0; i < arr.length -1; i++) {  
//            int sum=0;  
//            for (int j = i ; j < arr.length -1; j++) {  
//                sum+=arr[j];  
//                if (sum <= target){  
//                    maxSum = Math.max(maxSum,sum);  
//                }  
//            }  
//        }  
//        return maxSum;  
//    }  
  
    //Optimize way    static int findLongestSum(int[] arr, int target) {  
        int sum = 0;  
        int maxLength = 0;  
        int l = 0;  
  
        for (int r = 0; r< arr.length; r++) {  
            sum += arr[r]; //add the current element  
            //IF SUM EXCEEDS THE TARGET LIMIT            while (sum >= target) {  
                sum -= arr[l]; // remove the left pointer  
                l++; //move the left pointer to right  
            }  
            maxLength = Math.max(maxLength, r - l + 1);  
        }  
        return maxLength;  
    }  
}
```

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


## max consecutive ones

Problem : get the max consecutive one with a contrains of fliping at most k zeros in it

>Approach : 

1. Bruteforce : 
	- for this run two loops i(from 0 to n) & j (from i to n)
	- in 1st loop let a count off zero be zero
	- 2nd loop check if the found any zero then increase the count of zero 
	- And lastly if countZero <= k update len and maxLen
```code
public int longestOnes(int[] nums, int k) {

        int len = 0;

        int n = nums.length;

        int maxLength = 0;

        for(int i=0;i<n;i++){

            int countZero = 0;

            for(int j=i;j<n;j++){

                if(nums[j] == 0){

                    countZero++;

                }

                if(countZero<=k){

                    len =  j -i +1;

                    maxLength = Math.max(maxLength,len);

                }

            }

        }

        return maxLength;

    }
```

2. Optimized approach : using left and right pointer

```CODE
class Solution {

    public int longestOnes(int[] nums, int k) {

        int len = 0;

        int n = nums.length;

        int maxLength = 0;

        int left=0;

        int right =0;

        int zero = 0;

        //RUN A WHILE TILL THE SIZE OF ARRAY

        while(right < n){

            if(nums[right] ==0 ){

                zero++;

            }


            //SHRINK THE WINDOW UNITL THE NUM OF ZERO IS WITHIN LIM

            while(zero > k){

            if(nums[left]== 0){

                zero--;

            }

            left++;

            }

            //UPDATE MAX LEN

            len = right - left +1;

            maxLength = Math.max(maxLength,len);

            right++;

        }

        return maxLength;

    }

}
```


## Fruits into basket leetcode

problem : add fruits of distincs element as long as there at most 2 types

> Simple bruteforce approach

```java
class Solution {

    public int totalFruit(int[] fruits) {

        int maxLen =0;

        int n = fruits.length;

  

        for(int i=0;i<n;i++){

            HashSet<Integer> hash = new HashSet<>();

            for(int j=i;j<n;j++){

                hash.add(fruits[j]);

  

                if(hash.size() <= 2){

                    maxLen = Math.max(maxLen,j-i+1);

  

                }

                else

                    break;

            }

        }

        return maxLen;

    }

}
```

Done Upto fruit basket