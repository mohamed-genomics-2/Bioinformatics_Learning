# My first bioinformatics script

# 1. Define a DNA sequence (usually this comes from a file)
dna_sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# 2. Count the nucleotides
count_a = dna_sequence.count("A")
count_t = dna_sequence.count("T")
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")

# 3. Calculate GC Content percentage
# Formula: (G + C) / Total Length * 100
total_length = len(dna_sequence)
gc_content = (count_g + count_c) / total_length * 100

# 4. Print the results to the screen
print("--- DNA Analysis Results ---")
print("Total Length:", total_length, "base pairs")
print("A count:", count_a)
print("T count:", count_t)
print("GC Content:", gc_content, "%")