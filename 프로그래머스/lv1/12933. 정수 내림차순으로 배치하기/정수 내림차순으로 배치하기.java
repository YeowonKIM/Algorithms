import java.util.Arrays;
class Solution {
    public long solution(long n) {
        String answer = "";
        String[] str=String.valueOf(n).split("");
        Arrays.sort(str);

        for (int i=0; i<str.length; i++) {
            answer += str[str.length-(i+1)];
        }
        return Long.parseLong(answer);
    }
}