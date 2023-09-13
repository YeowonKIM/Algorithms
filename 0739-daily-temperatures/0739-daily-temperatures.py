class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for curr_date, curr_temp in enumerate(temperatures):
            while stack and stack[-1][1] < curr_temp:
                lower_date, lower_temp = stack.pop()
                answer[lower_date] = curr_date - lower_date
            stack.append((curr_date, curr_temp))
        return answer