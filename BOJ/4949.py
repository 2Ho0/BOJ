while True:
    w = input()
    alpha = "abcdefghijklmnopqrstuvwxyz. "

    if w == ".":
        exit(0)
    w = w.lower()
    for i in alpha:
        w = w.replace(i, "")

    for j in w:
        w = w.replace("()", "")
        w = w.replace("[]", "")
    if len(w) > 0:
        print("no")
    else:
        print("yes")
        