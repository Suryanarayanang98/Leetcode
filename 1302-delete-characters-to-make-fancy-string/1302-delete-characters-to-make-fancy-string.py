class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        new_string = s[:2]
        last_two_chars = [s[0],s[1]]
        
        for char in s[2:]:
            if len(set(last_two_chars)) != 1:
                new_string += char
                last_two_chars.pop(0)
                last_two_chars.append(char)
            else:
                if char not in last_two_chars:
                    new_string += char
                    last_two_chars.pop(0)
                    last_two_chars.append(char)
        
        return new_string
                
            

        