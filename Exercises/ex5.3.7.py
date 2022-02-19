def chocolate_maker(small, big, x):
    if type(x) is int:
        if x<=small:
            return True
        if(x-small)%5 == 0:
            if(x-small)//5 <= big:
                return True
        if(x%5==0 and x//5<=big):
            return True
    return False



if __name__ == "__main__":
    print(chocolate_maker(3,2,10))
