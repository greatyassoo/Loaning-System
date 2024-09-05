## Description:

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


## Elicitated requirments:

### Loan Provider:
        - Should be able to view the status of loan fund applications  [DONE]
        - create a loan fund application  [DONE]

### Loan Customer:
        - Should be able to view the status of loan applications  [DONE]
        - Make payments for his loans
        - create a loan application [DONE]
    
### Bank Personnel:
        - View applications from loan providers and customers  [DONE]
        - View status of loan fund applications  [DONE]
        - View status of loan applications  [DONE]
        - Approve or reject loan fund applications  [DONE]
        - Approve or reject loan applications  [DONE]
        - Define interest rate, duration for each loan [DONE]


## Assumptions:  
### Loan Customer
#### Loan Application, Loans, and Payments
- The customer first signs up for a Loan Application
- Then if It's approved by the Bank Staff then a Loan record is automatically created in the database with the appropriate fields
- Payments are done through a payment endpoint where the customer just calls it to add a payment  

### Bank 
The Bank `total_funds` is stored in the database and is
  - incremented when:
    - Approval of **Loan Fund Application**
    - Customer **Payment** occurs
  - decremented when:
    - Approval of **Loan Application**

The system keeps track of this value through all transactions, making sure that the is always sufficient amount of funds in place


### Bank Staff
The Bank Staff can view all applications from either customers or loan providers. A staff member can then choose to approve
or deny any of the applications whether that be a **Loan Fund Application** or **Loan Application**

Approval of a **Loan Application** is done after the system checking if there are sufficient funds in the bank.
After that, a **Loan** record is created in the database with the specified `interest_rate` and `duration`. 

Payments of this loan should be calculated as follows:
    
> payment = ((loan_amount * interest_rate) + loan_amount) / duration_in_months


