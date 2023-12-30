import re
def srh_pr(string):
    return re.findall(pattern=r'\b[АВЕКМНОРСТУХABEKMHOPCTY]\d{3}[АВЕКМНОРСТУХABEKMHOPCTY]{2}\d{2,3}\b', string=string)
def srh_tx(string):
    return re.findall(pattern=r'\b[АВЕКМНОРСТУХABEKMHOPCTY]{2}\d{5,6}\b', string=string)
def maches(string, private, taxi):
    ret_string = ''
    for number in string.split():
        if number in private:
            ret_string += 'Частный номер'
        elif number in taxi:
            ret_string += 'номер такси '
        else:
            ret_string += 'Не номер '
    return ret_string


def main():
    put = input()
    mch_private = srh_pr(put)
    mch_taxi = srh_tx(put)
    print(maches(put, mch_private, mch_taxi))
if __name__ == '__main__':
    main()