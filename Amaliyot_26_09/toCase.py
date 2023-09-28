def toCase(case: str):
    if case.__contains__("_"):
        return toCamelCase(case)
    else:
        return toSnakeCase(case)


def toCamelCase(case: str):

    resultOfCase = []
    var = case.split("_")
    resultOfCase.append(var[0])

    for i in range(1, len(var)):
        resultOfCase.append(var[i].capitalize())
    return "".join(resultOfCase)


def toSnakeCase(case: str):
    resultOfCase = []

    for i in range(len(case)):
        if case[i].islower():
            resultOfCase.append(case[i])

        if case[i].isupper():
            resultOfCase.append("_")
            resultOfCase.append(case[i].lower())

    return "".join(resultOfCase)

camelCase = "camelCase"
snakeCase = "snake_case"

calelCase2 = "checkBoxQuestionType"
snakeCase2 = "short_answer_question_type"

print(toSnakeCase(calelCase2))
print(toCamelCase(snakeCase2))
print(toCase(calelCase2))
