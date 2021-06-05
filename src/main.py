import re
import pyautogui
import time

# wait for some seconds
time.sleep(5)
regex = re.compile("<letter>(.*)<letter>")
line_to_search = 0
chars_to_press = ""

# Copy all the html elements to a file and source it here
with open("[file]", 'r') as elements:
    for line_i, line  in enumerate(elements, 1):
        # Find the line containing "<letter>"
        if(regex.search(line)):
            splited = line.split("<letter>")
            char = 1
            for i in splited:
                # pyautogui.press(splited[char][0], interval=0.0000002)
                try:
                    # Add the chars
                    chars_to_press = chars_to_press + splited[char][0]
                except IndexError:
                    break
                # if reached to the end of word, add space
                if len(splited[char]) > 20:
                    # pyautogui.press('space', interval=0.0002)
                    chars_to_press += ' '
                char += 1

# Write the paragraph
pyautogui.write(chars_to_press, interval=0.025)
