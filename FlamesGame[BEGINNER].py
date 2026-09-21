def rm_common(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                char = a[i]
                a.remove(char)
                b.remove(char)
                return (a + ["*"] + b, True)

    return (a + ["*"] + b, False)


if __name__ == "__main__":

    # Take player names as input
    n1 = list(input("Player 1 name: ").lower().replace(" ", ""))
    n2 = list(input("Player 2 name: ").lower().replace(" ", ""))

    # Validate input
    if not n1 or not n2:
        print("Please enter valid names.")
        exit()

    # Remove common characters
    cont = True
    while cont:
        lst, cont = rm_common(n1, n2)

        idx = lst.index("*")
        n1 = lst[:idx]
        n2 = lst[idx + 1:]

    # Count remaining letters
    cnt = len(n1) + len(n2)

    # FLAMES relationship list
    res = [
        "Friends",
        "Lovers",
        "Affectionate",
        "Marriage",
        "Enemies",
        "Siblings"
    ]

    # Eliminate relationships until one remains
    while len(res) > 1:

        split_index = (cnt % len(res)) - 1

        if split_index >= 0:
            right = res[split_index + 1:]
            left = res[:split_index]
            res = right + left
        else:
            res.pop()

    # Display result
    print("Relationship status:", res[0])