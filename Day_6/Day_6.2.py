def main():
    sum = 0
    with open('Day_6_input_data.txt') as file:
        current_group = []
        text = file.readlines()
        text.append('\n')
        for line in text:
            if line=='\n':
                # print("Current Group:\n {}".format(current_group))
                intersection = set(current_group[0]).intersection(*current_group)
                # print("Intersection:\n{}".format(intersection))
                sum += len(intersection)
                current_group = []
                continue

            current_group.append([])

            for question in line:
                if not question=='\n':
                    current_group[-1].append(question.strip())


    print(sum)

if __name__ == '__main__':
    main()
