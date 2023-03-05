import whois
import sys

def print_header(domain_name):
    print(f"## Domain information for `{domain_name}`:\n")

def print_field(field_name, field_value):
    print(f"- {field_name}: {field_value}")

def print_list_field(field_name, field_values):
    print(f"- {field_name}:")
    for value in field_values:
        print(f"  - {value}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python osint.py <domain_name>")
        return
    
    domain_name = sys.argv[1]

    try:
        domain_info = whois.whois(domain_name)
    except whois.exceptions.WhoisError as e:
        print(f"Error: {e}")
        return
    
    print_header(domain_name)
    print_field("Registrar", domain_info.registrar)
    print_field("Creation date", domain_info.creation_date)
    print_field("Expiration date", domain_info.expiration_date)
    print_field("Last updated", domain_info.last_updated)
    print_list_field("Name servers", domain_info.name_servers)
    print_list_field("Status", domain_info.status)
    print_list_field("Emails", domain_info.emails)
    print_field("DNSSEC", domain_info.dnssec)

if __name__ == "__main__":
    main()
