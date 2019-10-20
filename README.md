CSC1034: Practical 2
====================

This package allows analysis and display of proteins from Uniprot.

-----Prerequisites/Requirements---------

The Bio module  
The Argparse module  
The uniprot_receptor.xml.gz
The Gzip module

-----The Project------

The project was built to handle a portion of the uniprot database on proteins and then interact with the data we could extract 
from a gzip file. Uniplot.py is the "main" function which runs Cli and from there the given option is run.  


-----Arguement usage-----


dump: - will simply list all the proteans and their information straight from the given file

list: - will list all the protean names without any added information.

average: - will calculate the average length of the proteans in the given file

average_len_taxa:  - will create a graphical interface to display the most common taxas in the data set 


-----------------
