# Feature EMS service is used to maintain employee/user data in a REST based backend service
Feature: Employee Management System
    A rest api service to maintain your employee records.

# Scenario to fetch all employees page wise by providing the page number
Scenario: List all employees in the employee management system
    Given the employee management service is up and running
    When I fetch all employees in page 1 of the system
    Then I should see 3 employees returned

# Scenario to add a new employee by providing Name and Job to add
Scenario: Add an employee into the employee management system
    Given the employee management service is up and running
    When I add Madhan who is a QAE into the system
    Then I should see Madhan added in the list of employees

# Scenario to update an exisiting employee by providing Name and Job to update
Scenario: Update an employee in the employee management system
    Given the employee management service is up and running
    And there exists an employee with id 2 in the system
    When I update the name and job of employee with id 2 as Madhan and QAE in the system
    Then I should see name and job updated as Madhan and QAE added

# Scenario to remove an exisiting employee by providing the ID to delete
Scenario: Delete an employee from the employee management system
    Given the employee management service is up and running
    And there exists an employee with id 2 in the system
    When I delete an employee with id 2 from the system
    Then I should see employee with id 2 deleted from the system
    