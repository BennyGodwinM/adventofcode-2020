valid = 0

def return_instances(password,character):
    return password.count(character)

with open('Day_2_input_data.txt') as f:
    text = f.readlines()
    for line in text:
        policy,character,password = line.split(" ")
        character = character[0]
        low_lim,high_lim = [int(x) for x in policy.split("-")]

        instances = return_instances(password,character)
        # print("Policy: {} | Low_Lim: {}, | High_Lim: {} | Instances: {} | Password: {} | Character: {}".format(policy,low_lim,high_lim,instances,password,character))
        if(instances>=low_lim and instances<=high_lim):
            valid+=1
print(valid)