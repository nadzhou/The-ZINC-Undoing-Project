

"""We get a sdf file, convert to Smiles. we then 
calculate the 2D coordinats of the molecule and print it
out on the terminal. 
"""

from __future__ import print_function
import argparse as ap
from rdkit import Chem
from rdkit.Chem import AllChem

# Turning the input and parsing via argparse. Space.
parser = ap.ArgumentParser(description=__doc__)
parser.add_argument("drug_input")
args = parser.parse_args()

# Sdf is converted to Smiles. Space
drug = args.drug_input
with open(drug):
    suppl = Chem.SDMolSupplier(drug)
    with open('smiles.smi', 'w') as f: 
        for mol in suppl: 
            smi = Chem.MolToSmiles(mol)
            f.write("{}\n".format(smi))

# Calculating the 2D coordinates. Space
suppl = Chem.SDMolSupplier(drug)
with open('smiles.smi', 'r') as f: 
    for mol in f:  # yreads the file line by line
        Chem.MolFromSmiles(mol)
        print(Chem.MolToMolBlock(m2))    