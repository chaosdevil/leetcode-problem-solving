from time import time

def to_roman(value: int):
    romans = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for pair in romans:
        while value >= pair[0]:
            result += pair[1]
            value -= pair[0]

    return result

if __name__ == "__main__":
    start = time()
    for i in range(1, 3001):
        print(f"{i} {to_roman(i)}")
    print()
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")


