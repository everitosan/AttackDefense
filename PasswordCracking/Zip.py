import zipfile
from dictionary import generate_dict
from unzipper import brute_open


def main():
    dict = generate_dict(
        alph=["a", "b", "c", "d", "e", "1", "2", "3", "4", "5"],
        length=6
    )
    brute_open("files/secret.zip", dict)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye bye!")
