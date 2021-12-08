from utility.read_input import read_input_file
from utility.gene_generator import generate_gene
from utility.efficient import efficient_algorithm
from utility.config import INPUT_FILE_ADDRESS, OUTPUT_FILE_ADDRESS

if __name__ == '__main__':
    read_input_file_dict = read_input_file(INPUT_FILE_ADDRESS)
    first_base_string = read_input_file_dict['first_base_string']
    first_base_string_indices = read_input_file_dict['first_base_string_indices']
    second_base_string = read_input_file_dict['second_base_string']
    second_base_string_indices = read_input_file_dict['second_base_string_indices']
    
    first_gene = generate_gene(first_base_string, first_base_string_indices)
    second_gene = generate_gene(second_base_string, second_base_string_indices)

    first_matched_sequence, second_matched_sequence, score = efficient_algorithm(first_gene, second_gene)
    
    print("first gene: ", first_gene)
    print("second gene:", second_gene)
    print("first matched gene: ", first_matched_sequence)
    print("second matched gene:", second_matched_sequence)
    print("score = ", score)
    assert len(first_matched_sequence) == len(second_matched_sequence)
    