def remove_dollar_sign(s):
    return s.replace("$","")

money = "$100$"
result = remove_dollar_sign(money)
print(result)
