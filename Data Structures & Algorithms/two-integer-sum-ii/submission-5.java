class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;
        // Shrink the window based on if the sum is less than or greater than the target
        
        int sum = 0;

        while (l < r) {
            sum = numbers[l] + numbers[r];
            if (sum < target) {
                l++;
            } else if (sum > target) {
                r--;
            }
            else {
                return new int[] {l+1, r+1};
            }
        }
        return new int[0];
    }
}
