import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> list = new ArrayList<>();

        Arrays.sort(numbers);

        // 중복 상관없이 일단 리스트에 합 다 받기
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                sum = numbers[i] + numbers[j];
                System.out.println(sum);
                if (list.indexOf(sum) < 0) {
                    list.add(sum);
                }
            }
        }
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}