import numpy as np

from .config import ALPHA, DELTA


def basic_bottom_up(first_gene: str, second_gene: str):
    """
    O(len(first_gene) x len(second_gene))
    """
    opt_matrix = np.empty((len(first_gene) + 1, len(second_gene) + 1))
    for i in range(len(first_gene) + 1):
        opt_matrix[i, 0] = i * DELTA

    for j in range(len(second_gene) + 1):
        opt_matrix[0, j] = j * DELTA

    for j in range(1, len(second_gene) + 1):
        for i in range(1, len(first_gene) + 1):
            first_gene_char = first_gene[i - 1]
            second_gene_char = second_gene[j - 1]
            mismatch = opt_matrix[i - 1, j - 1] + \
                       ALPHA[(first_gene_char, second_gene_char)]
            skip_first_gene = opt_matrix[i - 1, j] + DELTA
            skip_second_gene = opt_matrix[i, j - 1] + DELTA
            opt_matrix[i, j] = min(mismatch, skip_first_gene, skip_second_gene)

    return opt_matrix


def basic_top_bottom(opt_matrix, first_gene, second_gene):
    """
    opt_matrix[i, j] = optimal matched sequence from indexes 0 to i in the first gene 
        and optimal matched sequence from indexes 0 to j in the second gene
    """
    i = len(first_gene)
    j = len(second_gene)
    first_matched_sequence = ''
    second_matched_sequence = ''
    while i != 0 and j != 0:
        if opt_matrix[i, j] == opt_matrix[i - 1, j] + DELTA:
            first_matched_sequence += first_gene[i - 1]
            second_matched_sequence += "_"
            i -= 1
        elif opt_matrix[i, j] == opt_matrix[i, j - 1] + DELTA:
            first_matched_sequence += "_"
            second_matched_sequence += second_gene[j - 1]
            j -= 1
        else:
            first_matched_sequence += first_gene[i - 1]
            second_matched_sequence += second_gene[j - 1]
            i -= 1
            j -= 1

    if j == 0:
        second_matched_sequence = second_matched_sequence[::-1]
        second_matched_sequence = '_' * \
                                  len(first_gene[0:i]) + second_matched_sequence
        first_matched_sequence = first_matched_sequence[::-1]
        first_matched_sequence = first_gene[0:i] + first_matched_sequence

    elif i == 0:
        first_matched_sequence = first_matched_sequence[::-1]
        first_matched_sequence = '_' * \
                                 len(second_gene[:j]) + first_matched_sequence
        second_matched_sequence = second_matched_sequence[::-1]
        second_matched_sequence = second_gene[0:j] + second_matched_sequence

    return first_matched_sequence, second_matched_sequence, opt_matrix[-1, -1]
