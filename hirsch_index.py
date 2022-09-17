"""Hirsch index  -  researchers h-index is the largest number h that the researcher has published h papers
that have been cited h times

H-index mesures both productivity and citation impact of the researcher

input variable is an array of times of citation, so this array means that this particular researcher
has 9 publications that each have been cited 1, 4, 1, 4, 2, 1, 3, 5, 6 times.

output is calculated h-index

The problem was derived from " Elements of programming interviews in python"
"""


def hirsch_indx_calculation(num_of_citation: list):

    num_of_citation.sort()

    for num in num_of_citation:
        if num == len(num_of_citation) - num_of_citation.index(num):
            return f"h = {num}"


print(hirsch_indx_calculation([1, 4, 1, 4, 2, 1, 3, 5, 6]))

# time complexity of the algorithm: O(nlogn)
# spacece complexity of the algorithm O(n):