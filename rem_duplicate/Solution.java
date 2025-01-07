package rem_duplicate;

public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0; // If the array is empty, return 0.
        }

        int i = 0; // Pointer for the position of unique elements.

        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) { // When a new unique element is found
                i++; // Move the pointer to the next position
                nums[i] = nums[j]; // Copy the unique element to the new position
            }
        }

        return i + 1; // Return the count of unique elements
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1, 1, 2, 2, 3, 3, 4, 5, 5};

        int k = solution.removeDuplicates(nums);

        System.out.println("Number of unique elements: " + k);
        System.out.print("Modified array with unique elements: ");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }
}
