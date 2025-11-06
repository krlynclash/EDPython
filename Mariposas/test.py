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


filename = "./Mariposas.txt"
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print(line)

    for words in "./Mariposas.txt":
        words = "./Mariposas.txt".split(" ")
        print(words)
        print(len(words))