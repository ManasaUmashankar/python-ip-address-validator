
import ipaddress


def validate_ip(ip):
    try:
        address = ipaddress.ip_address(ip)

        if address.is_loopback:
            ip_type = "Loopback"
        elif address.is_multicast:
            ip_type = "Multicast"
        elif address.is_private:
            ip_type = "Private"
        elif address.is_reserved:
            ip_type = "Reserved"
        elif address.is_global:
            ip_type = "Public"
        else:
            ip_type = "Special-purpose / Other"

        return {
            "valid": True,
            "ip": str(address),
            "version": address.version,
            "type": ip_type
        }

    except ValueError:
        return {
            "valid": False,
            "ip": ip,
            "version": None,
            "type": "Invalid"
        }
