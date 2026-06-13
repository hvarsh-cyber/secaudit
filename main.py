from scanner.vulnerability_scanner import VulnerabilityScanner

def main():
    # Target URL to scan
    target = input("Enter the URL to scan (e.g. https://example.com): ")
    
    # Create scanner and run
    scanner = VulnerabilityScanner(target)
    scanner.run_scan()

if __name__ == "__main__":
    main()