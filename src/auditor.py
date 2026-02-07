import re

class SmartContractAuditor:
    def __init__(self):
        # Vulnerability signatures (Simplified Opcode patterns)
        self.signatures = {
            "DELEGATECALL_UNSAFE": r"f4", # Opcode for DELEGATECALL
            "SELFDESTRUCT": r"ff",       # Opcode for SELFDESTRUCT
            "TX_ORIGIN_USAGE": r"32",    # Opcode for ORIGIN (tx.origin)
        }

    def analyze_bytecode(self, bytecode: str) -> dict:
        """
        Analyzes raw hex bytecode for vulnerability patterns.
        Note: This is a static analysis heuristic, not a full formal verification.
        """
        bytecode = bytecode.lower().replace("0x", "")
        findings = []

        for name, pattern in self.signatures.items():
            if re.search(pattern, bytecode):
                findings.append({
                    "type": name,
                    "severity": "HIGH" if name == "SELFDESTRUCT" else "MEDIUM",
                    "description": f"Detected potential usage of {name} opcode."
                })
        
        # Check for zero address hardcoded (common heuristic)
        if "0000000000000000000000000000000000000000" in bytecode:
             findings.append({
                "type": "ZERO_ADDRESS_REF",
                "severity": "LOW",
                "description": "Hardcoded zero address found."
            })

        return {
            "findings_count": len(findings),
            "findings": findings,
            "status": "VULNERABLE" if findings else "CLEAN"
        }

    def estimate_deployment_cost(self, bytecode: str) -> int:
        """Rough estimation of gas cost based on bytecode length."""
        # Clean bytecode
        bytecode = bytecode.replace("0x", "")
        length = len(bytecode) / 2 # Bytes
        
        # Base cost 21000 + 200 per byte (approx for deployment info)
        return 21000 + (int(length) * 200)
