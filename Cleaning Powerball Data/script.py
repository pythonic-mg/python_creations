import os
from urllib.request import urlretrieve

url = ("https://www.texaslottery.com/export/sites/lottery/"
       "Games/Powerball/Winning_Numbers/powerball.csv")

pb_file = "powerball.csv"

urlretrieve(url, pb_file)

with open(pb_file, "r") as fileref:
    draws = fileref.readlines()

print(f"\nThere are {len(draws)} lines of data in this file.\n")

print(f"Your original data looks like this: {draws[:1]} \n")

list_of_lists = []

for draw in draws:
    list_of_lists.append(draw.split(","))

print(f"After splitting the string into a list: {list_of_lists[:1]} \n")

for list in list_of_lists:
    list[:4] = []
    list[6:] = []

print(f"This is your data after removing the game title and date of draw: {list_of_lists[:1]}\n")

with open("just_numbers.csv", "w") as fileref:
    fileref.write("B1,B2,B3,B4,B5,PB\n")
    for list in list_of_lists:
       line = ",".join(list)
       fileref.write(line + "\n")

print(f'A new file, "just_numbers.csv" has been created. It has been saved to this directory, {os.getcwd()}')
