# Required imports used in the test suite
import pytest
import requests
import json
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


'''SCENARIO'S'''

# Scenario implementation to GET all employees
@scenario('employee.feature', 'List all employees in the employee management system')
def test_scenario_list_employees():
    pass

# Scenario implementation to POST an employee
@scenario('employee.feature', 'Add an employee into the employee management system')
def test_scenario_add_employee():
    pass

# Scenario implementation to PUT an employee
@scenario('employee.feature', 'Update an employee in the employee management system')
def test_scenario_update_employee():
    pass

# Scenario implementation to DELETE an employee
@scenario('employee.feature', 'Delete an employee from the employee management system')
def test_scenario_delete_employee():
    pass


'''GIVEN'S (Pre-condition)'''

# Given implementation is a pre-condition to check if the service is up and running
@given('the employee management service is up and running')
def given_service_running(container_url):
    url = container_url
    resp = requests.get(url)
    assert resp.status_code == 200

# Given implementation is a pre-condition to check if the employee ID exists in the system
@given(parsers.parse('there exists an employee with id {empId:d} in the system'))
def given_employee_id(service_url, empId):
    url = service_url + "/users/" + str(empId)
    resp = requests.get(url)
    j = json.loads(resp.text)
    assert resp.status_code == 200
    assert j['data']['id'] == empId


'''WHEN'S (Action)'''

# When implementation is an action to get all employees in a particular page in the system
@when(parsers.parse('I fetch all employees in page {page:d} of the system'))
def when_fetch_employees_page(service_url, page, context):
    url = service_url + "/users?page=" + str(page)
    resp = requests.get(url)
    j = json.loads(resp.text)
    assert resp.status_code == 200
    context['empAll'] = j

# When implementation is an action to add a employee with his job into the system
@when(parsers.parse('I add {empName:l} who is a {empJob:l} into the system'))
def when_add_user(service_url, empName, empJob, context):
    url = service_url + "/users"
    data = {
            "name": empName,
            "job": empJob
            }
    resp = requests.post(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 201
    assert j['id'] is not None
    assert j['job'] == empJob
    context['empNew'] = j

# When implementation is an action to update the name and job of an employee in the system
@when(parsers.parse('I update the name and job of employee with id {empId:d} as {empName:l} and {empJob:l} in the system'))
def when_update_user(service_url, empId, empName, empJob, context):
    url = service_url + "/users/" + str(empId)
    data = {
            "name": empName,
            "job": empJob
            }
    resp = requests.put(url, data=data)
    j = json.loads(resp.text)
    assert resp.status_code == 200
    context['empUpd'] = j

# When implementation is an action to delete an employee in the system
@when(parsers.parse('I delete an employee with id {empId:d} from the system'))
def when_delete_user(service_url, empId, context):
    url = service_url + "/users/" + str(empId)
    resp = requests.delete(url)
    assert resp.status_code == 204
    context['empDel'] = resp.status_code


'''THEN'S (Verification)''' 

# Then implementation is a verification to check the employees returned from the system
@then(parsers.parse('I should see {emps:d} employees returned'))
def then_all_employees(emps, context):
    assert len(context['empAll']['data']) == emps

# Then implementation is a verification to check if the employee is added in the system
@then(parsers.parse('I should see {empName:l} added in the list of employees'))
def then_employee_added(empName, context):
    assert context['empNew']['name'] == empName
    '''
    the dummy api used doesn't actually add the user to the system
    hence only status code verification is done after add
    If it would actually add the user then we can query/get the list to check if the user is actually added
    '''

# Then implementation is a verification to check the employee name and job updated in the system
@then(parsers.parse('I should see name and job updated as {empName:l} and {empJob:l} added'))
def then_employee_updated(empName, empJob, context):
    assert context['empUpd']['name'] == empName
    assert context['empUpd']['job'] == empJob
    '''
    the dummy api used doesn't actually update the user in the system
    hence only status code verification is done after update
    If it would actually update the user then we can query/get the list to check if the user is actually updated
    '''

# Then implementation is a verification to check the employee is deleted from the system
@then(parsers.parse('I should see employee with id {empId:d} deleted from the system'))
def then_employee_deleted(empId, context):
    assert context['empDel'] == 204
    '''
    the dummy api used doesn't actually delete the user from the system
    hence only status code verification is done after delete
    If it would actually delete the user then we can query/get the list to check if the user is actually removed
    '''