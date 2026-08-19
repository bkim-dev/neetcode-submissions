class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        int temp = 0, maxCount = 0;
        for (int n : nums) {
            hm.put(n, 1 + hm.getOrDefault(n, 0));
            if (hm.get(n) > maxCount) {
                temp = n;
                maxCount = hm.get(n);
            }
        }
        return temp;
    }
}