from Bio import SeqIO
handle = open("all_records.fasta", "rU")
records = list(SeqIO.parse(handle, "fasta"))
