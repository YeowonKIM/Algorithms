import static java.lang.Math.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        double sqrt= sqrt(n);
        if (sqrt< 0 || sqrt-(long)sqrt !=0) { answer= -1;}
        else {
            answer = (long) sqrt;
            answer = (answer+1)*(answer+1);
        }
        return answer;
    }
}