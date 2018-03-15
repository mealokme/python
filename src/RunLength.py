# Given a string in run length encoded form, decode it 
# e.g. 3[abc]2[ab]c
"""
# ASK 
# 1. Write out different forms of the strings to clarify 
 e.g.
 - abc
 - [abc]
 - c1[abc]
 Malformed strings :  
 - [ab ;  ab] ; 3[abc]3, [], ...
"""



def decompress(s):
    substr = ""
    parts = []
    c=1
    for i in range(len(s)):
        print (s[i])
        if s[i] != '[' and s[i] != ']' and not s[i].isalnum():
            raise Exception("unexpected character")
        if s[i].isdigit(): # assume single digit 
            c = int(s[i])
        elif s[i] == '[': 
            inside = True
        elif s[i] == ']':
            parts.append(substr * c )
            substr = ""
            c=1
            inside = False
        elif s[i].isalpha():
            substr += s[i]

    if(len(substr) > 0 ):
        parts.append(substr)
    return "".join(parts)
        
        
if __name__ == "__main__":
    d = decompress("3[abc]2[ab]c")
    print (d)

        




def containsAny(str, set):
    """ check wheter str contains any characters in set """
    return True in [] 








