import sys # New Line 1: Load the system library

# Check if the user forgot to provide a filename
if len(sys.argv) < 2:
    print("Error: You must provide a filename.")
    print("Usage: python3 gc_content.py <filename>")
    sys.exit()

# New Line 2: Grab the first word written AFTER the script name
filename = sys.argv[1] 

with open(filename, "r") as file:
    dna_sequence = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            print("Analyzing Sequence:", line)
        else:
            dna_sequence = dna_sequence + line

# (The rest of the math remains exactly the same...)
total_length = len(dna_sequence)
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")
gc_content = (count_g + count_c) / total_length * 100

print("--- Results ---")
print("Total Length:", total_length)
print("GC Content:", gc_content, "%")