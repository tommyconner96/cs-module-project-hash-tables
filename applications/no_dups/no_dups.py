
cache = {}

def no_dups(s):
    split_str = s.split()

    if s in cache:
        return cache[s]

    for each in split_str:
        cache[each]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))



# understand
# input for no_dups is a string, seperated by spaces, only letters a- z
# output is a string, same order, but with dupes removed
# no extra spaces at end of returnd str