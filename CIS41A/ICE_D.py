'''
Gautam Mehta
In Class Unit D
'''
for i in range (10, -1, -2):
    print (i)

import re
string = "I think that I shall never see a poem lovely as a tree. - Joyce Kilmer"
search= re.findall(r"\b\w*?[aeiouAEIOU]", string)
joined =" ".join(search)
print (joined)