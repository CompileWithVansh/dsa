//using string conversion


class Solution {
    public int[] separateDigits(int[] nums) {
        
        List<Integer> answer = new ArrayList<>();

        for (int num : nums) {

            String s = String.valueOf(num);

            for (char digit : s.toCharArray()) {
                answer.add(digit - '0');
            }
        }

        int[] result = new int[answer.size()];

        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }

        return result;
    }
} 