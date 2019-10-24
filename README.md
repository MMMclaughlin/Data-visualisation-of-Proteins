CSC1034: Practical 2
====================

This package allows analysis and display of proteins from Uniprot.

-----Prerequisites/Requirements---------

The Bio module  
The Argparse module  
A file of proteans in the same formay as uniprot.receptor.xml.gz
The Gzip module  
Matplotlib.pyplot module
Os module

-----The Project------

The project was built to handle a portion of the uniprot database of proteins and then interact with the data we could extract 
from a gzip file. Uniplot.py is the "main" function which runs Cli and from there the given option is run.  



-----Arguement usage-----

Optional Arguments -> these allow you to edit how the mandatory function runs  

--file then follow with a file location to change the used file of proteans. If this file does not exist the system will exit

--depth this allows you to go deeper into the taxa levels name a number greater than 0

  
  
Mandatory functions. One of these must be chosen, .---------

dump: - will simply list all the proteans and their information straight from the given file

list: - will list all the protean names without any added information.

average: - will calculate the average length of the proteans in the given file

average_len_taxa:  - will create a graphical interface to display the most common taxas in the data set 

average_len_taxa_piechart: - will create a graphical interface to display the most common taxas in the set  





-----------------
