Step1:
Run Setup.py file using "pip install -e ."

Step2.
Create a .gitnore file and add all the file related to python which has to be ignored
and commit that file.
Once it is commited, as part of git status, it will not show any files which has been
added as part of .gitignore.

Step3:
Create a folder for the Project
Create A virtualEnv using virtualenv <venv> name (also can specify what is the python version)
Open the folder 
Active the virtual env 
install all the dependcies.
collect the requirement.txt
push the file to the remote repo.
Add the folder structure and push

Step4:
How to configur the allure reports.
First install "pip install allure-pytest"
https://pypi.org/project/allure-pytest/
Second
pytest --alluredir=%allure_result_folder% ./tests
allure serve %allure_result_folder%
set allure_result_folder="C:\PROJECTS_GITHUB\API_Framework_Development_Draft_Demo1\Reports"
