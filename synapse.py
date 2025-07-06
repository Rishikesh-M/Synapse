import socket
import time
import sys


print("="*40)
print("    SYNAPSE - TCP Port Scanner")
print("        By Rishikesh M")
print("="*40)

if len(sys.argv) < 4:
    print("Usage: python synapse.py <target_ip> <start_port> <end_port> [timeout]")
    sys.exit(1)



protocol = 'tcp'

target = sys.argv[1]
start_p = int(sys.argv[2])
end_p = int(sys.argv[3])

if len(sys.argv) >= 5:
    timeout = float(sys.argv[4])
else:
    timeout = 1
def port_scan(ip, port, timeout):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))
        service = socket.getservbyport(port, protocol)
        print(f"[TCP] {port}  is Open → {service}")
    except:
        pass
for port in range(start_p, end_p):
    port_scan(target, port, timeout)
print("\u2705 Scan Completed Successfully...")