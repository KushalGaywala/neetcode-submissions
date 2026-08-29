class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for string in strs:
            enc_str += f'{str(len(string))}#{string}'
        print(enc_str)
        return enc_str

    def decode(self, s: str) -> List[str]:
        str_list = list()
        char_count = 0
        str_char_count = ""
        temp_str = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                char_count = i + int(str_char_count)
                str_char_count = ""
                temp_str = ""
                
                if i == char_count:
                    str_list.append("")

                while i < char_count and i < len(s):
                    temp_str += s[i]
                    i += 1
                
                    if i == char_count:
                        str_list.append(temp_str)

            else:
                str_char_count += s[i]
                i += 1
        
        return str_list
