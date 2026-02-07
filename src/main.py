import argparse
import json
from src.auditor import SmartContractAuditor

def main():
    parser = argparse.ArgumentParser(description="Crypto Blockchain Audit Tool")
    parser.add_argument("--bytecode", help="Hex string of contract bytecode")
    parser.add_argument("--file", help="Path to file containing bytecode")
    
    args = parser.parse_args()
    
    bytecode = ""
    if args.bytecode:
        bytecode = args.bytecode
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                bytecode = f.read().strip()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return

    if not bytecode:
        print("Error: No bytecode provided. Use --bytecode or --file.")
        return

    auditor = SmartContractAuditor()
    print("--- Starting Audit ---")
    
    report = auditor.analyze_bytecode(bytecode)
    cost = auditor.estimate_deployment_cost(bytecode)
    
    print(f"Status: {report['status']}")
    print(f"Findings: {report['findings_count']}")
    print(f"Est. Deployment Gas: {cost}")
    
    if report['findings']:
        print("\nDetails:")
        print(json.dumps(report['findings'], indent=2))

if __name__ == "__main__":
    main()
