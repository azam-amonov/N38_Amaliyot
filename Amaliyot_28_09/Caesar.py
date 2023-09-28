def caesarHashing(text: str, key: int) -> str:
    result = []

    for i in text:
        var = (ord(i) - 97 + key) % 26 + 97
        result.append(chr(var))

    return "".join(result)


print(caesarHashing("wxyz", 1))

print(97 % 26)

