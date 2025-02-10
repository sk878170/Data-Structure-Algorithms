public class Solution {
    public int Reverse(int n){
        if (n == 0){
            return 0;
        }

        else{
            int rev =0;
            while (n != 0){
                rev = (rev % 10) + (n/10);
                n = n% 10;
            }
            return rev;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 123;
        int result = solution.Reverse(n);
        System.out.println(result);
    }
}
