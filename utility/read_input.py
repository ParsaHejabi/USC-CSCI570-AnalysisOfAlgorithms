def read_input_file(input_file_address) -> dict:
    """
    Takes a string as input file address and returns the base strings along indices for each base string
    Written by: Parsa
    """
    res = dict()
    res['first_base_string'] = ''
    res['first_base_string_indices'] = []
    res['second_base_string'] = ''
    res['second_base_string_indices'] = []
    with open(input_file_address, 'r') as f:
        input_file_lines = [line.strip() for line in f.readlines()]
        is_first_base_string = True
        for line in input_file_lines:
            # isnumeric complexity
            if not line.isnumeric() and res['first_base_string'] == '':
                res['first_base_string'] = line
            elif line.isnumeric() and is_first_base_string:
                res['first_base_string_indices'].append(int(line))
            elif not line.isnumeric() and res['first_base_string'] != '':
                is_first_base_string = False
                res['second_base_string'] = line
            elif line.isnumeric() and not is_first_base_string:
                res['second_base_string_indices'].append(int(line))

    return res
