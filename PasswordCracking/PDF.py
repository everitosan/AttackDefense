import PyPDF2
from dictionary import generate_dict


def main():
    file = PyPDF2.PdfFileReader("files/secret.pdf")
    dict = generate_dict(
        ["a", "b", "c", "d", "e", "1", "2", "3", "4", "5"],
        length=6
    )
    print("Trying password: ")
    for opt in dict:
        print(" "*50, end="\r", flush=True)
        print(opt, end="\r", flush=True)
        isOK = file.decrypt(opt)
        if isOK:
            print("Found key: {}".format(opt))
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye!")
