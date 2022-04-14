Problem Statement:
=================================
Your Orgnisation handles multiple Loan recovery cases.
You have a dataset with details like Type of loan, Default Amount, Financial status, Percentage given back, Total Loans by applicant,
previously_defaulted, cibilscore etc and priority score of 1 or 0.(1 : Immediate Action needed, 0: Low Priority)
You have to give a priority Score for each cases based on the loan details.
This Value(0-1) is used as a priority scale.

Solution
===================================================
The dataset was preprocessed with sufficient steps (null handling, label encoding, one hot encodng, remove non-priority features etc)
Then trained random Forest model and got 78% accuracy.
This model was used to find the predict_proba() of testcases and that value(0-1) was used as priority Score.