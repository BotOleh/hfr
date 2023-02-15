result = []


def divider(a, b):
    try:

        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ValueError:
        print("a<b")
        return 0
    except IndexError:
        print("b>100")
        return 0
    except TypeError:
        print("Type")
        return 0
    except ZeroDivisionError:
        print("Zerodivision")
        return 0
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 0: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)