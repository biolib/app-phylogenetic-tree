from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib.pyplot as plt
import argparse
import sys
import subprocess


def generate_tree(infile):
    # Read the alignment
    format = "fasta"
    alignment = AlignIO.read(infile, format)
    
    # Calculate distances
    calculator = DistanceCalculator('identity')
    # Build the tree
    constructor = DistanceTreeConstructor(calculator,
                                          args.tree_type)  # Neighbor Joining tree or upgma for unweighted pair group method with arithmetic mean
    tree = constructor.build_tree(alignment)
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111)
    plt.title("Phylogenetic tree")
    tree.ladderize()
    dp = 5
    Phylo.draw(tree, axes = ax, branch_labels = lambda c: round(c.branch_length, dp), do_show = False)
    # Write output
    plt.savefig("tree.png")
    # Generate the Markdown preview
    print('![picture](tree.png)')


def print_tree(infile, format):
    # Read the alignment
    tree = Phylo.read(infile, format)
    fig = plt.figure(figsize = (12, 6))
    plt.title("Phylogenetic tree")
    #tree.ladderize() # Flip branches so deeper clades are displayed at top
    dp = 5
    Phylo.draw(tree)
    # Write output
    plt.savefig("tree.png")
    # Generate the Markdown preview
    print('![picture](tree.png)')

# Load input data
parser = argparse.ArgumentParser()
parser.add_argument("--input_type", default= "aln")
parser.add_argument("--format_tree")
parser.add_argument('--file', help = 'align', dest = 'file')
parser.add_argument('--tree_type', help = 'Tree type Neighbor Joining or UPGMA', dest = 'tree_type')
args = parser.parse_args()


if args.input_type == "aln":
    # Check the length of the input file
    counter = 0
    with open(args.file) as file:
        for line in file:
            if line.startswith('>'):
                counter += 1

    if counter < 3:
        print("There is too few sequences in your file. Please check your input has the correct length and format.")
        sys.exit(1)

    # generate tree
    generate_tree(args.file)
elif args.input_type == "tree":
    # print tree
    print_tree(args.file, args.format_tree)

