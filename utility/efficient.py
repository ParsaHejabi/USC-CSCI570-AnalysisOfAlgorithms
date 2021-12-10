import numpy as np

from utility.basic import basic_bottom_up, basic_top_bottom
from .config import ALPHA, DELTA


def efficient_algorithm(first_gene: str, second_gene: str):
    first_gene_length = len(first_gene)
    second_gene_length = len(second_gene)
    if first_gene_length == 1 or second_gene_length == 1:
        opt_matrix = basic_bottom_up(first_gene, second_gene)
        first_matched_sequence, second_matched_sequence, score = basic_top_bottom(opt_matrix, first_gene, second_gene)
        return first_matched_sequence, second_matched_sequence, score
    else:
        first_half_cost = bottom_up_with_two_column(first_gene, second_gene[:second_gene_length // 2])
        second_half_cost = bottom_up_with_two_column(first_gene[::-1], second_gene[second_gene_length // 2:][::-1])
        cut_cost = first_half_cost[:, -1] + second_half_cost[:, -1][::-1]
        first_gene_cutting_index = np.argmin(cut_cost)
        first_half_matched_first_gene, first_half_matched_second_gene, first_half_score = efficient_algorithm(
            first_gene[:first_gene_cutting_index], second_gene[:second_gene_length // 2])
        second_half_matched_first_gene, second_half_matched_second_gene, second_half_score = efficient_algorithm(
            first_gene[first_gene_cutting_index:], second_gene[second_gene_length // 2:])
    return first_half_matched_first_gene + second_half_matched_first_gene, \
           first_half_matched_second_gene + second_half_matched_second_gene, \
           first_half_score + second_half_score


def bottom_up_with_two_column(first_gene: str, second_gene: str):
    column_1 = np.empty((len(first_gene) + 1, 1))
    column_2 = np.empty((len(first_gene) + 1, 1))
    for i in range(len(first_gene) + 1):
        column_1[i, 0] = i * DELTA

    for j in range(1, len(second_gene) + 1):
        column_2[0, 0] = j * DELTA
        for i in range(1, len(first_gene) + 1):
            first_gene_char = first_gene[i - 1]
            second_gene_char = second_gene[j - 1]
            mismatch = column_1[i - 1, 0] + ALPHA[(first_gene_char, second_gene_char)]
            skip_first_gene = column_2[i - 1, 0] + DELTA
            skip_second_gene = column_1[i, 0] + DELTA
            column_2[i, 0] = min(mismatch, skip_first_gene, skip_second_gene)

        for i in range(len(first_gene) + 1):
            column_1[i, 0] = column_2[i, 0]
    return column_2
