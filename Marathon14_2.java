import java.util.ArrayList;
import java.util.Arrays;
class Solution14_2 {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i<arr.length;i++){
            if(arr[i]%divisor==0){
                list.add(arr[i]);
            }
        }
        if(list.size()==0){
            answer = new int[1];
            answer[0]=-1;
        }else{
            answer = new int[list.size()];
            for(int i =0; i<list.size() ; i++){
                answer[i] = list.get(i);
            }
            Arrays.sort(answer);
        }
        return answer;
    }
}
public class Marathon14_2 {
    public static void main(String[] args) {
        int arr[] = {5, 9, 7, 10};
        int divisor = 5;

        Solution14_2 solution14_2 = new Solution14_2();
        System.out.println(Arrays.toString(solution14_2.solution(arr, divisor)));
    }
}
