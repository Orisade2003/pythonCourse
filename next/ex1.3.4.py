def find_password(encrypted):
    return "".join(list(map(lambda x: chr((ord(x)+2)), encrypted)))

def main():
    print(find_password("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))

if __name__ == '__main__':
    main()