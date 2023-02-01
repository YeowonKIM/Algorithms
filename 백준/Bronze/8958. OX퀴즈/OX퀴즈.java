import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n =  sc.nextInt();
        for (int i=0; i<n; i++) {
            String str = sc.next();

            int middleScore=0, score=0;
            for (int j=0; j<str.length(); j++) {
                middleScore =(str.charAt(j)=='O') ? middleScore +=1 : 0;
                score += middleScore;
            }
            System.out.println(score);
        }
    }
}
