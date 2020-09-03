def no_dups(s):
    # Your code here
    s_dict = {}
    s = s.split()
    for string in s:
        if string in s_dict.keys():
            continue
        else:
            s_dict[string] = 1
    s = " "
    s = s.join(s_dict)
    return s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))