from src.scanner import run_port_scanner
from src.dns import dns_lookup
from src.icmp import ping_host,test_loopback
from src.arp import show_arp_table



def main():

    while True:

        print("\n========== Network Security Toolkit ==========")
        print("1. TCP Port Scanner")
        print("2. DNS Lookup")
        print("3. Ping Host (ICMP)")
        print("4. View ARP Table")
        print("5. Test Local Network (Loopback)")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            run_port_scanner()

        elif choice == "2":

            host = input("Enter host: ")

            ip = dns_lookup(host)

            if ip:
                print(f"IP Address: {ip}")
            else:
                print("Host could not be resolved.")
        
        elif choice == "3":

            host = input("Enter host: ")

            ping_host(host)
        
        elif choice == "4":

            print("ARP Table:")
            show_arp_table()

        elif choice =="5":
            print("Testing Local Network (Loopback)...")
            test_loopback()

        elif choice == "6":
            print("Exiting Toolkit...")
            break

        else:
            print("Invalid Option!")
if __name__ == "__main__":
    main()