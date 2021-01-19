def digits_to_words(input_string):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    digit_string = ''
    for i in input_string:
        if i in digits:
            if i == '1':
                char = 'one '
            elif i == '2':
                char = 'two '
            elif i == '3':
                char = 'three '
            elif i == '4':
                char = 'four '
            elif i == '5':
                char = 'five '
            elif i == '6':
                char = 'six '
            elif i == '7':
                char = 'seven '
            elif i == '8':
                char = 'eight '
            elif i == '9':
                char = 'nine '
            else:
                char = 'zero '
            digit_string += char
    digit_string = digit_string[:-1]

    return digit_string
    
def to_camel_case(underscore_str):
    if '_' not in underscore_str:
        return underscore_str

    input_str = list(underscore_str.lower())
    first = True

    for i in range(len(input_str)):
        if input_str[i] == '_':
            input_str[i] = ''
            if i == len(input_str)-1:
                break
            if input_str[i+1] != '_':
                if first == True:
                    first = False
                    continue
                input_str[i+1] = input_str[i+1].upper()
        else:
            first = False

    camelcase_str = ''.join(input_str)

    return camelcase_str