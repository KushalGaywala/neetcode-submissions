class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            scount = dict([(i, 0) for i in s])
            tcount = dict([(i, 0) for i in t])
            print(scount, tcount)
            
            for schar in s:
                scount[schar] = scount[schar] + 1
            for tchar in t:
                tcount[tchar] = tcount[tchar] + 1
            
            print(scount, tcount)

            for key, value in scount.items():
                print(key, value)
                print(key not in tcount, key, tcount)
                if key not in tcount:
                    return False
                if tcount[key] != value:
                    return False
            
            return True

        return False