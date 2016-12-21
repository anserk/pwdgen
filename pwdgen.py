import sys

leet_dict = {'o': '0', 'i': '1', 'e': '3', 'a': '4', 's': '5',
             't': '7', 'b': '8'}

caps_dict = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
             '6': '6', '7': '*', '8': '*', '9': '(', '0': ')',
             '_': '-', '=': '+', ',': '<', '.': '>', '/': '?',
             ';': ':', "'": '"', '[': '{', ']': '}', '\\': '|',
             '`': '~'}

vows = ['a', 'e', 'i', 'o', 'u']


def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b


def add_website_suffix(website):
    if not website:
        return ''
    return '@{}'.format(''.join([c for c in website.lower()
                                if c not in vows]))


def caps(sentence):
    return ''.join([caps_dict.get(c, chr(ord(c) -32))
                    if i % 2 in fib()
                    else c
                    for i, c in enumerate(sentence)])


def leet(sentence):
    return ''.join([leet_dict.get(c, c) for c in sentence])


def generate_password(sentence, website=''):
    return '{}{}'.format(caps(leet(sentence.lower().replace(' ', ''))),
                    add_website_suffix(website))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Please enter a sentence.')
    if len(sys.argv) == 3:
        print(generate_password(sys.argv[1], sys.argv[2]))
    else:
        print(generate_password(sys.argv[1]))
