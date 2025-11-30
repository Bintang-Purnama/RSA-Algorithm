# RSA-Algorithm
The Besat way to learn something is by practicing . So my Teacher asked us to make RSA-Algorithm that we can really use to encrypt and decrypt a massage

In This Code u can use it to decrypt and encrypt a massage , it will show you the key and the result . when you run the code it will show you a multiple choice 

This project is a Python implementation of the **RSA (Rivest–Shamir–Adleman)** cryptography algorithm. It is built **from scratch** without relying on external cryptography libraries, designed to demonstrate the mathematical logic behind Public Key Cryptography.

## 🚀 Key Features
* **Automatic Key Generation:** Generates Public and Private Key pairs using random prime numbers.
* **Efficient Prime Validation:** Uses the optimized $O(\sqrt{n})$ trial division method (`i * i <= n`) to verify prime numbers.
* **Text Support:** Automatically converts text input (String) into numbers (ASCII) for encryption.
* **Interactive CLI:** A user-friendly command-line interface menu.
* **Modular Exponentiation:** Utilizes Python's `pow()` for efficient calculation of large number powers.

## 📋 Prerequisites
* **Python 3.x** installed on your machine.
* No external modules are required (standard libraries `random` and `math` are used).

## 🛠️ How to Run

1.  **Download** the script (e.g., `rsa_program.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the file.
4.  Run the following command:
    ```bash
    python rsa_program.py
    ```
5.  Follow the on-screen menu:
    * The program generates keys automatically upon launch.
    * Select **1** to encrypt a text message.
    * Select **2** to decrypt the previously encrypted message.
    * Select **3** to regenerate a new pair of keys.

## 🧠 Mathematical Concepts Used

This program implements the core RSA formulas:

### 1. Key Generation
* **Modulus ($n$):** $n = p \times q$ (Where $p$ and $q$ are distinct random primes).
* **Totient ($\phi$):** $\phi(n) = (p-1) \times (q-1)$.
* **Public Key ($e$):** Selected such that $1 < e < \phi(n)$ and $gcd(e, \phi(n)) = 1$.
* **Private Key ($d$):** Calculated using the Modular Multiplicative Inverse, such that $(d \times e) \equiv 1 \pmod{\phi(n)}$.

### 2. Encryption & Decryption process
* **Encryption:** $C = M^e \pmod n$
* **Decryption:** $M = C^d \pmod n$

> **Technical Note:** The program uses Python's built-in `pow(base, exp, mod)` function. This implements **Modular Exponentiation**, allowing the program to compute large powers efficiently without causing memory overflow.

## ⚠️ Disclaimer
This program is for **educational purposes only**. The prime numbers generated are deliberately kept small (range 10-300) to ensure the program runs instantly for demonstration. Secure, production-grade RSA requires prime numbers with hundreds of digits (e.g., 2048-bit keys).

---
**Created by:** Bintang Surya Purnama
**Course:** Data Security
