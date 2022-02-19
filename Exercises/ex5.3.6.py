def fix_age(num):
    if num in range(13,20):
        if num not in (15,16):
            num = 0
    return num

def filter_teens(a,b,c):
    return (fix_age(a)+fix_age(b)+fix_age(c))


if __name__ == "__main__":
    print(filter_teens(2,13,1))