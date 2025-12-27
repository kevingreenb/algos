class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        ans, prev = 0, 0
        for p, s in cars:
            time = (target-p)/s
            if time > prev:
                prev = time
                ans += 1
        return ans