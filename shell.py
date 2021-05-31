import fidiscript

while True:
    text = input('litpy > ')
    result, error = litpy.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        print(result)
