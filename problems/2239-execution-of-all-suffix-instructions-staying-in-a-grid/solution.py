class Solution:
    def executeInstructions(
        self, n: int, startPos: List[int], s: str
    ) -> List[int]:
        answer = []
        l = len(s)
        for i in range(l):
            steps = 0
            instructions = s[i:]
            x, y = startPos
            for ins in instructions:
                if ins == "L": y -= 1
                elif ins == "R": y += 1
                elif ins == "U": x -= 1
                elif ins == "D": x += 1
                steps += 1
                if x < 0 or x >= n or y < 0 or y >= n:
                    steps-=1
                    break

            answer.append(steps)
        return answer
