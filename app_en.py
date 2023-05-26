# Basic Definition for arrays that store grades :)
grades = input("Type your grades : ")
newArray = grades.split(" ")
#loop to change every entry in array to int
for i in range(len(newArray)):
    newArray[i] = int(newArray[i])
#print function to calculate average grade :0
print("Your Grade average : ", (sum(newArray) / len(newArray)))