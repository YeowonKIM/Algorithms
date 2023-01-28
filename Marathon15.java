class Solution15 {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for (int i=0; i<a.length; i++) {
            answer += a[i]*b[i];
        }
        return answer;
    }
}

public class Marathon15 {
    public static void main(String[] args) {
        int[] a= {1,2,3,4};
        int[] b = {-3,-1,0,2};

        Solution15 solution15 = new Solution15();
        System.out.println(solution15.solution(a, b));
    }
}
