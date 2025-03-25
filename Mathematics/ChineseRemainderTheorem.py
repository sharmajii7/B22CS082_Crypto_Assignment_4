# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
# Find the integer a such that x ≡ a mod 935

# Elementary algebra solution from Russian Wikipedia says that 
# to solve the system(finding x), you need to find solutions to the first,
# second and third equations separately (it is enough to find solutions that do not exceed 5*11*17 = 935).

# So I searched for a solution among numbers not greater than 935 that will solve all three given equations.

for x in range(5*11*17 + 1):
    if x%5 == 2 and x%11 == 3 and x%17 == 5:
        print(x)
        break