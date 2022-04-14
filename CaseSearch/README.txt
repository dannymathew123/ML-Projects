Problem Statement:
=================================
Your organization have huge database of Debt recovery cases.
You need a UI based searching(Top Results) for cases using keywords in the description.

Solution
===================================================
An NLP based embedding of the description, followed by a cosine similarity between the query and available cases.
Tried BERT/USE at first, but due to person names and legal terms in description, it was not giving proper results.
Finally, we fixed on TF-IDF with cosine similarity.
All the descriptions are converted to TF-IDF embeddings and the keyword is converted to similar embedding.
Cosine similarity is found between the descriptions and top ones are listed.

