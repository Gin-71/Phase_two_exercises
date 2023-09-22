def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])[-2][0]
    print(f"this is letter {letter}")
    print(f"this are the items in counter{counter.items()}")
    print(f"this is the sorted{sorted(counter.items(), key=lambda item: item[1])}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
