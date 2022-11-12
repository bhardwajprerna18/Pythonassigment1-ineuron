#!/usr/bin/env python
# coding: utf-8

# ## Assignment Part-1

# In[ ]:



get_ipython().set_next_input('Q1. Why do we call Python as a general purpose and high-level programming language');get_ipython().run_line_magic('pinfo', 'language')
Ans: Python is a general-purpose programming language, It is used in many popular fields like artificial intelligence, machine learning, etc. It is high level because it is human understandable.


get_ipython().set_next_input('Q2. Why is Python called a dynamically typed language');get_ipython().run_line_magic('pinfo', 'language')
Ans: Python is dynamically typed language because data type of variables is determined at run time. Due to dynamic typing, in Python the same variable can have a different type at different times during the execution.


get_ipython().set_next_input('Q3. List some pros and cons of Python programming language');get_ipython().run_line_magic('pinfo', 'language')
PROS                                                                              CONS
Python is easy to learn and read                                	Slower than compiled languages
Python has a vast collection of libraries                       	High memory consumption
Flexible and Extensible                                         	Complex multithreading
Large Community                                                 	Garbage collection leads to potential memory losses
Highly Scalable                                                 	Python is not so strong with mobile computing
IoT Opportunities                                               	Python can have runtime errors


get_ipython().set_next_input('Q4. In what all domains can we use Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans: Desktop Application Development, Web Application Development, DevOps, Web Scraping, Natural Language Processing, Machine Learning, artificial intelligence.

get_ipython().set_next_input('Q5. What are variable and how can we declare them');get_ipython().run_line_magic('pinfo', 'them')
Ans: Variables are name given to memory location, they are containers which store some values.
o	The first character of the variable can be an alphabet or (_) underscore.
o	Special characters (@, #, %, ^, &, *) should not be used in variable name.
o	Variable names are case sensitive. For example - age and AGE are two different variables.
o	Reserve words cannot be declared as variables.



Q6. How can we take an input from the user in Python?
Ans: By using input function.
User_input= input()

get_ipython().set_next_input('Q7. What is the default datatype of the value that has been taken as an input using input() function');get_ipython().run_line_magic('pinfo', 'function')
Ans: string

get_ipython().set_next_input('Q8. What is type casting');get_ipython().run_line_magic('pinfo', 'casting')
Ans: Converting one datatype into another is known as type casting.

get_ipython().set_next_input('Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why');get_ipython().run_line_magic('pinfo', 'why')
    Yes

get_ipython().set_next_input('Q10. What are keywords');get_ipython().run_line_magic('pinfo', 'keywords')
Ans: Keywords are reserved words. 


Q11. Can we use keywords as a variable? Support your answer with reason.
Ans: No, as interpreter gets confused whether it is a keyword or variable
     It will create ambiguity. 


get_ipython().set_next_input("Q12. What is indentation? What's the use of indentaion in Python");get_ipython().run_line_magic('pinfo', 'Python')
Ans: Indentation refers to the spaces at the beginning of a code line. Python uses indentation to indicate a block of code.

get_ipython().set_next_input('Q13. How can we throw some output in Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans: By using print function. 
     A= input(“enter your name”)
     Print(A)

get_ipython().set_next_input('Q14. What are operators in Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans: Python operators are used to perform operations on values and variables.
Arithmetic operators : are used to performing mathematical operations like addition, subtraction, multiplication, and division.
Comparison or Relational operators:  compares the values. It either returns True or False according to the condition.
Logical operators : perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.
Assignment operators: are used to assign values to the variables.


get_ipython().set_next_input('Q15. What is difference between / and // operators');get_ipython().run_line_magic('pinfo', 'operators')
Ans: / operator is used for float division.
     (/, operator, is, used, for, integer, division, or, floor, division.)
Eg. 5/2 = 2.5
    5//2 = 2


# In[9]:


#Q16. Write a code that gives following as an output.

#iNeuroniNeuroniNeuroniNeuron
print('iNeuron'*4)


# In[11]:


# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
number= int (input("enter the number"))
if number%2==0:
    print("even")
else:
    print("odd")


# In[ ]:


get_ipython().set_next_input('Q18. What are boolean operator');get_ipython().run_line_magic('pinfo', 'operator')
Ans: The logical operators and, or and not are also referred to as boolean operators. While and as well as or operator needs two operands, which may evaluate to true or false, not operator needs one operand evaluating to true or false.
get_ipython().set_next_input('Q19. What will the output of the following');get_ipython().run_line_magic('pinfo', 'following')

1 or 0  Ans: 1

0 and 0 And 0

True and False and True Ans: False

1 or 0 or 0 Ans: 1



# In[13]:


print( True and False and True)


# In[ ]:


get_ipython().set_next_input('Q20. What are conditional statements in Python');get_ipython().run_line_magic('pinfo', 'Python')
Ans: A conditional statement as the name suggests itself, is used to handle conditions in your program. These statements guide the program while making decisions based on the conditions encountered by the program.

Python has 3 key Conditional Statements that you should know:

if statement
if-else statement
if-elif-else ladder


get_ipython().set_next_input("Q21. What is use of 'if', 'elif' and 'else' keywords");get_ipython().run_line_magic('pinfo', 'keywords')
Ans: 1) if Statement:
The if statement is a conditional statement in python, that is used to determine whether a block of code will be executed or not. Meaning if the program finds the condition defined in the if statement to be true, it will go ahead and execute the code block inside the if statement.

Syntax:

if condition:
        # execute code block
2) if-else Statement:
As discussed above, the if statement executes the code block when the condition is true. Similarly, the else statement works in conjuncture with the if statement to execute a code block when the defined if condition is false.

Syntax:

Syntax:
if condition:
        # execute code if condition is true
else:
        # execute code if condition if False
3) if-elif-else ladder:
The elif statement is used to check for multiple conditions and execute the code block within if any of the conditions evaluate to be true.

The elif statement is similar to the else statement in the context that it is optional but unlike the else statement, there can be multiple elif statements in a code block following an if statement.

if condition1:
    # execute this statement
elif condition2:
    # execute this statement
.
.
else:
    # if non of the above conditions
    # evaluate to True
    # execute this statement


# In[15]:


# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
age= int(input("enter the age"))
if age>=18:
    print("I can vote")
else:
    print("I cant vote")


# In[50]:


#Q23. Write a code that displays the sum of all the even numbers from the given list. 
numbers = [12, 75, 150, 180, 145, 525, 50] 
even=numbers[::2]
sum=0
for i in even:
    sum+=i
    print(sum)
    


# In[51]:


#Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output
number1=int(input('enter the first number'))
number2=int(input('enter the second number'))
number3=int(input('enter the third number'))
if number1>number2 and number1>number3:
    print("greatest number is:" , number1)
elif number2>number1 and number2>number3:
    print('greatest number is:' , number2)
else:
    print('greatest number is:' , number3)


# In[53]:


#Q25. Write a program to display only those numbers from a list that satisfy the following conditions

#- The number must be divisible by five

#- If the number is greater than 150, then skip it and move to the next number

#- If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5==0 and i>150 and i>500:
        print(i)


# In[ ]:




