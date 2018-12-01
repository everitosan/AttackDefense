from unzipper import brute_open


def main():
    passwords = []
    with open("dictionary.txt", mode="r") as pwds:
        for pwd in pwds.readlines():
            _pwd = pwd.replace("\n", "")
            passwords.append(_pwd)

    brute_open("files/PDF.zip", passwords)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye!")
