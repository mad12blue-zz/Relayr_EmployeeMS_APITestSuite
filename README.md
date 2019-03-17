# Relayr Employee Management System APITestSuite

Step by step instructions to execute the test suite:

1. Open terminal on mac

2. Clone the repository
$ git clone https://github.com/mad12blue/Relayr_EmployeeMS_APITestSuite.git

3. Navigate into the above cloned directory
$ cd Relayr_EmployeeMS_APITestSuite

4. Install pytest
$ pip install pytest

5. Install pytest-bdd for gherkin styling
$ pip install pytest-bdd

6. Install pytest-html for html reporting
$ pip install pytest-html

7. Run the below command to execute the test suite
$ TestNow=`date +%d-%m-%Y_%H.%M.%S` && py.test -v -s --cucumberjson=results/$TestNow-Log.txt --html=results/$TestNow-Report.html 

8. To run the tests in parallel threads (2)
$ TestNow=`date +%d-%m-%Y_%H.%M.%S` && py.test -v -s -n 2 --cucumberjson=results/$TestNow-Log.txt --html=results/$TestNow-Report.html 

9. Once the tests have started, progress and brief summary of execution can be seen on the terminal in human readable format as shown below

![Alt text](/ReadmeImages/TerminalSummary_rlr.png?raw=true "Terminal Summary")

10. Once the test execution is complete, HTML report and Log gets generated in "Relayr_EmployeeMS_APITestSuite/results" folder

![Alt text](/ReadmeImages/ReportFolder_rlr.png?raw=true "Report Folder")

11. Navigate to "Relayr_EmployeeMS_APITestSuite/results" folder and open "<timeStamp>-Log.log" file to view the latest test execution logs in detail

![Alt text](/ReadmeImages/Log_rlr.png?raw=true "Report HTML")

12. Navigate to "Relayr_EmployeeMS_APITestSuite/results" folder and open "<timeStamp>-Report.html" file in your favourite browser to view the latest test execution report in detail

![Alt text](/ReadmeImages/ReportHTML_rlr.png?raw=true "Report HTML")


