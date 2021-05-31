import fidiscript

while True:
    text = input('FidiScript> ')
    result, error = fidiscript.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        print(result)
