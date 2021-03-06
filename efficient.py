import sys

from utility.read_input import read_input_file
from utility.gene_generator import generate_gene
from utility.efficient import efficient_algorithm
from utility.write_output import write_output_file

if __name__ == '__main__':
    input_file_address = sys.argv[1]
    output_file_address = 'output.txt'
    read_input_file_dict = read_input_file(input_file_address)
    first_base_string = read_input_file_dict['first_base_string']
    first_base_string_indices = read_input_file_dict['first_base_string_indices']
    second_base_string = read_input_file_dict['second_base_string']
    second_base_string_indices = read_input_file_dict['second_base_string_indices']

    first_gene = generate_gene(first_base_string, first_base_string_indices)
    second_gene = generate_gene(second_base_string, second_base_string_indices)

    assert len(first_gene) == 2 ** len(first_base_string_indices) * len(first_base_string)
    assert len(second_gene) == 2 ** len(second_base_string_indices) * len(second_base_string)

    first_matched_sequence, second_matched_sequence, score = efficient_algorithm(
        first_gene, second_gene)

    assert len(first_matched_sequence) == len(second_matched_sequence)
    assert len(first_matched_sequence.replace('_', '')) == len(first_gene)
    assert len(second_matched_sequence.replace('_', '')) == len(second_gene)

    output = f'{first_matched_sequence[:50]} {first_matched_sequence[-51:]}\n{second_matched_sequence[:50]} {second_matched_sequence[-51:]}\n{float(score)}\n'
    write_output_file(output_file_address, output)
