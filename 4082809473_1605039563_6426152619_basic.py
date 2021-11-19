import numpy as np

INPUT_FILE_ADDRESS = 'input1.txt'
OUTPUT_FILE_ADDRESS = 'output.txt'
ALPHA = dict({
    ('A', 'A'): 0,
    ('C', 'C'): 0,
    ('G', 'G'): 0,
    ('T', 'T'): 0,
    ('A', 'C'): 110,
    ('C', 'A'): 110,
    ('A', 'G'): 48,
    ('G', 'A'): 48,
    ('A', 'T'): 94,
    ('T', 'A'): 94,
    ('C', 'G'): 118,
    ('G', 'C'): 118,
    ('C', 'T'): 48,
    ('T', 'C'): 48,
    ('G', 'T'): 110,
    ('T', 'G'): 110
})
DELTA = 30


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


def basic_bottom_up(first_gene: str, second_gene: str):
    opt_matrix = np.empty((len(first_gene), len(second_gene)))
    for i in range(len(first_gene)):
        opt_matrix[i, 0] = i

    for j in range(len(second_gene)):
        opt_matrix[0, j] = j

    for j in range(1, len(second_gene)):
        for i in range(1, len(first_gene)):
            first_gene_char = first_gene[i]
            second_gene_char = second_gene[j]
            mismatch = opt_matrix[i - 1, j - 1] + \
                ALPHA[(first_gene_char, second_gene_char)]
            skip_first_gene = opt_matrix[i - 1, j] + DELTA
            skip_second_gene = opt_matrix[i, j - 1] + DELTA
            opt_matrix[i, j] = min(mismatch, skip_first_gene, skip_second_gene)

    return opt_matrix


def basic_top_bottom(opt_matrix, first_gene, second_gene):
    i = len(first_gene) - 1
    j = len(second_gene) - 1
    first_matched_sequence = ''
    second_matched_sequence = ''
    while i != 0 and j != 0:
        if opt_matrix[i, j] == opt_matrix[i - 1, j] + DELTA:
            first_matched_sequence += "_"
            i -= 1
        elif opt_matrix[i, j] == opt_matrix[i, j - 1] + DELTA:
            second_matched_sequence += "_"
            j -= 1
        else:
            first_matched_sequence += first_gene[i]
            second_matched_sequence += second_gene[j]
            i -= 1
            j -= 1

    if i == 0:
        first_matched_sequence += first_gene[i]
        second_matched_sequence += second_gene[:j + 1][::-1]
    elif j == 0:
        first_matched_sequence += first_gene[:i + 1][::-1]
        second_matched_sequence += second_gene[j]

    return first_matched_sequence[::-1], second_matched_sequence[::-1], opt_matrix[-1, -1]


if __name__ == '__main__':
    read_input_file_dict = read_input_file(INPUT_FILE_ADDRESS)
    first_base_string = read_input_file_dict['first_base_string']
    first_base_string_indices = read_input_file_dict['first_base_string_indices']
    second_base_string = read_input_file_dict['second_base_string']
    second_base_string_indices = read_input_file_dict['second_base_string_indices']
    # print(first_base_string, first_base_string_indices,
    #       second_base_string, second_base_string_indices)
    first_gene = generate_string(first_base_string, first_base_string_indices)
    second_gene = generate_string(
        second_base_string, second_base_string_indices)
    # print(first_gene, second_gene)
    # assert first_gene == 'ACACTGACTACTGACTGGTGACTACTGACTGG', "Houston we have a problem in generating strings!"
    # assert second_gene == 'TATTATACGCTATTATACGCGACGCGGACGCG', "Houston we have a problem in generating strings!"

    opt_matrix = basic_bottom_up(first_gene, second_gene)
    # print(opt_matrix)
    first_matched_sequence, second_matched_sequence, score = basic_top_bottom(
        opt_matrix, first_gene, second_gene)
    print(first_gene)
    print(second_gene)
    # print(len(first_matched_sequence), len(second_matched_sequence))
    # print(first_matched_sequence, second_matched_sequence, score)
    print(score)
    print(first_matched_sequence)
    print(second_matched_sequence)
    assert first_matched_sequence[:50] == 'ACACACTGAC_TACTGACTGGTG_ACTACTG_ACT_G_GACTGAC_TACT'
    assert second_matched_sequence[:50] == 'TAT_TA_TTATACG_CTA_TTATACG_CGACGCGGACGC_G_T_ATACG_'

    assert first_matched_sequence[-51:] == 'CTACTG_ACT_G_GACTGAC_TACTGACTGGTG_ACTACTG_ACT_G_G_'
    assert second_matched_sequence[-51:] == 'G_CGACGCGGACGC_G_T_ATACG_CTA_TTATACG_CGACGCGGACGCG'
