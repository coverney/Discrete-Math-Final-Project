# Discrete-Math-Final-Project
---

**Link to Presentation**: https://docs.google.com/presentation/d/1uqC-Qx4atb-EpN-K5tSreMO5Cp9bhCh1xRemJBxIhJU/edit?usp=sharing

## Dependencies
To run the code in this repository, install jupyter notebook and Python 3 in your environment. A list of the packages needed for different scripts is included in the requirements.txt document.

## Data
The data for this project comes from Stanford's Network Analysis Project (SNAP). The first data set we used is the [Amazon Copurchases Dataset](https://snap.stanford.edu/data/amazon-meta.html), which has Amazon products (primarily books) as the nodes, and copurchases (products bought at the same time) as the edges. This dataset includes a list of copurchases based on their ASIN ID number, and [meta data ](https://snap.stanford.edu/data/amazon-meta.html) which has the product information for all products involved. The second data set we used is the [email-EU-core network](https://snap.stanford.edu/data/email-Eu-core.html), which was generated from the email data of a large European research institution. The dataset includes incoming and outgoing emails between members of the research institution, and excludes outgoing and incoming messages to the rest of the world. Each node is a person, represented by an ID number, and there is an edge (u, v) in the network if person u sent person v at least one email. 

## Parsing Data
In order to access the data from these datasets, we created scripts for parsing the network information into dictionary data structures, where each key is a node, and all edges are listed as the values of that node. The networks were both **undirected graphs**, so the connections were listed both ways. These data structures were then stored in pickle files to speed up access for future use. <br>
`parse_names.py`: Parses the Amazon network along with its metadata labels. <br>
`parse_emails.py`: Parses the EU-core-network email data. <br>
`parse_departments.py`: Parses the EU-core-network departments for each person. <br>

## Bron-Kerbosch Algorithm
In the Jupyter notebooks in this repository labelled with "Bron-Kerbosch", you can run our implementation of the Bron-Kerbosch algorithm, using recursive backtracking. The notebooks display information on algorithm run-time, number of recursive calls, identified maximal and maximum cliques, mapped names of what the clique items are, and visualizations of department breakdown for the email network. The notebooks are labelled by date they were made, and by dataset. The more recent notebooks include more features. The notebooks include implementation of the BK algorithm naively, with a pivot, and with degeneracy ordering as extensions. We discovered that the pivot method was significantly faster than the naive method for the email dataset, taking 29.36 ms for the pivot method, and 202.46 ms for the naive method. This is almost a factor of 10!

## Visualization

