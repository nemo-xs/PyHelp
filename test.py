import simplecrypt


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as pw:
    for password in pw.read().splitlines():
        print(password)
        try:
            info = simplecrypt.decrypt(password, encrypted).decode('utf8')
            break
        except simplecrypt.DecryptionException:
            pass
    print(info)


# if __name__ == '__main__':
#     main()
