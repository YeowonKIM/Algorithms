import java.util.Arrays;

class Solution11 {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        for (int i=0; i<n; i++) {
            answer[i] = (long)(i+1)*x;
        }
        return answer;
    }
}
public class Marathon11 {
    public static void main(String[] args) {
        int x = -4, n =2;
        Solution11 solution11 = new Solution11();
        System.out.println(Arrays.toString(solution11.solution(x,n)));
    }
}
