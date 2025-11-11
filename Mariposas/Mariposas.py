mission = "To nurture the creativity, empathy, and critical thinking skills essential to thriving in a changing global environment."

#print(mission)

#print(len(mission))

words = mission.split(" ")
print(len(words))

char_count = len(mission)
print(char_count)

non_blank_char_count = 0
for character in mission:
    if character != "":
         #print(character)
         non_blank_char_count +=1
print(non_blank_char_count)

#How many times does the letter "e" appear in the mission statement?
e_in_mission_count = 0
for character in mission:
    if character == "e":
        #print(character)
        e_in_mission_count +=1
print(e_in_mission_count)   


filename = "./Mariposas/Mariposas.txt"
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        words = line.split(" ")
        print(words)
        print(len(words))


#global data
data = []
filename = "./Mariposas/Mariposas.txt"

def ReadFile():
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            data.append(line.strip())


#1 read the file
ReadFile()

#2 how many paragraphs?
paragraphcount = 0
for line in data:
    if line != " ":
        paragraphcount += 1
        #print(line)

#print(len(data))
print(paragraphcount)


#3 how many sentences?
sentencecount = 0
for line in data:
    sentences = line.split(".")
    for sentence in sentences:
        if sentence != "":
            #print(sentences)
            #print(len(sentences))
            sentencecount += 1
print(sentencecount)

#4 how many characters?
characterCount = 0
for line in data:
    #print(line)
    print(len(line))
    #characterCount += len(line)
print(characterCount)

#5 how many non blank characters?
non_blank_char_count = 0
commacount = 0
for line in data:
    for character in line:
        if character != " ":
            non_blank_char_count += 1
        if character == ",":
            commacount += 1
print(non_blank_char_count)
print(commacount)

#6 how many times did the word "Odilia appear in this article?"
#no hardcoding, answer is 9
odilia_count = 0
for line in data:
    words = line.split(" ")
    for word in words:
        if word == "Odilia":
            odilia_count += 1
print(odilia_count)