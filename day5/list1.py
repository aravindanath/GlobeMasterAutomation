# student =[]  is a list
student =[]
print(type(student))
print("Intial blank list:",student)

student.append("Arvind")
student.append("Ramya")
student.append("Sirisha")
student.append("Shamlal")
student.append("Anjali")
student.append(345624)

print("List after addition:",student)


for i in range(101,115):
    student.append(i)

print("\nList after addition of elements from 101-115:")
print(student)

