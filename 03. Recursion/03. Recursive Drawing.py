def recursive_draw(num):
    if num <= 0:
        return

    print("*" * num)

    recursive_draw(num - 1)

    print("#" * num)

recursive_draw(int(input()))