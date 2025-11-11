# Lab 6 - Data Security and Encryption

- **Student ID:** 7702185
- **Name:** Alexandre VITTENET
- **Course:** Cybersecurity - Fall 2025
- **Instructor:** Asst. Prof. Essaid Meryam

## Language Used
- Python 3.12+

## Dependencies
- `hashlib` (built-in)
- `os` (built-in)
- `pycryptodome` (for Exercise 3 only)

### Installation
```bash
# Use a virtual environment
python3 -m venv venv
source venv/bin/activate
# Install pycryptodome to have Crypto.Random and Crypto.Cipher for ex3
pip install pycryptodome
```

## How to Run

### Exercise 1 - Caesar Cipher
```bash
python3 lab6_ex1.py
```
Tests substitution cipher with positive and negative shifts.

### Exercise 2 - SHA-256 Integrity Check
```bash
python3 lab6_ex2.py
```
Demonstrates file integrity verification and the avalanche effect.
Creates `data.txt` automatically if it doesn't exist.

### Exercise 3 - AES-GCM Encryption
```bash
python3 lab6_ex3.py
```
Demonstrates authenticated encryption with tampering detection.

## Files Included
- `lab6_ex1.py` - Caesar cipher implementation
- `lab6_ex2.py` - SHA-256 file integrity checker
- `lab6_ex3.py` - AES-GCM authenticated encryption
- `README.md` - This file
- `data.txt` - Sample file (generated automatically by Exercise 2)

## Notes
All exercises include color-coded output for better readability and demonstrate core cryptographic concepts as specified in Lecture 6.