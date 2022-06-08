
import re


with open('./properties-to-delete-in-gnl.txt') as text:
    text = text.read()
    pattern = '\(([-a-z0-9@:%_\+.~#?&/=]*)?\.?([-a-z]*\.[-a-z]{2,4})(\.[-a-z]{2,4})?(\/[-a-zA-Z0-9@:%_\+.~#?&/=]*)?\)'
    allMatches = re.findall(pattern, text)

i = 1

for match in allMatches:
    if len(match) > 1:
        buildMatchString = ''.join(match)
        print(str(i) + " " + buildMatchString)
        print()
        
    else:
        print(str(i) +  " " + match)
        print()
    i+=1