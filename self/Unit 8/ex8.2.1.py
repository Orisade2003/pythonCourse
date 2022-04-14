def update_string():
    """
    the function prints the needs string using formatting
    """
    data = ("self", "py", 1.543)
    format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"%data
    print(format_string)

def main():
    update_string()

if __name__ == '__main__':
    main()