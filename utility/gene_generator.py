def generate_gene(base, indexes) -> str:
    """
    Takes a base string and indices of where the base string to be added to the cumulative string and returns
    constructed gene
    """
    gene = base
    for i in indexes:
        gene = gene[:i + 1] + gene + gene[i + 1:]
    return gene
