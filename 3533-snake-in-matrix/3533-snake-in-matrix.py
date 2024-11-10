class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i_coord = 0
        j_coord = 0
        for cmd in commands:
            if cmd == "UP":
                i_coord -= 1
            if cmd == "RIGHT":
                j_coord += 1
            if cmd == "DOWN":
                i_coord += 1
            if cmd == "LEFT":
                j_coord -= 1
        
        return i_coord*n + j_coord