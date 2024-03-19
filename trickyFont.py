import string

def different_characters(source_list: list) -> int:
    all_chars = ""
    fio = source_list[0] + source_list[1] + source_list[2]
    for i in fio:
        if i in all_chars:
            continue
        else:
            all_chars += i
    return(len(all_chars))

def day_month(source_list: list) -> int:
    list_number = list(source_list[3] + source_list[4])
    result = 0
    for i in list_number:
        result += int(i)
    return(result * 64)

def alphabet(source_list: list) -> int:
    return((list(string.ascii_uppercase).index(source_list[0][0]) + 1) * 256)

def get_cipher(source_list: list) -> str:
    one = different_characters(source_list)
    two = day_month(source_list)
    thre = alphabet(source_list)
    result = hex(one + two + thre)[2:].upper()
    if len(result) > 3:
        result = result[-3:]
    return(result)

if __name__ == "__main__":
    result = ""

    in_file = open("input.txt")
    out_file = open("output.txt", 'w')

    i = int(in_file.readline())
    for j in range(i):
        source = in_file.readline()
        source_list = source.split(',')
        result += get_cipher(source_list) + ' '
    out_file.write(result)