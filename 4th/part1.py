


def read_bingos():
    with open('input.txt') as f:
        all_lines = f.readlines()
        all_lines = [l.strip() for l in all_lines]
        nums = [i for i in all_lines[0].split(",")]
        

        bingo_arr = []
        for l in range(2, len(all_lines)):
            if all_lines[l] != "":
                bingo_arr.append(all_lines[l].split(" "))
               
            else:
                pass

    return (nums, bingo_arr)

def clear_empty(tabl: list) -> list:
    for x in range(len(tabl)):
        for i in tabl[x]:
            if i == '':
                tabl[x].remove(i)
    
    return tabl

def mark_numbers(num: int, flat_tables: list) -> list:
    for row in flat_tables:
        for item in range(len(row)):
            if row[item] == num:
                row[item] = False

    return flat_tables

def count_remaining(table: list) -> int:
    nums_sum = 0
    for x in table:
        nums_sum += int(x)

    return nums_sum

def check_bingo(flat_tables: list):
    # horizontal check
    for indx in range(0, len(flat_tables), 5):
        if list(set(flat_tables[indx])) == [False] or list(set(flat_tables[indx+1])) == [False] or list(set(flat_tables[indx+2])) == [False] or list(set(flat_tables[indx+3])) == [False] or list(set(flat_tables[indx+4])) == [False]:
            return (True, flat_tables[indx] + flat_tables[indx+1] + flat_tables[indx+2] + flat_tables[indx+3] + flat_tables[indx+4])
        
    #vertical check
    for indx in range(0, len(flat_tables), 5):
        for row in range(0, 5):
            if list(set([flat_tables[indx][row], flat_tables[indx+1][row], flat_tables[indx+2][row], flat_tables[indx+3][row], flat_tables[indx+4][row]])) == [False]:
                return (True, flat_tables[indx] + flat_tables[indx+1] + flat_tables[indx+2] + flat_tables[indx+3] + flat_tables[indx+4])

    return (False, [])



def part1():
    nums, bingo_table = read_bingos()
    bingo_table = clear_empty(bingo_table)
    for num in nums:
        bingo_table = mark_numbers(num, bingo_table)
        bingo, table = check_bingo(bingo_table)
        if bingo:
            print(count_remaining(table) * int(num))
            return

part1()