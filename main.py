def main():
    dir = "books/frankenstein.txt"
    with open(dir) as f:
        text = f.read().lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else: 
            chars[char] = 1
    print(f"--- Begin report of {dir} ---")
    print(f"{len(text.split())} words found in the document\n")
    for char in sorted(chars,reverse=True,key=lambda value: chars[value]):
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")
    print("--- End report ---")

main()