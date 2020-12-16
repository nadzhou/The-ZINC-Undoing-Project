#!/usr/bin/env python


from __future__ import print_function
import time
import argparse as ap
from rdkit import Chem
from rdkit.Chem import AllChem
from pathlib import Path

start_time = time.time()


def main(): 

    args = args_sdf2pdb()
    drug_folder = retrieve_drug_folder(args)
    sdf2pdb(drug_folder, args)



def args_sdf2pdb(): 
    # Turning the input and parsing via argparse.
    parser = ap.ArgumentParser(description=__doc__)
    parser.add_argument("drug_input", help='Input file in SDF format')
    # Optional argument that will generate ay number of 
    # conformations user inputs.
    parser.add_argument("--c", type=int, default=1,
                help="get number of  conformations needed to be generated")
    args = parser.parse_args()


def retrieve_drug_folder(args): 
    # Sdf is converted to Smiles. Space
    return Path(args.drug_input)


def sdf2pdb(drug_folder):  
    # This will only retrieve the sdf files in a folder. 
    for drug in drug_folder.rglob("*.sdf"):

        print('Initializing conversion')
        print(str(drug))

        suppl = Chem.SDMolSupplier(str(drug))

        for mol in suppl:
            print("mole: %s" % mol)

            # Generate 3D coordinates
            m = Chem.AddHs(mol)
            cids = AllChem.EmbedMultipleConfs(m, numConfs=args.c, randomSeed=917)
            #AllChem.MMFFOptimizeMoleculeConfs(m)

            drug_path = Path(f'/home/nad/Desktop/n34/{drug.stem}/')       
            drug_path.mkdir(parents=True)

            # Iterate over conformer ids
            for i in cids:
                # Create a writer for each conformer
                fname = drug_path/f'{drug_path}/conformer_{i}.pdb'
                writer = Chem.PDBWriter(str(fname))
                # Write specific conformer
                writer.write(m, confId=i)
            
    print("Drug Done")

# Finally we need to track time too, right. 
print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__': 
    main()