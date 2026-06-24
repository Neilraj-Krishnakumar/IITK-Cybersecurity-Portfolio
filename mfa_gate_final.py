import random
import time

print("=============================================================")
print("[DEVSECOPS INSIGHT]: Automated Token Verification Active")
print("[PERIMETER NODE]: Multi-Factor Authentication Entry Gate")
print("===========================================================")

username = input("Enter admin username: ")
security_password = input("Enter security password: ")
security_pin = input("Enter security pin: ")

num1 = random.randint(20, 80)
num2 = random.randint(20, 80)
expected_sum = num1 + num2

print("\n[ALERT]: Anti-Automation Token Required to bypass proxy checks.")
math_challenge = input(f"SECURITY MATH CHALLENGE: What is {num1} + {num2}? ")

identity_check = (username == "Neilraj Krishnakumar")
password_check = (security_password == "Swami@1234")
pin_check = (security_pin == "1234")
math_check = (math_challenge == str(expected_sum))

print("\n------------------------------------------------------------------")
if identity_check and password_check and pin_check and math_check:
    print("STATUS: ACCESS GRANTED. National Infrastructure Portal Unlocked.")
    print("LOG: Gateway session initialized under secure compliance parameters.")
else:
    print("STATUS: ACCESS DENIED. Authentication Failure.")
    print("LOG: Connection securely terminated by Layer 1 Perimeter Sentinel.")
print("================================================================")
