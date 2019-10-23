'''retrieve molecules from sdf, convert to smiles
and then draw the structure of the fingerprint via 
a similarity map with the a template. .'''

from __future__ import print_function
import argparse as ap
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import SimilarityMaps

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
            refmol = Chem.MolFromSmiles('CCCN(CCCCN1CCN(c2ccccc2OC)CC1)Cc1ccc2ccccc2c1') # this is the template here

            ms = Chem.MolFromSmiles(mol)
            fp = SimilarityMaps.GetAPFingerprint(ms, fpType='normal')
            fp = SimilarityMaps.GetTTFingerprint(ms, fpType='normal')
            fp = SimilarityMaps.GetMorganFingerprint(ms, fpType='bv')

            fig, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol, ms, SimilarityMaps.GetMorganFingerprint)
            fig.save('/home/nad/Desktop/navid22.png')