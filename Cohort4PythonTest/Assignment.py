
# QUETION 1 

# Given the two lists below,

student_name =  ["sandra", "patricia", "phiona", "Anitah"]
student_marks = [80, 56, 78, 90]
data = ["sandra",90,"kamwokya"]

print(student_name)

# 1 (a) A list that excludes the first and last items.

print(student_name[1:3])

# 1 (b) Add Masha at the 4th position.

student_name.insert(4,"masha")
print(student_name)

# 1 (c) Update the name phiona ensure the name is stored as phiona Alladinah.
student_name.remove("phiona")
print(student_name)
student_name.append("phiona Alladinah")
print(student_name)

# 1 (d) Display the length of the student_list.

list_length = len(student_name)
print(list_length)

# 1 (e) print all student_names using a for loop.

for name in student_name:
    print(name)

# 1 (f) Calculate the total marks of the student_marks variable.

    total_marks = sum(student_marks)
print(f"The total marks of students is {total_marks}")