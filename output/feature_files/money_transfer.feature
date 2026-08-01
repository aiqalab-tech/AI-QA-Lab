Feature: Money Transfer

  Scenario: Verify successful money transfer with valid beneficiary
   Given the customer is logged into ParaBank
   And the customer has sufficient balance
   When the customer performs the transaction
   Then the transaction should be completed successfully

  Scenario: Verify transfer fails with insufficient balance
   Given the customer is logged into ParaBank
   When the customer performs an invalid transaction
   Then an appropriate error message should be displayed

  Scenario: Verify transfer amount validation
   Given the customer is on the transaction page
   When invalid input is entered
   Then validation messages should be displayed

  Scenario: Verify OTP validation during money transfer
   Given the customer initiates a secure transaction
   When an invalid OTP is entered
   Then the transaction should be rejected

