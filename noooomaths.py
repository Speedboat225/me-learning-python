# There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?

tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 96
tree5 = 11

sum = tree1 + tree2 + tree3 + tree4 + tree5

print(sum)

avg = sum/5

print(avg)

# Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?

maths = 40
science = 70
hindi = 50
english = 60

sum2 = maths + science + hindi + english

print(sum2)

pcnt = (sum2/400) * 100

print(pcnt)

# Write a program to calculate the number of notes in the given amount?

amount = int(input("hi pls enter smth thx\n"))

note1=amount//500#5 notes of hundreds
note2=(amount%100)//50
note3=((amount%100)%50)//10

print(note1, note2, note3)
