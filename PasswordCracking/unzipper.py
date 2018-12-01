import zipfile
import os
import shutil


def create_destination_dir(dir_name):
    dir = os.path.dirname(__file__)
    dest_dir = os.path.join(dir, dir_name)
    print("Creating destination:")
    print(dest_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)


def brute_open(file="secret.zip", dictionary=[]):
    """
        [file]          should indicate the path to the file
        [dictionary]    is a list of strings with the possible passwords
    """
    file = zipfile.ZipFile(file, mode="r")
    extract_dir_name = file.filename.replace(".", "_")
    key_found = False
    create_destination_dir(extract_dir_name)
    content = file.namelist()
    print(content)
    print("Trying password:")
    for opt_pass in dictionary:
        print(" "*50, end="\r", flush=True)
        print("{}".format(opt_pass), end="\r", flush=True)
        try:
            bytes_pwd = bytes(opt_pass, "utf-8")
            file.extractall(path=extract_dir_name, pwd=bytes_pwd)
            print("Found: {}".format(opt_pass))
            key_found = True
            break
        except:
            pass
    if not key_found:
        print("Password not found")
        shutil.rmtree(path=extract_dir_name)
