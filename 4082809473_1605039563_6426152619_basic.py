INPUT_FILE_ADDRESS = 'input.txt'
OUTPUT_FILE_ADDRESS = 'output.txt'


def read_input_file(input_file_address=INPUT_FILE_ADDRESS) -> dict:
    """
    Takes a string as input file address and returns the base strings along indices for each base string
    Written by: Parsa
    """
    res = dict()
    res['first_base_string'] = ''
    res['first_base_string_indices'] = []
    res['second_base_string'] = ''
    res['second_base_string_indices'] = []
    with open(INPUT_FILE_ADDRESS, 'r') as f:
        input_file_lines = [line.strip() for line in f.readlines()]
        is_first_base_string = True
        for line in input_file_lines:
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


def generate_string(base: str, indexes: list[int]) -> str:
    """
    Takes a base string and indices of where the base string to be added to the cumulative string and returns
    constructed gene
    Written by: Alireza
    """
    gene = base
    for i in indexes:
        gene = gene[:i + 1] + gene + gene[i + 1:]
    return gene


# def alignment(string1, string2):
#     matrix = []
#     return matrix


# def create_output():
#     """
#     call aligment matrix istring1, string2n the whole 2 strings and get the matrixmatrix = alignment())string
#     """
#     matrix = alignment(string1, string2)
#     result = create_output(matrix)
#     run_basic_algorithm()
#     s1 = ""
#     s2 = ""
#     matrix = alignment(s1, s2)

if __name__ == '__main__':
    read_input_file_dict = read_input_file(INPUT_FILE_ADDRESS)
    first_base_string = read_input_file_dict['first_base_string']
    first_base_string_indices = read_input_file_dict['first_base_string_indices']
    second_base_string = read_input_file_dict['second_base_string']
    second_base_string_indices = read_input_file_dict['second_base_string_indices']
    print(first_base_string, first_base_string_indices, second_base_string, second_base_string_indices)
    first_gene = generate_string(first_base_string, first_base_string_indices)
    second_gene = generate_string(second_base_string, second_base_string_indices)
    print(first_gene, second_gene)
    assert first_gene == 'ACACTGACTACTGACTGGTGACTACTGACTGG', "Houston we have a problem in generating strings!"
    assert second_gene == 'TATTATACGCTATTATACGCGACGCGGACGCG', "Houston we have a problem in generating strings!"
