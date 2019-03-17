Feature: Employee Management System
    A rest api service to maintain your employee records.

Scenario: List all employees in the employee management system
    Given the employee management service is up and running
    When I fetch all employees in page 1 of the system
    Then I should see 3 employees returned

Scenario: Add an employee into the employee management system
    Given the employee management service is up and running
    When I add Madhan who is a QAE into the system
    Then I should see Madhan added in the list of employees

Scenario: Update an employee in the employee management system
    Given the employee management service is up and running
    And there exists an employee with id 2 in the system
    When I update the name and job of employee with id 2 as Madhan and QAE in the system
    Then I should see name and job updated as Madhan and QAE added

Scenario: Delete an employee from the employee management system
    Given the employee management service is up and running
    And there exists an employee with id 2 in the system
    When I delete an employee with id 2 from the system
    Then I should see employee with id 2 deleted from the system
    