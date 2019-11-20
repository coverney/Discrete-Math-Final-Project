# There are 244,750 number ids vs. 542,684 book names...that's twice as many names as ids
import string
import re
import pickle

# Open the amazon copurchases meta data file
file = open('./amazon-meta.txt', 'r', encoding='utf-8', errors='ignore')

# This will store the product ASIN IDs as keys, and the product names as the values
product_ID_map = {}
# This will store the ASIN ID's of each product as a key, and the list of 5 'similar' product ASIN IDs as the value
# i.e. 'B000059TOC': '630366704X B0002ERXB8 B0001932ZU B0001VTPUE B0007LPSH2'
copurchases = {}

# Iterate through the file line by line to store the product ASIN IDs, and corresponding product Names
# Store the "similar" products in the adjacency dictionary, copurchases
linecount = 0
for line in file:
    linecount +=1
    if linecount % 10000 == 0:
        print(linecount)
    line = line.strip()
    if line.startswith("ASIN"):
        ASIN = line[5:].strip()
    elif line.startswith("title"):
        title = line[6:].strip()
        title = ' '.join(title.split())
    elif line.startswith("similar"):
        lst = line.split()
        copurchased = [c for c in lst[2:]]
    elif line == "":
        try:
            if ASIN != "":
                product_ID_map[ASIN] = title
                if ASIN in copurchases:
                    copurchases[ASIN].extend(copurchased)
                else:
                    copurchases[ASIN] = copurchased
                for el in copurchased:
                    if ASIN in copurchases:
                        if el not in copurchases[ASIN]:
                            copurchases[ASIN].append(el)
                    else:
                        copurchases[ASIN] = [el]
        except NameError:
            continue
        ASIN, title, copurchased = "", "", ""

# Close the metadata file
file.close()
# Pickle the product_ID_map to save the data and run faster later
file_Name = "ID_map-11-18"
# open the file for writing
picklefile = open(file_Name,'wb')
# this writes the object a to the
pickle.dump(product_ID_map, picklefile)
# here we close the fileObject
picklefile.close()

# Pickle the copurchases dictionary to save the data and run faster later
file_Name = "copurchases-11-18"
# open the file for writing
picklefile = open(file_Name,'wb')
# this writes the object a to the
pickle.dump(copurchases, picklefile)
# here we close the fileObject
picklefile.close()

print("Done")
