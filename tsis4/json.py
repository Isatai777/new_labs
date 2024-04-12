import json

try:
    with open("C:/Users/OMATA/Desktop/pp2/tsis4/sample-data.json", 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

interfaces = data.get("interfaces", [])

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    dn = interface.get("DN", "")
    description = interface.get("Description", "")
    speed = interface.get("Speed", "")
    mtu = interface.get("MTU", "")
    print("{:<50} {:<20} {:<10} {:<6}".format(dn, description, speed, mtu))

total_interfaces = len(interfaces)
print("\nTotal interfaces:", total_interfaces)