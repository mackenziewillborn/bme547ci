def main():
    s = input("Input: ")
    ans = is_tachycardic(s)

    print("The input contains the word 'tachycardic': {}".format(ans))


def is_tachycardic(s):
    str = s.lower()
    string = str.replace(" ", "")

    if string.find("tachycardic") == -1:
        p = False
        return p
    else:
        p = True
        return p

if __name__ == "__main__":
    main()
