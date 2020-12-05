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
    high_seat_id = 0
    with open('Day_5_input_data.txt') as f:
        for boarding_pass in f.readlines():
            row,col,seat_id = find_seat_ID(boarding_pass)
            if seat_id>high_seat_id:
                high_seat_id = seat_id
    print(high_seat_id)

if __name__ == '__main__':
    main()
