# Crypto Blockchain Audit Tool

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Web3.py](https://img.shields.io/badge/Web3.py-6.0-gold.svg)](https://web3py.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **security-focused auditing tool** for Ethereum Virtual Machine (EVM) compatible blockchains. This repository provides scripts to static analyze smart contract bytecode and detect common vulnerabilities patterns.

## 🚀 Features

- **Bytecode Analysis**: Scans compiled contract bytecode for known vulnerability signatures.
- **Vulnerability Detection**: Identifies potential issues like Re-entrancy guards missing, Delegatecall usage, and Zero-address checks.
- **Gas Usage Analysis**: Estimates transaction costs based on opcode distribution.
- **Report Generation**: Outputs audit findings in structured JSON format.
- **Network Agnostic**: Works with any EVM chain (Ethereum, BSC, Polygon).

## 📁 Project Structure

```
crypto-blockchain-audit-tool/
├── src/
│   ├── auditor.py        # Core analysis logic
│   └── main.py           # CLI Entrypoint
├── data/
│   └── contracts.json    # Sample contract data
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/crypto-blockchain-audit-tool.git

# Install
pip install -r requirements.txt

# Run Audit
python src/main.py --bytecode 0x608060405234801561001057600080fd5b5060...
```

## 📄 License

MIT License
