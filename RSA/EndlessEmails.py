import gmpy2
from Crypto.Util import number
from itertools import combinations

def load_output():
    """
    Loads data from output.txt file containing n and c values.
    Returns a dictionary with lists of integers for 'n' and 'c'.
    """
    ret = {'n': [], 'c': []}  # Initialize dictionary with empty lists for n and c
    
    # Use text mode with 'r' instead of 'rb' since we're decoding
    with open("output.txt", 'r') as fd:
        for line in fd:  # Iterate line by line more efficiently
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            try:
                k, v = line.split('=', 1)  # Split only on first '=' occurrence
                k = k.strip()
                if k == 'e':  # Skip lines with 'e'
                    continue
                ret[k].append(int(v))  # Convert value to int and append
            except (ValueError, KeyError):
                continue  # Skip malformed lines gracefully
                
    return ret

def decrypt(grps, e):
    """
    Attempts to decrypt ciphertexts using Chinese Remainder Theorem.
    Args:
        grps: dict containing lists of moduli (n) and ciphertexts (c)
        e: encryption exponent (typically 3 in this case)
    """
    # Pre-compute combinations once
    group_combinations = combinations(zip(grps['n'], grps['c']), e)
    
    for grp in group_combinations:
        # Calculate product of all n values (N) using multiplication
        N = 1
        for n, _ in grp:
            N *= n

        # Apply Chinese Remainder Theorem
        M = 0
        for n, c in grp:
            Ni = N // n  # Partial product
            inv = number.inverse(Ni, n)  # Modular inverse
            M += c * Ni * inv
        M %= N  # Reduce modulo N

        # Attempt to find eth root
        m, exact = gmpy2.iroot(M, e)  # Changed to iroot (faster than root)
        if exact:  # If we found an exact root
            print(number.long_to_bytes(int(m)))  # Convert to bytes and print

def main():
    """Main execution function"""
    grps = load_output()
    decrypt(grps, 3)

if __name__ == "__main__":
    main()