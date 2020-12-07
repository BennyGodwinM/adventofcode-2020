def main():
    sum = 0
    with open('Day_6_input_data.txt') as file:
        current_group = []
        text = file.readlines()
        text.append('\n')
        for line in text:
            if line=='\n':
                sum += len(set(current_group))
                current_group = []
                continue
            for question in line:
                if not question=='\n':
                    current_group.append(question.strip())

    print(sum)

if __name__ == '__main__':
    main()
