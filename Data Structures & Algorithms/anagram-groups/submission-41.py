class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = defaultdict(list)
        
        for string in strs:
            char_count = [0]*26            
            for char in string:
                char_count[ord(char)-97] += 1
            matches[tuple(char_count)].append(string)
        
        return list(matches.values())