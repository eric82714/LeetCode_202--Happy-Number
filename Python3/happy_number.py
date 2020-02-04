class Solution:
    def isHappy(self, n: int) -> bool:
        loop = []
        
        while True:
            total = sum([pow(int(x), 2) for x in str(n)])         
            if total == 1: return True
            if total in loop: return False
            loop.append(total)
            n = total
