class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def dfs(v):
            visited[v] = True
            for next_v in rooms[v]:
                if visited[next_v] == False:   
                    dfs(next_v)

        dfs(0)
        return all(visited)


        