import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class RTI {

    // Function to convert Roman numeral to integer
    public int romanToInt(String s) {
        Map<Character, Integer> roman = new HashMap<>();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);

        int total = 0;
        int prev = 0;

        // Traverse the Roman numeral in reverse order
        for (int i = s.length() - 1; i >= 0; i--) {
            int value = roman.get(s.charAt(i));
            if (value < prev) {
                total -= value;
            } else {
                total += value;
            }
            prev = value;
        }
        return total;
    }

    // Function to convert integer to Roman numeral
    public String intToRoman(int num) {
        Map<Integer, String> roman = new HashMap<>();
        roman.put(1000, "M");
        roman.put(900, "CM");
        roman.put(500, "D");
        roman.put(400, "CD");
        roman.put(100, "C");
        roman.put(90, "XC");
        roman.put(50, "L");
        roman.put(40, "XL");
        roman.put(10, "X");
        roman.put(9, "IX");
        roman.put(5, "V");
        roman.put(4, "IV");
        roman.put(1, "I");

        StringBuilder result = new StringBuilder();

        // Traverse through the Roman numeral values in descending order
        for (Map.Entry<Integer, String> entry : roman.entrySet()) {
            while (num >= entry.getKey()) {
                result.append(entry.getValue());
                num -= entry.getKey();
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        RTI sol = new RTI();
        try (Scanner scanner = new Scanner(System.in)) {
            String ans = "y";

            while (ans.equals("y")) {
                System.out.println("Menu\n1. Roman to Integer\n2. Integer to Roman");
                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1 -> {
                        System.out.print("Enter the Roman number: ");
                        String romanNumber = scanner.next();
                        int result = sol.romanToInt(romanNumber);
                        System.out.println("The integer value of " + romanNumber + " is: " + result);
                    }
                    case 2 -> {
                        System.out.print("Enter the integer: ");
                        int integerNumber = scanner.nextInt();
                        String resultRoman = sol.intToRoman(integerNumber);
                        System.out.println("The Roman numeral for " + integerNumber + " is: " + resultRoman);
                    }
                    default -> System.out.println("Invalid choice!");
                }

                System.out.print("Quit [y/n]: ");
                ans = scanner.next();
            }
        }
    }
}
