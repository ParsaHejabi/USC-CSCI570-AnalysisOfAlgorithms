def generate_string(base: str, indexes: list[int]) -> str:
    gene = base
    for i in indexes:
        gene = gene[:i+1] + gene + gene[i+1:]
    return gene
