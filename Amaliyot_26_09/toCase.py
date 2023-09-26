camelCase = "camelCase"
snakeCase = "snake_case"


def toCase(case: str):
    if case.__contains__("_"):
        return toCamelCase(case)
    else:
        return toSnakeCase(case)

    return "Your case is not a valid!"


def toCamelCase(case: str):
    for i in range(len(case)):
        if case[i] == "_":
            case[i + 1].upper()
            case[i].replace("_", "")
    resultCase = case
    return resultCase


def toSnakeCase(case: str):
    resultOfCase = []

    for i in range(len(case)):
        if case[i].islower():
            resultOfCase.append(case[i])
        if case[i].isupper():
            resultOfCase.append("_")
            resultOfCase.append(case[i].lower())

    return "".join(resultOfCase)

res = toSnakeCase(camelCase)
print(res)
#
#
# result = toCase(snakeCase)
# result2 = toCase(camelCase)
#
# snake = toSnakeCase(camelCase)
# camel = toCamelCase(snakeCase)
#
# print(snake)
# print(camel)
#
# print(result)
# print(result2)