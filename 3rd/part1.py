with open("input.txt") as f:
    bin_vals = f.readlines()
    bin_vals = [value.strip() for value in bin_vals]

def bin_to_dec(bin_str: str) -> int:
    bin_str = bin_str[::-1]
    num = 0 

    for x in range(len(bin_str)):
        num += int(bin_str[x]) * (2 ** x)

    return num

def calculate(vals: list) -> None:
    gamma = ""
    epsilon = ""
    one_cnt = [0]*12
    zero_cnt = [0]*12
    for item in vals:
        for i, v in enumerate(item):
            if int(v) == 0:
                one_cnt[i] += 1
            else:
                zero_cnt[i] += 1


    for x in range(12):
        if one_cnt[x] > zero_cnt[x]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(bin_to_dec(gamma) * bin_to_dec(epsilon))

calculate(bin_vals)