
# Automation Exercise

## BDD - API & UI
This practice project includes API and UI tests which have been written using Behave for Python against the automation website: https://automationexercise.com/

### Create a virtual environment and install dependencies

````
python3 -m venv autopractice_venv
source autopractice_venv/bin/activate

pip install -r requirements.txt
add .env -- Replace your ENV'S.
````

### Environment Variables

The project contains a ``.env`` file

#### Environment variable for API
1. **BASE_URL**


## Testing

### Run the QA test automation
In terminal execute:
```
behave
```

### Generate Allure report for automation
To install allure:
```
pip install allure-behave
brew install allure
```
Run behave with allure:
```
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```
Move into features directory and generate report:
```
cd features
allure generate
```
Open HTML report:
```
allure open allure-report --host localhost --port 53276  
```
