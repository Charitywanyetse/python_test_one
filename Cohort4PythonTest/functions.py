# # # Example
#Create a function that returns the main components of a functions in python.
def function_basics():
     print(f"The main components of functions are : \n function body \n function parameter")

function_basics()

 #Create a function that returns your student name,regestration number and student age.

def student_information():
    student_name = "Charity"    # local variables
student_regestration_number = "2024/DSC/0103/SS"  # local variables
student_age = "21" # local variables
print(f"My name is {student_name}my regestration number is {student_regestration_number} and am {student_age}")
student_information()

# # # Create a function that returns your student name ,regestration number and age as parameters.

# def student_details(name, age, reg_no):
#      print(f"{name}, {age}, {reg_no}")


# # student_details("charity","21","2024/DSC/0103/SS")

# # #RETURN VALUES
# # # It also works as a print function.

# # def my_name ():
# #     return "Charity"

# # my_name ()

# # # approach2
# def name():
#      name = "Charity"
#      return name

# # name()


# # OR

 #def her_name(name):
    print(f"{name}")

#her_name("glorious")

#def my_age():
 #    age = 21
 #    return age

#print(f"my name is {my_name_approach2}")

    # Create a function that calculate the area of a triangle.
    # The base and height must be function parameters.

#def area_of_triangle(base, height):
#     area =int( 1/2*base*height ) 
#     print(f"The area of a triangle of base: {base} and height: {height} is {area}")

#area_of_triangle(3 , 4 )

# Approach2

#def area_of_triangle():
 #    base = int(input("Enter the base of a triangle: "))
  #   height = int(input("Enter the height of a triangle: "))
   #  area =int( 1/2 * base * height) 
    # print(f"The area of a triangle with base: {base} and height: {height}is {area}")
     
#area_of_triangle()