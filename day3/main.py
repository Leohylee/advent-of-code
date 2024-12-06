def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        lines = file.readlines()
    output = ""
    for line in lines:
        output += line
    return output

def calculate_mul(memory_input):
    product = 0
    mul_idx = 0
    num_idx = 0
    num = ['','']
    number_flag = False
    mul_str = "mul("
    enable_str = "do()"
    disable_str = "don't()"
    enable_idx = 0
    enable_flag = True
    for char in memory_input:
        # check if it is disabled, if yes, only look for enable function: do()
        if not enable_flag and char == enable_str[enable_idx]:
            enable_idx += 1
            if enable_idx == 4:
                # trigger do()
                enable_flag = True
                enable_idx = 0
        # if not processing mul() or number, check don't()
        elif enable_flag and mul_idx == 0 and num_idx == 0 and char == disable_str[enable_idx]:
            enable_idx += 1
            if enable_idx == 7:
                # trigger don't()
                enable_flag = False
                enable_idx = 0
        # if enabled and not processing number, check mul()
        elif enable_flag and not number_flag and char == mul_str[mul_idx]:
            mul_idx += 1
            if mul_idx == 4:
                number_flag = True
        # if enabled and processing number, check if the character is numeric
        elif enable_flag and number_flag and char.isnumeric():
            num[num_idx] += char
        # if getting the end of mul(), calcullate the product, and reset everything
        elif enable_flag and number_flag and num_idx == 1 and char == ')':
            product += int(num[0]) * int(num[1])
            num = ['','']
            mul_idx = 0
            num_idx = 0
            number_flag = False
        # move to process number 2
        elif enable_flag and number_flag and char == ',':
            num_idx = 1
        # reset every flag and counter variables
        else:
            mul_idx = 0
            num_idx = 0
            num = ['','']
            number_flag = False
            enable_idx = 0
    return product

if __name__ == "__main__":
    memory = read_input('./input.txt')
    print(calculate_mul(memory))