
from random import randint

punctuations = '''!()-[]{};:'"'\,<>./?@#$%^&*_~'''
huge_list = []
name_list = []
adjective_list = []
i = 0
f = open("sortirane.txt", encoding="utf-8")
for line in f:
    huge_list.extend(line.split())

#print(huge_list)

for x in huge_list:
    if x.isupper() and len(x) > 1:
        name_list.append(x)
while i < len(name_list):
    for x in name_list[i]:
        #  print(x)
        if x in punctuations:
            name_list[i] = name_list[i].replace(x, "")
    i += 1
# print(name_list)
# print(len(name_list))
huge_list.clear()
f = open("adjectives.txt", encoding="utf-8")
for line in f:
    huge_list.extend(line.split())
for x in huge_list:
    if x.isalpha() and len(x) > 1:
        adjective_list.append(x)
# print(adjective_list)

value1 = randint(0, 314)
value2 = randint(0, 4840)
name = name_list[value1].lower().title() + " " + adjective_list[value2].title()
print(name)
history = open('history.txt', 'a')
history.write("\r" + name)
history.close()