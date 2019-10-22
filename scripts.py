from __future__ import print_function
import argparse as ap
from rdkit import Chem
from rdkit.Chem import AllChem

# I'm taking drugs as a sdf file
# and then converting them to smiles 
# and showing 2D coordinates on terminal. 

parser = ap.ArgumentParser(description='retrieving sdf files from an input file')

parser.add_argument("drug_input")
args = parser.parse_args()
drug = args.drug_input

with open(drug):
    suppl = Chem.SDMolSupplier(drug)
    with open('smiles.smi', 'w') as f: 
        for mol in suppl: 
            smi = Chem.MolToSmiles(mol)
            f.write("{}\n".format(smi))
    f.close()

    with open('smiles.smi', 'r') as f: 
        for mol in f:  
            m2= Chem.MolFromSmiles(mol)
            print(Chem.MolToMolBlock(m2))    
