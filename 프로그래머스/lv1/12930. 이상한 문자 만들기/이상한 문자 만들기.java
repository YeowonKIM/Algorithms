class Solution {
     public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        char[] ch = s.toCharArray();

        int idx = 0;
        for (char c : ch) {
            if (c == ' ') {
                idx = 0;
                sb.append(" ");
            } else if (idx % 2 == 0) {
                sb.append(Character.toUpperCase(c));
                idx++;
            } else {
                sb.append(Character.toLowerCase(c));
                idx++;
            }
        }

        return sb.toString();
    }
}