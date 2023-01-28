class Solution12 {
    public long solution(int price, int money, int count) {
        long tot = 0;
        // 필요 금액
        for (int i=1; i<count+1; i++) {
            tot += price*i;
        }
        return ((tot-money)<0)? 0 : tot-money;
    }
}

public class Marathon12 {
    public static void main(String[] args) {
        int price = 3, money =20, count =4;

        Solution12 solution12 = new Solution12();
        System.out.println(solution12.solution(price,money,count));

    }
}
