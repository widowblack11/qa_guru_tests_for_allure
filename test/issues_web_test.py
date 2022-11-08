import allure
import pytest
from .steps import web_steps as steps
from .marks import microservice, layer, owner, tm4j, jira_issues


pytestmark = [
    layer("web"),
    owner("eroshenkoam"),
    allure.feature("Issues")
]

OWNER = "allure-framework"
REPO = "allure2"
ISSUE_TITLE = "Some issue title here"


@pytest.fixture(scope="module")
def web_driver():
    steps.start_driver()
    yield
    steps.stop_driver()


@tm4j("AE-T3")
@microservice("Billing")
@allure.story("Create new issue")
@jira_issues("AE-2")
@pytest.mark.web
@pytest.mark.critical
@allure.title("Creating new issue authorized user")
def test_should_create_issue(web_driver):
    steps.open_issues_page(OWNER, REPO)
    steps.create_issue_with_title(ISSUE_TITLE)
    steps.should_see_issue_with_title(ISSUE_TITLE)


@tm4j("AE-T4")
@microservice("Repository")
@allure.story("Create new issue")
@jira_issues("AE-1")
@pytest.mark.web
@pytest.mark.regress
@allure.title("Adding note to advertisement")
def test_should_create_issue(web_driver):
    steps.open_issues_page(OWNER, REPO)
    steps.create_issue_with_title(ISSUE_TITLE)
    steps.should_see_issue_with_title(ISSUE_TITLE)


@tm4j("AE-T5")
@microservice("Repository")
@allure.story("Close existing issue")
@jira_issues("AE-1")
@pytest.mark.web
@pytest.mark.regress
@allure.title("Closing new issue for authorized user")
def test_should_create_issue(web_driver):
    steps.open_issues_page(OWNER, REPO)
    steps.create_issue_with_title(ISSUE_TITLE)
    steps.close_issue_with_title(ISSUE_TITLE)
    steps.should_see_issue_with_title(ISSUE_TITLE)
