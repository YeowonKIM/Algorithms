import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int change = 1000 - sc.nextInt();

        int [] moneys = {500,100,50,10,5,1};

        // cnt : 돈전 개수, rest : 남은 잔돈
        int cnt =0, rest=change;
        for (int money : moneys) {
            cnt += rest/money;
            rest = rest%money;
            if (rest==0)
                break;
        }
        System.out.println(cnt);
    }
}