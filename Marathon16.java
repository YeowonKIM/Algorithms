class Solution16 {
    boolean solution(String s) {
        s = s.toLowerCase();
        int cnt=0;

        for (int i=0; i<s.length();i++) {
            char charAt = s.charAt(i);
            if (charAt=='p') {
                cnt +=1;
            } else if (charAt=='y') {
                cnt -= 1;
            }
        }
        return (cnt==0)? true : false;
    }
}

public class Marathon16 {
    public static void main(String[] args) {
        String str1 = "pPoooyY";
        String str2= "Pyy";

        Solution16 solution16 = new Solution16();
        System.out.println(solution16.solution(str1));
        System.out.println(solution16.solution(str2));


    }
}
