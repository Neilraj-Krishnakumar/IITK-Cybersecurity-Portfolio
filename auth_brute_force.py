import sys
import random
import time

def simulate_auth_sentinel():
    print("SYSTEM PLATFORM NATIVE LAYER:", sys.platform)
    print("SENTINEL WATCH TIMESTAMP:", time.strftime("%H:%M:%S"))
    print("INITIALIZING SECURE PORTAL AUTHENTICATION SENTINEL")
    time.sleep(1)

    target_access_string = "SECURE_GATEWAY_2026"
    active_attempts_count = 0
    system_access_granted = False

    while active_attempts_count < 5 and not system_access_granted:
        active_attempts_count = active_attempts_count + 1
        system_timestamp = time.strftime("%H:%M:%S")

        possible_keys = ["GUEST_PASS", "ADMIN_123", "SECURE_GATEWAY_2026", "ROOT_ACCESS"]
        generated_attempt_string = random.choice(possible_keys)

        print("SENTINEL AUDIT: EVALUATING AUTHENTICATION FRAME " + str(active_attempts_count) + "AT" + system_timestamp)
        print("  [EVALUATED STRING DATA] : " + generated_attempt_string)

        if generated_attempt_string == target_access_string:
            print(" STATUS ENGINE REPORT: MATCH FOUND. ACCESS GRANTED TO SYSTEM ARCHITECTURE. ")
            system_access_granted = True
        else:
            print(" STATUS ENGINE REPORT: INVALID CREDENTIALS. MALICIOUS VECTOR BLOCKED ")

        time.sleep(1)
    
    print("PORTAL SECURITY WATCH CYCLES COMPLETED")
    print("Total transaction authorization logs processed: " + str(active_attempts_count))
    simulate_auth_sentinel()