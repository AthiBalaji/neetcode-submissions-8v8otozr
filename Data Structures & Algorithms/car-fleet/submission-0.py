class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        stack = []

        for p, s in reversed(sorted(pair)):
            time_to_reach = (target - p)/s
            if not stack:
                stack.append(time_to_reach)
            if stack and time_to_reach > stack[-1]:
                stack.append(time_to_reach)

        return len(stack)



        