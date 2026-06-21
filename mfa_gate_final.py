import random 

username = input("Enter username : ")
security_password = input("Enter security password : ")
security_pin = input("Enter security pin : ")

num1 = random.randint(20, 80)
num2 = random.randint(20, 80)
expected_sum = num1 + num2
math_challenge = input("SECURITY MATH CHALLENGE : What is " + str(num1) + " + " + str(num2) + "? ")

identity_check = (username == "Neilraj Krishnakumar")
password_check = (security_password == "Swami@1234")
pin_check = (security_pin == "1234")
security_math_check= (math_challenge ==  str(expected_sum))

if identity_check and pin_check and password_check and security_math_check :
	print("ACCESS GRANTED : National Infrastructure Portal Open")
else :
	print("ACCESS DENIED : Authentication Faliure . Connection Terminated")
