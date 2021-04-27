import litpy

while True:
    text = input('litpy > ')
    result, error = litpy.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
