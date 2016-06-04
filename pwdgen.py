import sys

leet_dict = {'o': '0', 'i': '1', 'e': '3', 'a': '4', 's': '5',
             't': '7', 'b': '8'}

caps_dict = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
             '6': '6', '7': '*', '8': '*', '9': '(', '0': ')',
             '_': '-', '=': '+', ',': '<', '.': '>', '/': '?',
             ';': ':', "'": '"', '[': '{', ']': '}', '\\': '|',
             '`': '~'}

caps_freq = [1, 3, 5, 8, 13, 21, 34]


def caps(sentence):
    result = ''
    for i, c in enumerate(sentence):
        if i % 2 in caps_freq:
            result += caps_dict.get(c, chr(ord(c) - 32))
        else:
            result += c
    return result


def leet(sentence):
    result = ''
    for c in sentence:
        result = result + leet_dict.get(c, c)
    return result


def generate_password(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(' ', '')
    sentence = leet(sentence)
    sentence = caps(sentence)
    return sentence


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Please enter a sentence.')
    print(generate_password(sys.argv[1]))
