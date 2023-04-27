from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random

prod_URLS = [
    {
        "env": "Prod",
        "url": "https://www.geeksforgeeks.org/",
        "element": "hslider",
        "expected_value": "Trending NowDSAData StructuresAlgorithmsInterview PreparationData ScienceTopic-wise PracticeCC++JavaJavaScriptPythonCompetitive ProgrammingMachine LearningAptitudeWrite & EarnWeb DevelopmentPuzzlesProjects"
    },
    {
        "env": "Prod",
        "url": "https://www.geeksforgeeks.org/",
        "element": "hslider",
        "expected_value": "Trending StructuresAlgorithmsInterview PreparationData ScienceTopic-wise PracticeCC++JavaJavaScriptPythonCompetitive ProgrammingMachine LearningAptitudeWrite & EarnWeb DevelopmentPuzzlesProjects"
    }]

test_URLS = [
    {
        "env": "Test",
        "url": "https://www.geeksforgeeks.org/",
        "element": "hslider",
        "expected_value": "Trending NowDSAData StructuresAlgorithmsInterview PreparationData ScienceTopic-wise PracticeCC++JavaJavaScriptPythonCompetitive ProgrammingMachine LearningAptitudeWrite & EarnWeb DevelopmentPuzzlesProjects"
    },
    {
        "env": "Test",
        "url": "https://www.geeksforgeeks.org/",
        "element": "hslider",
        "expected_value": "Trending StructuresAlgorithmsInterview PreparationData ScienceTopic-wise PracticeCC++JavaJavaScriptPythonCompetitive ProgrammingMachine LearningAptitudeWrite & EarnWeb DevelopmentPuzzlesProjects"
    }]


results = pd.DataFrame()


def run_tests(number_of_tests, selected_URLS):
    
    results = pd.DataFrame()
    counter = 0

    while counter < number_of_tests:
        test_URL = random.choice(list(selected_URLS))
        print(f"Test {counter} using {test_URL['url']}")

        # create webdriver object
        driver = webdriver.Safari()

        this_url = test_URL["url"]
        this_element = test_URL['element']
        this_expected_value = test_URL['expected_value']
        this_env = test_URL['env']
        outcome = ""

        driver.get(this_url)
        driver.implicitly_wait(2)

        element = driver.find_element(By.ID, this_element)
        value = element.text
        try:
            assert value == this_expected_value
        except:
            outcome = "Failed"
        else:
            outcome = "Passed"

        df_temp = pd.DataFrame(data={'Test Number': [counter], "Environment": [this_env], "URL": [this_url], "Test Result": [outcome]})
        results = pd.concat([results, df_temp])

        driver.close()
        counter +=1
    
    results.to_csv(f'{this_env}_c{number_of_tests}_results.csv', index=False)

run_tests(50, test_URLS)