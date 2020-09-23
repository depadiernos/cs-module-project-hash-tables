import re

def no_dups(s):
    # Your code here
    table = set()

    split_s = re.split(' ', s)

    if s == "":
        return ""

    for word in split_s:
        if word not in table:
            table.add(word)
            if len(table) == 1:
                new_string = word
            else:
                new_string = new_string + f' {word}'
            
    return new_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))