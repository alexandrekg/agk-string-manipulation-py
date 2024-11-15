
def main():
    full_name = str(input("Please enter your full name: "))
    print(f"Your name in uppercase: {full_name.upper()}")
    print(f"Your name in lowercase: {full_name.lower()}")
    print(f"Total number of characters: {len(full_name)}")
    print(f"Your name reversed: {full_name[::-1]}")


if __name__ == "__main__":
    main()