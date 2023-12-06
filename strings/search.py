def search(pat, txt):
    M = len(pat)
    N = len(txt)
    i = 0

    while i <= N - M:
        j = 0

        # For current index i, check for pattern match
        while j < M and txt[i + j] == pat[j]:
            j += 1

        if j == M:  # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print("Pattern found at index", i)
            i = i + M
        elif j == 0:
            i = i + 1
        else:
            i = i + j  # slide the pattern by j


# Driver program to test above function
def main():
    txt = ""  # Enter the entire string here
    pat = ""  # Enter the string to be searched here
    search(pat, txt)


if __name__ == "__main__":
    main()
