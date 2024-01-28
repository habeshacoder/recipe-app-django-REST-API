def divide_watermelon(w):
    if w % 2 != 0 or w == 2:
        return "NO"
    else:
        return "YES"

w = int(input())

result = divide_watermelon(w)

print(result)