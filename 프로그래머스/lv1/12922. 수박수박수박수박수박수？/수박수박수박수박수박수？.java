class Solution {
    public String solution(int n) {
        String answer = "";
        for (int i=1; i<n+1; i++) {
            if (i%2==1){answer = answer+"수";}
            else {answer = answer+"박";}
        }
        return answer;
    }
}