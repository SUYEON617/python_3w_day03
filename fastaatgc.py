#! /home/suyeon/miniconda3/bin/python3.7

from Bio import SeqIO

record=SeqIO.read("059.fasta","fasta")

A=record.seq.count("A")
T=record.seq.count("T")
G=record.seq.count("G")
C=record.seq.count("C")

print(f"A: {A}")
print(f"T: {T}")
print(f"G: {G}")
print(f"C: {C}")
