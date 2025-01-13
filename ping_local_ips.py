#Router export: Troubleshooting > Open in Broser
#import into Excel:  ="{""IP"":"""&C1&""",""name"":"""&A1&"""},"

import subprocess

import my_secrets


def ping_ips(ip_addresses):
    for ip in ip_addresses:
       # print(f"Pinging {ip['IP']}: {ip['name']}  ...")
        try:
            # Use `subprocess.run` to execute the ping command
            result = subprocess.run(
                ["ping", "-n", "1", ip['IP']],  # Use "-n" for Windows, "-c" for Unix-based systems
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )
            if result.returncode == 0:
                print(f"{ip['IP']}: {ip['name']} is reachable.\n")
            else:
                print(f"{ip['IP']}: {ip['name']} is NOT reachable.\n")
        except Exception as e:
            print(f"Error pinging {ip['ip']}: {ip['name']}: {e}\n")

# Example list of IP addresses
ip_addresses_unsorted = my_secrets.ip_addresses_unsorted

def get_ip_int(ip):
    host_id = ip.split(".",3)[3]
    hoist_id_int = int(host_id)
    return hoist_id_int
        
ip_addresses = sorted(ip_addresses_unsorted, key=lambda k: get_ip_int(k['IP']))

# Call the function
ping_ips(ip_addresses)
