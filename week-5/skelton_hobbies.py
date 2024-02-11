#
# Title: skelton_hobbies.py
# Author: Cody Skelton
# Date: 02.11.2024
# Purpose: Loops practice 
# Requirements from WEB 335 Exercise 5.3
#

# list of hobbies
hobbies = ["haunt", "leathercraft", "video games", "d&d", "cooking"]

# loop through hobbies list
for x in hobbies:
    print(x)

# list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# loop through days and get weekends off
i = 0

for x in days:
    if i == 5 or i == 6:
        print(x + ": You are off. Enjoy your hobbies")
    else:
        print(x + ": It is a work day")
    i += 1