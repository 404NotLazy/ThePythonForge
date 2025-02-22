
def check_validity(card_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    reversed_card_number = card_number[::-1]

    odd_digits = reversed_card_number[::2]
    even_digits = reversed_card_number[1::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_even_digits + sum_of_odd_digits

    return total % 10 == 0

def main():
    card_number = '374245455400126'
    translation_table = str.maketrans({'-':'', " ":''})
    translated_card_number = card_number.translate(translation_table)

    if(check_validity(translated_card_number)):
        print("VALID!")
    else:
        print("INVALID!")
if __name__ == '__main__':
    main()
