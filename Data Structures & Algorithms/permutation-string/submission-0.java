class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int l = 0;
        int r = l + s1.length();

        if (s1.length() > s2.length()) {
            return false;
        }

        HashMap<Character, Integer> count1 = new HashMap<>();
        for (int i = 0; i < s1.length(); i++) {
            char t = s1.charAt(i);
            count1.put(t, count1.getOrDefault(t, 0) + 1);
        }
    
        int need = count1.size();
        for (int i = 0; i < s2.length(); i++) {
            HashMap<Character, Integer> count2 = new HashMap<>();
            int charCount = 0;
            for (int j = i; j < s2.length(); j++) {
                char c = s2.charAt(j);
                count2.put(c, count2.getOrDefault(c, 0) + 1);

                if (count1.getOrDefault(c, 0) < count2.get(c)) {
                    break;
                }

                if (count1.getOrDefault(c, 0) == count2.get(c)) {
                    charCount++;
                }

                if (charCount == need) {
                    return true;
                }
            }
        }
        return false;
    }
}
