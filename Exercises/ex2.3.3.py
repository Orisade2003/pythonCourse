def threeLittlePigs():
    bricks = input("Enter 3 digits, Each  digit represents the number of bricks a single pig has")
    allBricks = int(bricks)%10 + (int(bricks)//10 % 10) + (int(bricks)//100)
    print(allBricks)
    print(int(allBricks)//3)
    remainderBricks = int(allBricks)%3
    print(remainderBricks)
    print(remainderBricks == 0)

if __name__ == '__main__':
    threeLittlePigs()