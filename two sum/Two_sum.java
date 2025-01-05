import java.util.HashMap;
import java.util.Scanner;

public class Two_sum {

    public static int[] Two_Sum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>(); // To store numbers and their indices
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            // Check if the complement exists in the map
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i }; // Return indices
            }
            // Add the current number and its index to the map
            map.put(nums[i], i);
        }
        return new int[] {}; // Return empty array if no solution is found (shouldn't happen per problem constraints)
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the number of elements: ");
            int n = scanner.nextInt();

            int[] nums = new int[n];
            System.out.println("Enter the elements: ");
            for (int i = 0; i < n; i++) {
                nums[i] = scanner.nextInt();
            }

            System.out.print("Enter the target: ");
            int target = scanner.nextInt();

            int[] result = Two_Sum(nums, target);
            if (result.length > 0) {
                System.out.println("Indices of numbers that add up to target: " + result[0] + ", " + result[1]);
            } else {
                System.out.println("No solution found.");
            }
        }
    }
}
