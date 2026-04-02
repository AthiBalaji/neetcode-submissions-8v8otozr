class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert_string_to_int(s):
            p= 1
            sum = 0
            for l in range(len(s)-1,-1,-1):
                temp =p*int(s[l])
                sum+=temp
                p*=10
            return sum 
        
        a =convert_string_to_int(num1)
        b =convert_string_to_int(num2)  
        return str(a*b)

        