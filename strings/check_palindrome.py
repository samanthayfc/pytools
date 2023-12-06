def is_palindrome(s):
    # Start from leftmost and rightmost corners of the string
    l, h = 0, len(s) - 1

    # Keep comparing characters while they are the same
    while h > l:
        if s[l] != s[h]:
            print(s, "is not a Palindrome")
            return
        l += 1
        h -= 1

    print(s, "is a palindrome")


# Driver program to test the function
def main():
    s = input("Enter a string: ")
    is_palindrome(s)


if __name__ == "__main__":
    main()
