import re

regex = re.compile("<letter>(.*)<letter>")

with open("../../ls/src/elements", 'r') as elements:
    for line_i, line  in enumerate(elements, 1):
        if(regex.search(line)):
            print(line_i)

