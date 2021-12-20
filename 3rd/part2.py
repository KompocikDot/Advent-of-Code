with open("input.txt") as f:
    bin_vals = f.readlines()
    bin_vals = [value.strip() for value in bin_vals]

def bin_to_dec(bin_str: str) -> int:
    bin_str = bin_str[::-1]
    num = 0 

    for x in range(len(bin_str)):
        num += int(bin_str[x]) * (2 ** x)

    return num

def remove_some(arr: list[str], remove_str: str, removing_indx: int) -> list[str]:
    arr_en = arr.copy()
    for i, v in enumerate(arr):
        if v[removing_indx] == remove_str:
            arr_en.remove(v)

    return arr_en

def calculate(bin_arr: list, mode: str) -> int:
    for i in range(len(bin_arr[0])):
        if len(bin_arr) == 1:
            return bin_to_dec(bin_arr[0])

        zeros = 0
        for elem in bin_arr:
            if elem[i] == "0":
                zeros += 1
        if mode == "oxygen":
            if zeros > len(bin_arr) / 2:
                bin_arr = remove_some(bin_arr, "1", i)
            else:
                bin_arr = remove_some(bin_arr, "0", i)
        else:
            if zeros <= len(bin_arr) / 2:
                bin_arr = remove_some(bin_arr, "1", i)
            else:
                bin_arr = remove_some(bin_arr, "0", i)

    return bin_to_dec(bin_arr[0])

print(calculate(bin_vals, "o2") * calculate(bin_vals, "oxygen"))