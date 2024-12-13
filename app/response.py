import os

def block_ip(ip):
    """
    Simulates blocking an IP address by adding it to iptables (or another firewall).
    This will only work on Linux-based systems with root access.
    """
    print(f"[*] Blocking IP: {ip}")
    # Simulating adding the IP to iptables
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    print(f"[!] IP {ip} blocked.")
