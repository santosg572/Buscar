from pymed import PubMed

# Initialize the PubMed object
pubmed = PubMed(tool="MyToolName", email="my@email.address")

# Run a query
#results = pubmed.query("COVID-19 vaccine", max_results=5000)

#results = pubmed.query("(gifted[Title]) AND (('2025/01/01'[Date - Publication] : '2026/01/01'[Date - Publication]))", max_results=5000)

results = pubmed.query("(gifted[Title])", max_results=5000)


# Iterate through results
k = 1
for article in results:
    print(str(k) + ' - ' + article.title)
    k = k+1

