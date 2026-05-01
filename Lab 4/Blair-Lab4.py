# Rivets Arm His Lama Den
#
# Team Name: Borq
# Members: Hailey Allman, Sadie Ann, Blair Bourque, McKinley Humble, Isaiah Thigpen
#
# Decodes messages from the text files encoded in RSA

import sys
import math

# ------------- Factor a number into the product of 2 primes ------ #
def factor(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            p = i
            q = n // i
            if is_prime(p) and is_prime(q):
                return p, q
    return None, None

# ------------ Determine if the number is prime ---------------- #
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# ----------------- Calculate GCD --------------------- #
def calculate_gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

# ----------------- Generate Candidate values of e ----------------- #
def generate_e_values(z):
    # Generates e values of the form 2^k + 1 where 1 < e < z
    e_list = []
    k = 1
    while True:
        e = (2**k) + 1
        if e >= z:
            break
        # e must be coprime to z to have a modular inverse
        if calculate_gcd(e, z) == 1:
            e_list.append(e)
        k += 1
    return e_list

# ----------------- Naively calculate d ----------------- #
def calculate_d(e, z):
    # Find d such that (d * e) % z = 1
    # We iterate until we find the smallest positive d
    d = 1
    while (d * e) % z != 1:
        d += 1
        # Safety break if no inverse is found within a reasonable range
        if d > z:
            return None
    return d

# ----------------- Decrypt Ciphertext ----------------- #
def decrypt(C, d, n):
    plaintext = ""
    for c in C:
        # Decrypt c with K_priv: m = c^d mod n
        m = pow(c, d, n)
        # Convert to ASCII character[cite: 5]
        plaintext += chr(m)
    return plaintext

def main():
    # Read n and the list of ciphertexts from stdin[cite: 5]
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return

    n = int(input_data[0].strip())
    # Convert comma separated string into a list of integers[cite: 5]
    C = [int(x.strip()) for x in input_data[1].split(',') if x.strip()]

    # Factor n into p and q[cite: 5]
    p, q = factor(n)
    
    # Calculate z = lcm(p-1, q-1)[cite: 5]
    # Formula: ((p-1)*(q-1)) / gcd(p-1, q-1)[cite: 5]
    z = ((p - 1) * (q - 1)) // calculate_gcd(p - 1, q - 1)

    print(f"p={p}, q={q} n={n} z={z}")

    # Generate candidate e values[cite: 5]
    e_values = generate_e_values(z)

    for e in e_values:
        d = calculate_d(e, z)
        print(f"Trying e={e} d={d}")
        print(f"Public key: ({e}, {n})")
        print(f"Private key: ({d}, {n})")

        # Attempt to decrypt and print
        try:
            result = decrypt(C, d, n)
            # Basic validation: ensure characters are printable/reasonable[cite: 5]
            # If invalid, the prompt logic implies trying the next e[cite: 5]
            if all(32 <= ord(char) <= 126 or char in "\n\r\t" for char in result):
                print(result)
                break
            else:
                print("ERROR: invalid plaintext.")
        except Exception:
            print("ERROR: invalid plaintext.")

if __name__ == "__main__":
    main()