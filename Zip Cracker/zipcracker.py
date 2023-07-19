import zipfile
# pass.txt is demo file which contain some password put path of your password file instead
password_file = "E:\PYTHON\Rakshak\pass.txt"
# protected.zip is demo zip file having one file with password "admin" put your full path of zip file
zip_file = "E:\PYTHON\Rakshak\protected.zip"
zip = zipfile.ZipFile(zip_file)


def crack_password(password_file,zip):
    index = 0

    with open(password_file,'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    index+=1
                    zip.extractall(pwd=word)
                    print("Password Found at line ",index)
                    print("Password is : ",word.decode())
                    return True
                except:
                    continue
    return False

crack_password(password_file,zip)