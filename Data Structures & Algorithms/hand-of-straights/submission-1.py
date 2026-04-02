class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize !=0:
            return False

        counter = defaultdict(int)
        for elem in hand:
            counter[elem]+=1
        
        hand.sort()
        for elem in hand:
            if counter[elem] == 0:
                continue
            counter[elem] -=1
            for i in range(1, groupSize):
                print("ith check for elem",elem,  i)
                if counter[elem+i] == 0:
                    print("counter elem+i", counter[elem+i],"false printed")
                    return False
                else:
                    print("elem+i is being minused", elem+i)
                    counter[elem+i]-=1
        return True 

            
            
        