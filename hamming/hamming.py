"""
Calculates the Hamming difference between two DNA strands
"""

def distance(dna_A, dna_B):
    """
    Calculates the distance between two dna strands
    Given: string dna_A, string dna_B
    Return: int distance
    """
    if not (isinstance(dna_A, str) and isinstance(dna_B, str)):
        raise ValueError("both paramenters should be of type str")
    if len(dna_A)!=len(dna_B):
        raise ValueError("dna strands must be of equal lengths")
    distance = 0
    for i in range(len(dna_A)):
        if dna_A[i]!=dna_B[i]:
            distance +=1
    return distance
