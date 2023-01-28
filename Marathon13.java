class Solution13 {
    public String solution(int a, int b) {
        String answer = "";
        String[] dayOfWeek = {"THU","FRI","SAT","SUN","MON","TUE","WED"};
        int[] lastDate = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int sum = 0;

        for (int i=0; i<a-1; i++) {
            sum +=lastDate[i];
        }
        answer = dayOfWeek[(sum+b)%7];
        return answer;
    }
}
public class Marathon13 {
    public static void main(String[] args) {
        int a= 1, b=1;

        Solution13 solution13 = new Solution13();
        System.out.println(solution13.solution(a,b));
    }
}
