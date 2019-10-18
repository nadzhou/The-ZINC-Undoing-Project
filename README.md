# The-ZINC-Undoing-Projectas

hey everyone. 

ZINC is a  big database of commcerically available compounds which we can use to virtual screen and this is done mostly computationally (as the name virtual screening suggests), popular among friends for being the first step to virtual screening. I'll be doing some manipulation of the database here. 

Motivation
naturally, it gets hectic if what you'rre doing everyday is click your way through to get compounds individually. we need a way to retrieve molecules en masse. and that's what this program will try to accomplish. 

Goals
the goal here is to retrieve 'drug-like' compounds there are two main categories of compound in the database: 

1. Lead-like: defined as, "which we define here as having molecular weight between 150 and 350, calculated LogP less than four, number of hydrogen-bond donors less than or equal to three, and number of hydrogen-bond acceptors less than or equal to six."*

2. Drug-like: which Wikipedia says is a qualitative measure given by both water and fat solubility when orally administered. highly potent and light in molecular weight. 

*https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1360656/
