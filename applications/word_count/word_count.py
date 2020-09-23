import re

def word_count(s):
    # Your code here

    table = {}

    ignore_list = '" : ; , . - + = / \\ | [ ] { } ( ) * ^ &'
    s = s.lower()
    str = re.split(' |\r|\t|\n', s)

    for word in str:
        new = word.strip(ignore_list)
        if new != "":
            if new not in table:
                table[new] = 1
            else:
                table[new] += 1
    return table
    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))