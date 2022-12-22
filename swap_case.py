def swap_case(s):
    res = ""
    for char in s:
        if char.islower():
            res += char.upper()
        else:
            res += char.lower()
    return res

