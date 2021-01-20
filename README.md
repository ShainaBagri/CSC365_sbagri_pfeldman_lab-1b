# CSC365_Lab1B

The code makes use of the package pandas. It can be installed via "pip install pandas".

Because the code is written in python, it does not need an extra step to be compiled.
Simply run the code with "python schoolsearch.py".

Commands that can be invoked:

S[tudent]: <lastname> [B[us]]

T[eacher]: <lastname>

B[us]: <number>

G[rade]: <number> S[tudent]|T[eacher]|H[igh]|L[ow]

C[lassroom]: <number> S[tudent]|T[eacher]

A[verage]: <number>

D[ata] [G[rade]|B[us]|T[eacher]]

E[nrollment]

I[nfo]

Q[uit]

Note: Data command without any flags returns dataframe with GPA, Grade, Bus, and Teacher sorted by GPA value in increasing order.

Note: A flag is required for Grade and Classroom commands, but is optional for Student and Data commands.