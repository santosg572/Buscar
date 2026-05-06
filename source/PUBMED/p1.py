from pymed import PubMed

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
results = pubmed.query("mixed models[Title]", max_results=5000)  


# Loop through the results
for article in results:
    print(f"Title: {article.title}")
#    print(f"Authors: {article.authors}")
#    print(f"Publication Date: {article.publication_date}")
#    print(f"Summary: {article.abstract}")
#    print("-" * 40)


