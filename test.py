code = input()
for i in ["!", "?", ",", "."]:
    code = code.replace(i, "")
print(code.lower())
