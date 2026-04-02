class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = defaultdict(int)
        for i,c in enumerate(s):
            last_occurence[c] = i 
        res = []
        k = 0 
        l = last_occurence[k]
        count = 1 
        while k < len(s):
            l = max(last_occurence[s[k]], l)
            print("last occurence for k, l",k,l)
            if k == l:
                print("k =l",k,l)
                res.append(count)
                print('res',res)
                k = last_occurence[s[k]]+1
                count = 1
                continue
            else:
                k+=1
                count+=1
            

        return res          

        