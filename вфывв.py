import re
def word(string):
    new_string = re.sub(pattern=r'\b[0-1][0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9]\b', string=string,
                        repl='(TBD)')
    new_string = re.sub(pattern=r'\b[0-1][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]\b', string=new_string, repl='(TBD)')
    return new_string
def main():
    input = input()
    text = word(put)
    print(text)

if __name__ == '__main__':
    main()