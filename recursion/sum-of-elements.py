def listsum(listnums):
    if len(listnums) == 1:
        return listnums[0]
    else:
        return listnums[0] + listsum(listnums[1:])

if __name__ == "__main__":
    print(listsum(list(range(1,10))))