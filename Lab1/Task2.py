# Lab 1, Task 1.2: Caesar cipher with keyword (Romanian alphabet)

alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSŞTŢUVWXYZ"
n = 31

while True:
    print("")
    print("=== Task 1.2: Caesar cipher with keyword ===")
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
        word = input("Keyword (at least 7 letters): ")
        keyword = ""
        error = False

        for ch in word:
            if ch == " ":
                continue
            ch = ch.upper()
            if ch == "Ș":
                ch = "Ş"   
            if ch == "Ț":
                ch = "Ţ"             
            if ch not in alphabet:
                print("Invalid character:", ch)
                error = True
                break
            keyword += ch

        if error == True:
            continue
        if len(keyword) < 7:
            print("Keyword is too short, need at least 7 letters")
            continue
        break

    new_alphabet = ""
    for ch in keyword:
        if ch not in new_alphabet:
            new_alphabet += ch
    for ch in alphabet:
        if ch not in new_alphabet:
            new_alphabet += ch

    print("Permuted alphabet:", new_alphabet)

    while True:
        text = input("Text: ")
        text2 = ""
        error = False

        for ch in text:
            if ch == " ":
                continue
            ch = ch.upper()
            if ch == "Ș":
                ch = "Ş"   
            if ch == "Ț":
                ch = "Ţ"
            if ch not in alphabet:
                print("Invalid character:", ch)
                error = True
                break
            text2 += ch

        if error == False:
            break

    result = ""
    for ch in text2:
        position = new_alphabet.index(ch)
        if mode == "e":
            new_position = (position + k) % n
        else:
            new_position = (position - k) % n
        result += new_alphabet[new_position]

    print("Result:", result)