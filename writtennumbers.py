"""Convert a number in base-10 into a written out number in English."""

def tensdigit(tens):
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
    return tens_word

def onesdigit(ones):
    if ones == 9:
        ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'
    return ones_word
    return teens

def oneandteen(tens, ones):

    if tens == 0:
        output = ones
    elif tens == 1:
        if ones == 1:
            output = 'eleven'
        elif ones == 2:
            output = 'twelve'
        elif ones == 3:
            output = 'thirteen'
        elif ones == 5:
            output = 'fifteen'
        else:
            output = onesdigit(ones) + 'teen'
    else:
        output = tensdigit(tens) + '-' + onesdigit(ones)
    return output




def main():
    num = int(input('A number between 1 and 99: '))

    tens = num // 10
    ones = num % 10

    teens = oneandteen(tens, ones)
    ones_word = onesdigit(ones)
    if tens == 1:
        print(teens)
    elif tens == 0:
        print(onesdigit(ones))
    else:
        ones_word = onesdigit(ones)
        tens_word = tensdigit(tens)
        print(tensdigit(tens) + "-" + onesdigit(ones))
main()
