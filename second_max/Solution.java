package DSA.second_max;

public class Solution{
    public int second_Largest(int[] arr){
        int max=0;
        int max2=0;
        for (int i=0;i<arr.length;i++){
            if(i > max){
                max=i;
            }

            else if (i > max2 && max != max2) {
                max2 = i;
                
            }
        }
        return max2;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println(s.second_Largest(arr));
    }
}