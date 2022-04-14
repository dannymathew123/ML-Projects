Problem Statement:
=================================
Your organization is trying to digitalize documents. You have 1000s of pdfs which are OCRed and need to be classified correctly.
Documents are for reciepts corresponding to three categories.
1. Loan interest : Loan interest Details
2. Loan Agreement : Loan agreement details
3. Loan Security: loan security related details

Assume all the loan Agreement look same, with same struture and words.
Only differing in the Name of person, address, Amount, Bank Name etc. 
Likewise, Loan interest,Loan security looks same but only differs on the name, etc.

You get 1000s of OCRed reciepts in text files and have to manually classify them to loan interest/Loan Agreement/Loan security
As the pdf is OCRed, data wont be perfect and some documents will have some missing data.
Application side will read documents and give the file contents as strings.
You have to write a function to to classify them as one of the three types (unclear ones should be labelled as 'Needs Manual Checking') and return the class type.

Input : file content as a string.
Output : One of these classes
    1.Loan Agreement 
    2.Loan Interest 
    3.Loan Security 
    4.Need Manual Checking.

Solution
===================================================
 Take a sample of each types and take vector of the contents using BERT embedding.
 For each input string, take the cosine similarity of the input and calculated vectors.
 If the maximum similarity exceeds 70%, assign that class to it. Else, assign 'Needs Manual checking'.

eg: 
Loan Agreement Similarity = 0.34
Loan Security similarity = 0.67
Loan Interest similarity = 0.88

Return "Loan Interest" as Output.