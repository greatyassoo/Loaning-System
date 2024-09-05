You are required to create an application to manage bank loans. The bank should receive funds from loan providers and be able to lend its customers within the limit of total funds. A user should be able to login to the system through a username and password. You have 3 user roles that you need to account for:



Description:

    Loan Provider: Should represent the total budget of the loans

    Loan Customer: Should represent the loan, loan’s term and the loan’s amount

    The Bank Personnel: Should define max and min amounts, interest rate, duration for each loan



Endpoints:

Loan Providers:

    View status of loan fund applications. 

Loan Customers:

    View status of loan applications.

    Make payments for his loans

The Bank Personnel:

    View applications from loan providers and customers and be able to above.

    The system should always make sure that the total loans should not exceed the total funds.


Elicitated requirments:

    Loan Provider:
        - Should be able to view the status of loan fund applications  [DONE]
        - create a loan fund application  [DONE]

    Loan Customer:
        - Should be able to view the status of loan applications
        - Make payments for his loans
        - create a loan application
    
    Bank Personnel:
        - View applications from loan providers and customers
        - View status of loan fund applications
        - View status of loan applications
        - Approve or reject loan fund applications
        - Approve or reject loan applications
        - Define max and min amounts, interest rate, duration for each loan
        