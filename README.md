# The-ZINC-Undoing-Projectas

# PDB-MAKER
Perhaps the most important part of this repository is the PDB-Maker file. through the command line, I get an input of the
directory to retrieve ALL the sdf files from with the additional optional argument of the number of conformations that the
user might want to generate. this optional argument is set to 1 by default. 

    parser = ap.ArgumentParser(description=__doc__)
    parser.add_argument("drug_input", help='Input file in SDF format')
    parser.add_argument("--c", type=int, default=1,
            help="get number of  conformations needed to be generated")
    args = parser.parse_args()
  the code will then write the files on desktop on the subfolder named after the drug's stem name.
  
        drug_path = Path(f'/home/nad/Desktop/n34/{drug.stem}/')       
        drug_path.mkdir(parents=True)

         # Iterate over conformer ids
        for i in cids:
            # Create a writer for each conformer
            fname = drug_path/f'{drug_path}/conformer_{i}.pdb'
            writer = Chem.PDBWriter(str(fname))
            # Write specific conformer
            writer.write(m, confId=i)

# INTRODUCTION 

hey everyone. 

ZINC is a  big database of commcerically available compounds which we can use to virtual screen and this is done mostly computationally (as the name virtual screening suggests), popular among friends for being the first step to virtual screening. I'll be doing some manipulation of the database here. 

**Motivation**
naturally, it gets hectic if what you'rre doing everyday is click your way through to get compounds individually. we need a way to retrieve molecules en masse. and that's what this program will try to accomplish. 

**Goals**
the goal here is to retrieve 'drug-like' compounds there are two main categories of compound in the database: 

1. Lead-like: defined as, 
> "which we define here as having molecular weight between 150 and 350, calculated LogP less than four, number of hydrogen-bond donors less than or equal to three, and number of hydrogen-bond acceptors less than or equal to six."*

2. Drug-like: which Wikipedia says is a qualitative measure given by both water and fat solubility when orally administered. highly potent and light in molecular weight. 

*https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1360656/
