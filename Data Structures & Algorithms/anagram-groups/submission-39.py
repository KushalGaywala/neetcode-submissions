class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = defaultdict(list)
        
        for i, string in enumerate(strs):
            char_count = [0]*26            
            for j, char in enumerate(string):
                char_count[ord(char)-97] = char_count[ord(char)-97] + 1
            matches[tuple(char_count)].append(string)
        
        return list(matches.values())