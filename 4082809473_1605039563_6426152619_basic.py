import sys

from utility.read_input import read_input_file
from utility.gene_generator import generate_gene
from utility.basic import basic_bottom_up, basic_top_bottom
from utility.write_output import write_output_file

if __name__ == '__main__':
    input_file_address = sys.argv[1]
    output_file_address = sys.argv[2]
    read_input_file_dict = read_input_file(input_file_address)
    first_base_string = read_input_file_dict['first_base_string']
    first_base_string_indices = read_input_file_dict['first_base_string_indices']
    second_base_string = read_input_file_dict['second_base_string']
    second_base_string_indices = read_input_file_dict['second_base_string_indices']

    first_gene = generate_gene(first_base_string, first_base_string_indices)
    second_gene = generate_gene(second_base_string, second_base_string_indices)

    opt_matrix = basic_bottom_up(first_gene, second_gene)

    first_matched_sequence, second_matched_sequence, score = basic_top_bottom(
        opt_matrix, first_gene, second_gene)
    # print("first gene: ", first_gene)
    # print("second gene:", second_gene)
    # print("first matched gene: ", first_matched_sequence)
    # print("second matched gene:", second_matched_sequence)
    # print("score = ", score)
    assert len(first_matched_sequence) == len(second_matched_sequence)

    # assert first_matched_sequence[:50] == '_A_CA_CACT__G__A_C_TAC_TGACTG_GTGA__C_TACTGACTGGAC'
    # assert second_matched_sequence[:50] == 'TATTATTA_TACGCTATTATACGCGAC_GCG_GACGCGTA_T_AC__G_C'

    # assert first_matched_sequence[-51:] == 'GTGA__C_TACTGACTGGACTGACTACTGACTGGTGACTACT_GACTG_G'
    # assert second_matched_sequence[-51:] == 'G_GACGCGTA_T_AC__G_CT_ATTA_T_AC__GCGAC_GC_GGAC_GCG'

    # Make the output string
    output = f'{first_matched_sequence[:50]} {first_matched_sequence[-51:]}\n{second_matched_sequence[:50]} {second_matched_sequence[-51:]}\n{float(score)}\n'
    write_output_file(output_file_address, output)
