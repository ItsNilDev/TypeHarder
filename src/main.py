import re
import pyautogui

regex = re.compile("<letter>(.*)<letter>")
line_to_search = 0
chars_to_press = ""

with open("../../ls/src/elements", 'r') as elements:
    for line_i, line  in enumerate(elements, 1):
        if(regex.search(line)):
            splited = line.split("<letter>")
            char = 1
            for i in splited:
                # pyautogui.press(splited[char][0], interval=0.0000002)
                if char == 446:
                    break
                chars_to_press = chars_to_press + splited[char][0]
                if len(splited[char]) > 20:
                    # pyautogui.press('space', interval=0.0002)
                    chars_to_press += ' '
                char += 1


pyautogui.write(chars_to_press, interval=0.000001)
