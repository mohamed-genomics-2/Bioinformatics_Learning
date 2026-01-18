import sys
from Bio import SeqIO  # Import the Sequence Input/Output tool

# 1. Safety Check (Same as before)
if len(sys.argv) < 2:
    print("Usage: python3 gc_biopython.py <filename>")
    sys.exit()

filename = sys.argv[1]

print(f"--- Analyzing {filename} ---")

# 2. The Biopython Magic
# SeqIO.parse automatically reads the file record by record.
# It handles the ">" lines and joining DNA lines for you.
for record in SeqIO.parse(filename, "fasta"):
    
    # 'record' is an object that holds .id (name) and .seq (DNA)
    gene_name = record.id
    dna_sequence = record.seq
    
    # 3. Calculate GC (Biopython sequences work just like strings)
    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")
    total_len = len(dna_sequence)
    
    gc_content = (g_count + c_count) / total_len * 100
    
    # 4. Print cleanly
    print(f"Gene: {gene_name}")
    print(f"Length: {total_len} bp")
    print(f"GC Content: {gc_content:.2f}%") # .2f rounds to 2 decimal places
    print("-" * 20) # Prints a divider line