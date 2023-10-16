class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []

        def dfs(v):
            visited.append(v)
            for next_v in rooms[v]:
                if next_v not in visited:
                    dfs(next_v)

        dfs(0)
        if len(visited) == len(rooms): return True
        else: return False

        