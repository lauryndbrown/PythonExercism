"""
Module converts DNA to RNA
"""
dna_to_rna = {"G":"C", "C":"G", "T":"A", "A":"U"} 
def to_rna(dna):
    """
    Given: string dna
    Return: string representing rna
    """
    if not isinstance(dna, str):
        raise ValueError("function takes a string")
    rna = []
    for nucleotide in dna:
        try:
            rna.append(dna_to_rna[nucleotide])
        except KeyError:
            return ''
    return ''.join(rna)

