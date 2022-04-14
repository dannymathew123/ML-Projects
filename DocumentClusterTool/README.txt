Problem Statement:
=================================
You will get loads of documents which we dont have training data to classify.
We just know how many categories of docs are there in each drop.
You have to come up with a flexible solution to cluster them by user giving how many clusters.
Files need to be aautomatically clustered and a excel should come with the assigned cluster.

Solution
===========================
Documents should be read and have to create a BERT embedding of them.
Then do a normal clustering(K means) with the specific K.