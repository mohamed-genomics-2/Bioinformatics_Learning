import matplotlib.pyplot as plt

# 1. Define Sequences
# I made these longer so you can see the effect of the "Window"
seq1 = "ACCTTGTCCTCTTTGCCCGGGTACGTACGTACGTACGTACG"
seq2 = "ACCTTGTCCTATTGCCCGGGTACGTACGTACGTACGTACG" 
# Note: seq2 has a mismatch ("A" instead of "C") near the start

# 2. Set Window and Threshold parameters
window_size = 5   # Look at 5 bases at a time
threshold = 4     # At least 4 must match (80% similarity)

# 3. Create data for the plot
x_coords = []
y_coords = []

# Loop through seq1, stopping before we run off the end
for i in range(len(seq1) - window_size + 1):
    
    # Loop through seq2
    for j in range(len(seq2) - window_size + 1):
        
        # Get the two "chunks" (slices)
        chunk1 = seq1[i : i + window_size]
        chunk2 = seq2[j : j + window_size]
        
        # Count matches in this specific chunk
        matches = 0
        for k in range(window_size):
            if chunk1[k] == chunk2[k]:
                matches += 1
        
        # FILTER: Only record a dot if matches meet the Threshold
        if matches >= threshold:
            x_coords.append(i)
            y_coords.append(j)

# 4. Draw the Plot
plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords, color='blue', s=20) 

# Labeling
plt.xlabel(f"Sequence 1 (Window={window_size})")
plt.ylabel(f"Sequence 2 (Threshold={threshold})")
plt.title(f"Dot Plot with Noise Filtering\n(Match {threshold} out of {window_size})")
plt.grid(True, linestyle='--', alpha=0.5)

# 5. Save it
plt.savefig("dotplot_filtered.png")
print(f"Plot saved! Window: {window_size}, Threshold: {threshold}")