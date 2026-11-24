
from src.validator import validate_ip

print("=" * 40)
print("       IP ADDRESS VALIDATOR")
print("=" * 40)

user_input = input("\nEnter IP addresses separated by commas: ")

if not user_input.strip():
    print("\nError: Please enter at least one IP address.")
    exit()

ip_list = user_input.split(",")

valid_count = 0
invalid_count = 0

print("\n========== VALIDATION REPORT ==========")

for ip in ip_list:

    ip = ip.strip()

    if not ip:
        continue

    result = validate_ip(ip)

    if result["valid"]:
        valid_count += 1

        print(
            result["ip"],
            "| IPv" + str(result["version"]),
            "|",
            result["type"]
        )

    else:
        invalid_count += 1
        print(ip, "| Invalid IP")

print("\n========== SUMMARY ==========")
print("Valid IP addresses:", valid_count)
print("Invalid IP addresses:", invalid_count)
print("Total checked:", valid_count + invalid_count)
