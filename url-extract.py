
import re
from tkinter.filedialog import askopenfilename

# Open an askfile window
file = askopenfilename(
    filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])

# Set pattern for searching
PATTERN = '\(([-a-z0-9@:%_\+.~#?&/=]*)?\.?([-a-z]*\.[-a-z]{2,4})(\.[-a-z]{2,4})?(\/[-a-zA-Z0-9@:%_\+.~#?&/=]*)?\)'

# Open file, read data, and find all matches
with open(file, 'r', encoding='utf-8') as f:
    allMatches = re.findall(PATTERN, f.read())

# Print out the matches and the respective index
for i, match in enumerate(allMatches):
    if len(match) > 1:
        print(f'{i} {"".join(match)}\n')
    else:
        print(f'{i} {match}\n')
