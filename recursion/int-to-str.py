def to_string(integer, base):
    string_ref = '0123456789ABCDEF'
    if integer // base == 0:
        return string_ref[integer % base]
    else:
        return to_string(integer // base, base=base) + string_ref[integer % base]

if __name__ == "__main__":
    print(to_string(1024, 10))
    print(to_string(1023, 16))