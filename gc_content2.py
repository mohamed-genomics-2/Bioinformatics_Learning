# My upgraded bioinformatics script: Reading from a FASTA file

filename = "insulin.fasta"

# 1. Read the file
# We use 'with open' because it automatically closes the file safely
with open(filename, "r") as file:
    dna_sequence = ""
    for line in file:
        line = line.strip() # Remove invisible newline characters
        
        # Check: Is this the header? (Starts with >)
        if line.startswith(">"):
            print("Analyzing Sequence:", line) # Just print the name
        else:
            # If it's not a header, it's DNA. Add it to our string.
            dna_sequence = dna_sequence + line

# 2. Count the nucleotides (Same logic as before)
count_a = dna_sequence.count("A")
count_t = dna_sequence.count("T")
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")

# 3. Calculate GC Content
total_length = len(dna_sequence)
gc_content = (count_g + count_c) / total_length * 100

# 4. Print Results
print("--- Results ---")
print("Total Length:", total_length)
print("GC Content:", gc_content, "%")