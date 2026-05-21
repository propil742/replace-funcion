word = "КОТ"
def kit(wawa, waw, woo):
    wawaw = ""
    for char in wawa:
        if char != str(waw):
            wawaw += char
        else:
            char = str(woo)
            wawaw += char
    return wawaw

print(kit(word, "О", "И"))