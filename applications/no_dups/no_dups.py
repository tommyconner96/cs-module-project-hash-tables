
def no_dups(s):
    split_str = s.split()
    word_list = {}
    # new_str = ''

    for word in split_str:
        # new_str = ' '.join(map(str, word_list))
        if word not in word_list:
            word_list[word] = 1
        else:
            pass
    return ' '.join(map(str, word_list))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
