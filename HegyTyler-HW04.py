# Tyler Hegy
# UWYO COSC 1010
# Submission Date: 11/10/2024
# HW 04
# Lab Section: 12
# Sources, people worked with, help given to: Luis Molina
# Comments: Helped me understand the indexing to use in the if statement 

from pathlib import Path

path = Path('prompt.txt')
contents = path.read_text()
lines = contents.splitlines()

output = Path('out.txt')
image = ""
for line in lines:
    image+="\n"
    new_line = line.split('\t')
    for i in range(len(new_line)-1):
        if 'w' in new_line[i]:
            image+=' '*int(new_line[i].split(':')[1])
        else:
            image += '*'*int(new_line[i].split(':')[1])
output.write_text(image)
