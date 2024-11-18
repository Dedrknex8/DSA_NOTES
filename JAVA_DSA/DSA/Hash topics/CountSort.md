```java
class Solution {

    public int[] sortArray(int[] nums) {

        if (nums == null || nums.length <= 1) {

            return nums; // Return the input array as is.

        }

  

        // Get the minimum and maximum elements in the array.

        int min = nums[0];

        int max = nums[0];

        for (int num : nums) {

            if (num > max) max = num;

            if (num < min) min = num;

        }

  

        // Create a frequency array with size based on the range of values.

        int range = max - min + 1;

        int[] countArray = new int[range];

  

        // Populate the frequency array.

        for (int num : nums) {

            countArray[num - min]++;

        }

  

        // Populate the original array with sorted values.

        int idx = 0;

        for (int i = 0; i < range; i++) {

            while (countArray[i] > 0) {

                nums[idx++] = i + min; // Add back the offset for negative numbers.

                countArray[i]--;

            }

        }

  

        return nums;

    }

}
```