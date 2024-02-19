# 51cdslength.py by Jordan Shore
#
# This program reports the length of protein-coding genes in the E. Coli Genome.

import gzip

path = "GCF_000005845.2_ASM584v2_genomic.gff.gz"
with gzip.open(path, "rt") as file:
	for line in file:
		words = line.split()
		if (line[0] == "#") or (words[2] != "CDS"):
			continue
		start = int(words[3])
		end = int(words[4])
		print(end - start + 1)
