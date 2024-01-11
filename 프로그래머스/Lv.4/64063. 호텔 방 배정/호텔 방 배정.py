import sys
sys.setrecursionlimit(10**7)  # 재귀 호출 깊이 제한

def solution(k, room_number):
    answer = []
    reserved_room = dict()

    def find(room):
        if room not in reserved_room:
            reserved_room[room] = room+1
            return room

        reserved_room[room] = find(reserved_room[room])
        return reserved_room[room]

    for room in room_number:
        vacant_room = find(room)
        answer.append(vacant_room)

    return answer