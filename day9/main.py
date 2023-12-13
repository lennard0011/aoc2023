def calculate_first_differences(numbers):
    first_differences = []
    for i in range(len(numbers) - 1):
        first_differences.append(numbers[i + 1] - numbers[i])
    return first_differences

def calculate_next_number(numbers):
    first_differences = calculate_first_differences(numbers)
    if (all([first_difference == 0 for first_difference in first_differences])):
        return numbers[-1]
    else:
        return numbers[-1] + calculate_next_number(first_differences)


def run(part=1, file='test'):
    with open(f'day9/{file}.txt') as f:
        lines = f.readlines()

    answer = 0
    for line in lines:
        numbers = [int(number) for number in line.replace('\n', '').split(' ')]
        if part == 2:
            numbers.reverse()
        next_number = calculate_next_number(numbers)
        answer += next_number
    print(answer)

        
run(2, 'input')