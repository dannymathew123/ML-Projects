Problem Statement:
=================================
Your organization handles huge number of excel files with each one corresponding to a specific type.
Huge number of files comes to client, and need to be classified as the right type of file.
An expert needs to open the file and based on the colomn headings, should decide which type it is.
We cannot write a simple comparison logic to find it, as some random columns will be missing here and there.
We have a set of few excel files of each types to build the logic.

Solution
===================================================
Fetch the combination of headings of each type.
Write a logic to multiply the datasets by removing random ones from the available training set.
Convert them using a Bag-Of-Words algorithm and train a ML model.
Test the new file by reading the headers and find the type.