valid_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def key_value_pair_parser(key_value):
    key,value = key_value.split(":")
    return [key,value]

def line_parser(line):
    return [key_value_pair_parser(x) for x in line.split(" ")]

def is_valid(passport_dict):
    for key in valid_keys:
        if not key in passport_dict:
            return False
    return True

def main():
    valid = 0
    f = open("Day_4_input_data.txt")
    text = f.readlines();
    current_passport = {}
    text.append('\n')

    for line in text:
        try:
            fields_list = line_parser(line)
            fields_dict = {pair[0]: pair[1] for pair in fields_list}
            current_passport.update(fields_dict)
        except ValueError:
            if (is_valid(current_passport)):
                valid+=1
            current_passport = {}

    print(valid)

if __name__ == '__main__':
    main()
