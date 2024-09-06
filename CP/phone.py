def words_to_digits(s):
    words_to_digits_mapping = {'zero':'0',
        'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine': '9'
    }

    digits = ''
    i = 0

    while i < len(s):
        current_word = s[i]

        if current_word == 'double':
            repeated_digit = s[i + 1]
            digits += words_to_digits_mapping[repeated_digit] * 2
            i += 2
            continue
        elif current_word == 'triple':
            repeated_digit = s[i + 1]
            digits += words_to_digits_mapping[repeated_digit] * 3
            i += 2
            continue
        else:
            digits += words_to_digits_mapping[current_word]
        i += 1

    return digits

# Example usage:
s = "nine double three five one five four zero double nine"
result = words_to_digits(s.split())
print(result)
