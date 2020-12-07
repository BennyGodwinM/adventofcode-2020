def input_parser():
    rules = {}
    with open('Day_7_input_data.txt') as file:
        text = file.readlines();
        for rule in text:
            bits = rule.split(' ')
            main_bag = " ".join(bits[0:2])
            segment = bits[4:]
            nested_bags = nested_bag_parser(' '.join(segment))
            rules[main_bag] = nested_bags
        return(rules)

def nested_bag_parser(segment):
    bags = {}
    nested_bags = segment.split(',')
    for bag in nested_bags:
        bits = bag.split(" ")
        if bits[0]=='no':
            return None
        elif bits[0]=='':
            number = bits[1]
            bag_name = " ".join(bits[2:4])
        else:
            number = bits[0]
            bag_name = " ".join(bits[1:3])

        bags[bag_name] = number
    return (bags)

rules = {}

def find(bag_name, searched_bag):
    return bag_name == searched_bag or any([find(b, searched_bag) for b in rules[bag_name]])

def search(bag):
    
    if bag=='shiny gold':
        return 1
    nested_bags = rules[bag]
    if nested_bags==None:
        return 0
    nested_bags = list(nested_bags.keys())
    for nested_bag in nested_bags:
        if search(nested_bag)==0:
            continue
        return search(nested_bag)
    return 0

def main():
    bag_colors = 0
    global rules 
    rules = input_parser()
    for rule in rules:
        bag_colors += search(rule)
        # bag_colors+=find(rule[0],'shiny gold')
    print (bag_colors)
    print(nested_bags('shiny gold',0))

def nested_bags(bag,total):
    print(rules[bag])
    for nested_bag in rules[bag]:
        print(nested_bag)

if __name__ == '__main__':
    main()
