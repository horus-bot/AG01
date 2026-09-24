# class Student :

#     def __init__(self):
#         print("hey this is to show how good the init fn is : ")


# class Student1 :
#     def __init__(self,name,roll_no,statement):
#         self.name = name
#         self.roll_no = roll_no
#         self.statement = statement

#     def greet(self):
#         print(self.name," is here ")

#     def tellRoll(self):
#         print(self.name," has the roll no : ",self.roll_no)

#     def speak(self):
#         print (self.statement)       
            

# harsh = Student1("harsh",24,"i hope you understand")   
# harsh.greet()
# harsh.tellRoll()
# harsh.speak()


 

class student:

    def __init__(self,name,roll_no):
        self.name = name 
        self.roll_no = roll_no

    def greet(self):
            print(self.name,"is here")


harsh = student("harsh",24)
harsh.greet()

yashwant = student("yashwant",12)
yashwant.greet()