subject = ["C","C++","Java","Python","Basic","C","C"]
print(subject)
print(subject+[29,"Shuvo","CSE"])
print(subject*3) #print three time
print("Python" in subject)

print(len(subject))
subject.append("TOC") #add item in last
print(subject)

subject.insert(2,"OS") # insert os in 2 index
print(subject)

subject.remove("Java")
print(subject)

subject.sort()
print(subject)

subject.reverse()
print(subject)

subject.pop()
print(subject)

position = subject.index("C")
print(position)

cunt = subject.count("C")
print(cunt)

subject2 = subject.copy()
print(subject2)

subject.clear()
print(subject)