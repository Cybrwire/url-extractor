
import re
from tkinter.filedialog import askopenfilename

# Open an askfile window
file = askopenfilename()

# Set pattern for searching
PATTERN = '\(([-a-z0-9@:%_\+.~#?&/=]*)?\.?([-a-z]*\.[-a-z]{2,4})(\.[-a-z]{2,4})?(\/[-a-zA-Z0-9@:%_\+.~#?&/=]*)?\)'

# Open file and read data
with open(file, 'r', encoding='utf-8') as text:
    text = text.read()

# Find matches in the data
allMatches = re.findall(PATTERN, text)

# Print out the matches and the respective index
for i, match in enumerate(allMatches):
    if len(match) > 1:
        buildMatchString = ''.join(match)
        print(f'{i} {buildMatchString}\n')
    else:
        print(f'{i} {match}\n')
