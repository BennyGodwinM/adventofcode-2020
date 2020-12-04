import re

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
    return passport_validation(passport_dict)

def is_present_in_range(value,low,high):
    if int(value)>=low and int(value)<=high:
        return True
    return False

def is_hex(s):
    return re.fullmatch(r"^#[0-9a-f]{6}$", s or "") is not None

def is_valid_pid(s):
    return re.fullmatch(r"^[0-9]{9}$",s or "") is not None

def passport_validation(passport_dict):
    if not is_present_in_range(passport_dict['byr'],1920,2002):
        # print("Failed byr")
        return False
    if not is_present_in_range(passport_dict['iyr'],2010,2020):
        # print("Failed iyr")
        return False
    if not is_present_in_range(passport_dict['eyr'],2020,2030):
        # print("Failed eyr")
        return False
    hgt = passport_dict['hgt'].strip()
    hgt_type = hgt[-2:]
    hgt_value = hgt[0:-2]
    if hgt_type=='cm':
        if not is_present_in_range(hgt_value,150,193):
            # print("Failed hgt")
            return False
    elif hgt_type=='in':
        if not is_present_in_range(hgt_value,59,76):
            # print("Failed hgt")
            return False
    else:
        # print("Failed hgt")
        return False

    if not is_hex(passport_dict['hcl']):
        # print("Failed hcl")
        return False

    valid_ecl = "amb blu brn gry grn hzl oth".split(" ")
    if not passport_dict['ecl'] in valid_ecl:
        # print("Failed ecl")
        return False

    if not is_valid_pid(passport_dict['pid']):
        # print("Failed pid")
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
        except :
            current_passport = {key.strip(): item.strip() for key, item in current_passport.items()}
            if (is_valid(current_passport)):
                valid+=1
            current_passport = {}

    print(valid)

if __name__ == '__main__':
    main()
