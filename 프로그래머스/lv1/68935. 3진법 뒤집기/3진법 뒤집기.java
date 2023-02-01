class Solution {
     public int solution(int n) {
        String ternary = "";
        while (n>0) {
            ternary = ternary + ""+n%3;
            n /= 3;
        }
        System.out.println("ternary="+ternary);
        int sum =0;
        for (int i=0; i<ternary.length(); i++) {
            char ch = ternary.charAt(ternary.length()-(i+1));
            sum += (ch -'0')*Math.pow(3, i);
        }
        return sum;
    }
}