# Tyler Hegy
# UWYO COSC 1010
# Submission Date: 11/10/2024
# HW 04
# Lab Section: 12
# Sources, people worked with, help given to: Luis Molina
# Comments: Helped me understand the indexing to used for value variable 

from pathlib import Path

path = Path('prompt.txt')
contents = path.read_text()
lines = contents.splitlines()

output = Path('out.txt')
image = ""

for line in lines:
    image+="\n"
    new_line = line.split('\t')

    upper = len(new_line[0:-1])
    for i in range(0,upper):
        value = int(new_line[i].split(':')[1])
        if 'w' in new_line[i]:
            image+=' '*value
        elif '*' in new_line[i]:
            image += '*'*value
        else:
            continue

output.write_text(image)
    
