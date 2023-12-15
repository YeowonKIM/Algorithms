class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        # vertex에 연결되어 있는 모든 vertex에 방문 할 것
        def bfs(v):
            queue = deque()
            queue.append(v)
            visited[v] = True
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if visited[next_v] == False:
                        queue.append(next_v)
                        visited[next_v] = True

        bfs(0)
        # if len(visited) == len(rooms): return True  # 근데 여기서 False 개수 체크 해줘야 함
        # else: return False
        return all(visited)

