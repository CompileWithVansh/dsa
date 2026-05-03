class Solution {
    // Time complexity: O(n), Space complexity: O(n)
    public String removeDuplicates(String s) {
        Stack<Character> stack =new Stack<>();
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if (stack.isEmpty()){
                stack.push(ch);

            }
            else if (ch !=stack.peek()){
                stack.push(ch);

            }
            else if(ch==stack.peek()){
                stack.pop();

            }

        }
        StringBuilder ans = new StringBuilder();
        while(!stack.isEmpty()){
            ans.append(stack.pop());

        }
        return ans.reverse().toString();
    }
}