import sys
import random
import time

def execute_network_sentinel():
    print("SYSTEM PLATFORM NATIVE LAYER:", sys.platform)
    print("DIAGNOSTIC TRACK TIMESTAMP:", time.strftime("%H:%M:%S"))
    print("INITIALIZING CORE NETWORK INTEGRITY SENTINEL SYSTEM")
    time.sleep(1)

    active_nodes_pool = ["GATEWAY_ALPHA", "GATEWAY_BETA", "FIREWALL_MAIN", "DMZ_NODE_01"]
    scans_completed = 0

    while scans_completed < 5:
        scans_completed = scans_completed + 1
        syetem_timestamp = time.strftime("%H:%M:%S")

        selected_node = random.choice(active_nodes_pool)
        print("SENTINEL DIAGNOSTIC CYCLE", scans_completed, "AT", syetem_timestamp)
        print("TARGET SUITE NODE:", selected_node)

        simulated_latency = random.randint(15, 120)
        print("RESPONSE LATENCY:", simulated_latency, "MS")

        if simulated_latency > 90:
            print("DIAGNOSTIC STATUS: WARNING - HIGH LATENCY VECTOR DETECTED")

        else:
            print("DIAGNOSTIC STATUS: HEALTHY - OPTIMAL OPERATIONAL METRIC")

        time.sleep(1)

    print("CORE NETWORK SENTINEL OPERATIONS CYCLES COMPLETE")
    print("Total infrastructure nodes audited:", scans_completed)

execute_network_sentinel()

