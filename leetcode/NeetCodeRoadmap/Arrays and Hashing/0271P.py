def encode(self, strs):
    result = ""
    for s in strs:
        result += str(len(s)) + "@" + s
    return result

def decode(self, str):
    result, i = [], 0

    while i < len(str):
        j = i
        while str[j] != "@":
            j += 1
        length = int(str[i:j])
        result.append(str[j + 1 : j + 1 + length])
        i = j + 1 + length
    return result