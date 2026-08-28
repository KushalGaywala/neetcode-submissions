class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        matches = {}
        
        for i, string in enumerate(strs):
            char_count = [0]*26            
            for j, char in enumerate(string):
                char_count[ord(char)-97] = char_count[ord(char)-97] + 1
        
            if tuple(char_count) not in matches:
                matches[tuple(char_count)] = [string]
            else:
                matches[tuple(char_count)].append(string)
        
        # for value in matches.values():
        #     anagrams.append(list(value))

        return list(matches.values())