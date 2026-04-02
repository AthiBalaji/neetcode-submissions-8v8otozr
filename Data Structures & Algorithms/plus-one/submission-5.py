class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1, -1,-1):
            digit = (digits[i]+c)%10
            print(digit)
            if digits[i]+c >=10:
                c=1
            else:
                c=0
            digits[i] = digit

        if c == 1:
            res = [1]
            for i in range(len(digits)):
                res.append(digits[i])
            return res 
        else:
            return digits 
        