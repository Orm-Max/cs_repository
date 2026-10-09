# Lab 1, Task 1.1: Caesar cipher with one key (Romanian alphabet)

alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSŞTŢUVWXYZ"
lower = "aăâbcdefghiîjklmnopqrsştţuvwxyz"
n = 31

while True:
    print("")
    print("=== Task 1.1: Caesar cipher ===")
    mode = input("Operation (e - encrypt, d - decrypt, 0 - exit): ")

    if mode == "0":
        break

    if mode != "e" and mode != "d":
        print("Choose e, d or 0")
        continue

    while True:
        key_text = input("Key k (1..30): ")
        if key_text.isdigit() == False:
            print("The key must be an integer")
            continue
        k = int(key_text)
        if k < 1 or k > 30:
            print("The key must be between 1 and 30")
            continue
        break

    while True:
        text = input("Text: ")
        text2 = ""
        error = False

        for ch in text:
            if ch == " ":
                continue

            if ch in lower:
                position = lower.index(ch)
                ch = alphabet[position]
            if ch not in alphabet:
                print("Invalid character:", ch)
                error = True
                break
            text2 = text2 + ch

        if error == False:
            break

    result = ""
    for ch in text2:
        position = alphabet.index(ch)
        if mode == "e":
            new_position = (position + k) % n
        else:
            new_position = (position - k) % n
        result = result + alphabet[new_position]

    print("Result:", result)