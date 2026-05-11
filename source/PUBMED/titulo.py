import sys
from pymed import PubMed

#palabra = sys.argv[1]

palabra = "chaos"

# Initialize the PubMed client
# Note: You must provide a valid tool name and email for the PubMed API
pubmed = PubMed(tool="MyPubMedSearcher", email="my@email.address")


# Perform a query
#results = pubmed.query("parkinson[Title]", max_results=5000)
#results = pubmed.query("raspberry[Title]", max_results=5000)
#results = pubmed.query("GROMACS[Title]", max_results=5000)
#results = pubmed.query("NVIDIA[Title]", max_results=5000)
#results = pubmed.query("Finite element[Title]", max_results=5000)
#results = pubmed.query("machine learning[Title]", max_results=5000)
#results = pubmed.query("gifted[Title]", max_results=5000)
#results = pubmed.query("high capabilities", max_results=5000)
#results = pubmed.query("computational biology[Title]", max_results=5000)
#results = pubmed.query("built environments[Title]", max_results=5000)
#results = pubmed.query("sleep quality[Title]", max_results=5000)

palabra = palabra+"[Title]"
results = pubmed.query(palabra, max_results=5000)  

file = "chaos_may1126.txt"

filon = open(file, 'w')

# Loop through the results
k = 1
for article in results:
    print(f"Title: {article.title}")
    filon.write(str(k)+'.- '+article.title+'\n')
#    print(f"Authors: {article.authors}")
#    print(f"Publication Date: {article.publication_date}")
#    print(f"Summary: {article.abstract}")
#    print("-" * 40)
    k = k+1
filon.close()

