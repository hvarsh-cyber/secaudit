import os
from scanner.vulnerability_scanner import VulnerabilityScanner

def main():
    # Get URL from environment variable or ask user
    target = os.getenv("TARGET_URL", None)
    
    if not target:
        target = input("Enter the URL to scan (e.g. https://example.com): ")
    
    scanner = VulnerabilityScanner(target)
    scanner.run_scan()

if __name__ == "__main__":
    main()