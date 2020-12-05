import math
def find_section(lower,upper,character):
    if character=='F' or character=='L':
        upper = math.floor(upper-((upper-lower)/2))
    elif character=='B' or character=='R':
        lower= math.ceil(lower+((upper-lower)/2))
    return [lower,upper]

def find_seat_ID(bsp):
    row_chars = bsp[0:7]
    col_chars = bsp[-4:-1]
    row_low = 0
    row_up = 127
    col_low = 0
    col_up = 7
    for character in row_chars:
        row_low,row_up = find_section(row_low,row_up,character)
    for character in col_chars:
        col_low,col_up = find_section(col_low,col_up,character)

    return [row_up,col_up,(row_up*8) + col_up]
def main():
    seat_ids = []
    with open('Day_5_input_data.txt') as f:
        for boarding_pass in f.readlines():
            row,col,seat_id = find_seat_ID(boarding_pass)
            if not (row==127 or row==0):
                seat_ids.append(seat_id)

    seat_ids.sort()
    index = 1
    while index<len(seat_ids):
        current_seat = seat_ids[index]
        previous_seat = seat_ids[index-1]
        my_seat = (current_seat+previous_seat)/2
        if my_seat+1==current_seat and my_seat-1==previous_seat:
            print(int(my_seat))
            break
        index+=1



if __name__ == '__main__':
    main()
