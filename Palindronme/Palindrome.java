import java.util.Scanner;

public class Palindrome {

    public static boolean isPalindrome(int x) {
        if (x < 0)
            return false; // Negative numbers cannot be palindromes

        int original = x;
        int reversed_num = 0;

        while (x > 0) {
            int digit = x % 10;
            reversed_num = (reversed_num * 10) + digit;
            x = x / 10;
        }

        return original == reversed_num;
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {

        System.out.print("Enter a number: ");
        int num = scanner.nextInt();

        if (isPalindrome(num)) {
            System.out.println(num + " is a palindrome");
        } else {
            System.out.println(num + " is not a palindrome");
        }

        scanner.close();
    }
}
}
