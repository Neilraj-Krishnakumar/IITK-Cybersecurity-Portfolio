import sys
import random
import time

def run_network_sensor():
    print("========================================================================")
    print("[BURP SUITE NODE]: Live Packet Interception Active")
    print("[DEVSECOPS TOOLING]: Simulating corporate Log Training Streams")
    print("====================================================================")
    print("SYSTEM PLATFORM NATIVE LAYER:", sys.platform)
    print("SENSOR ONLINE TIMESTAMP:",time.strftime("%H:%M:%S"))
    time.sleep(1)

    target_threat_vector = "192.168.1.50"
    total_packet_count = 0

    while total_packet_count < 5:
        total_packet_count = total_packet_count + 1
        system_time_stamp = time.strftime("%H:%M:%S") 

        captured_ip_node = "192.168.1." + str(random.randint(48, 52))
        print(f"\n[BURP FRAME {total_packet_count}]: SRC: {captured_ip_node} logged at {system_time_stamp}")

        if captured_ip_node == target_threat_vector:
            print("WARNING ENGINE : Malicious infrastructure block detected!")
            print("FIREWALL EXECUTOR : Terminating active session connections instantly.")
        else:
            print("ROUTING REPORT : Packet signature verified as clean.")

        time.sleep(0.5)
    
    print("-------------------------------------------------------------------------")
    print("STATUS: Burp Suite telemetry capture cycles completed.")
    print("Total system frames inspected: " + str(total_packet_count))
    print("======================================================================")

run_network_sensor()   





   
