def validate_credit_card(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 19:
        return False

    # luhn Algorithm https://en.wikipedia.org/wiki/Luhn_algorithm
    reverse_digits = card_number[::-1]
    total = 0

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0


card_number = "4539 1488 0343 6467"

print(f"The card is valid: {validate_credit_card(card_number)}")

card_number = "4539 1488 0343 6463"
print(f"The card is valid: {validate_credit_card(card_number)}")
