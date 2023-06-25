example_string="HeyDuBist___Cool"

def camel_to_snake(camel_str):
    snake_string=""
    for index,letter in enumerate(example_string):
        if letter.isalpha():
            if index == 0 and letter.isupper():
                snake_string+=letter.lower()
            if index != 0 and letter.islower():
                snake_string+=letter
            if index != 0 and letter.isupper():
                snake_string=snake_string+"_"+letter.lower()
        if not letter.isalpha() and letter == "_":
            pass
        if not letter.isalpha() and letter != "_":
            snake_string+=letter
    return snake_string

print(camel_to_snake(example_string))
