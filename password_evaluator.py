import sys
import random
import time

def evaluate_password_strength():
    print("SYSTEM PLATFORM NATIVE LAYER:", sys.platform)
    print("AUDITOR CORE TIMESTAMP:", time.strftime("%H:%M:%S"))
    print("INITIALIZING ENTERPRISE CREDENTIAL AUDITING ENGINE")
    time.sleep(1)

    test_passwords_pool = ["12345", "PORTAL_USER", "SECURE_2026", "CYBERSHIELD#99"]
    records_audited = 0

    while records_audited < 5:
        records_audited = records_audited + 1
        system_timestamp = time.strftime("%H:%M:%S")

        current_target = random.choice(test_passwords_pool)
        print("AUDIT CYCLE", records_audited, "AT",system_timestamp, "| TESTING:", current_target)

        character_length = len(current_target)

        if character_length < 8:
            print("CRITICAL ERROR: Credentials length fails minimum 8-character threshold!")
            print("POLICY STATUS: REJECTED AND FLAGGED AS VULNERABLE.")
        else:
            print("VALIDATION PASS: Minimum length verified.")
            print("POLICY STATUS: APPROVED FOR ACCESS MATRIX LAYER.")

        time.sleep(1)
    print("CREDENTIALS POLICY INTEGRITY CHECK COMPLETED")
    print("Total unique access strings evaluated:", records_audited)

evaluate_password_strength()   

