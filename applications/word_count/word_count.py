

def word_count(s):
    d = {}
    result = s.lower()
    words = result.split()
    illegal_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
                     '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    for i in illegal_chars:
        result = result.replace(i, '')
        words = result.split()

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
