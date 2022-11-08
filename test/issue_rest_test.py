import allure
import pytest
from .steps import rest_steps as steps
from .marks import microservice, layer, owner, tm4j, jira_issues

pytestmark = [
    layer("rest"),
    owner("baev"),
    allure.feature("Issues")
]

OWNER = "allure-framework"
REPO = "allure2"


@tm4j("AE-T1")
@allure.title("Create issue via api")
@allure.story("Create new issue")
@microservice("Billing")
@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.parametrize("owner", [OWNER])
@pytest.mark.parametrize("repo", [REPO])
@pytest.mark.parametrize("title", ["First Note", "Second Note"])
def test_should_create_user_note(owner, repo, title):
    steps.create_issue_with_title(owner, repo, title)
    steps.should_see_issue_with_title(owner, repo, title)


@tm4j("AE-T2")
@jira_issues("AE-1")
@allure.title("Close issue via api")
@allure.story("Close existing issue")
@microservice("Repository")
@pytest.mark.web
@pytest.mark.regress
@pytest.mark.parametrize("owner", [OWNER])
@pytest.mark.parametrize("repo", [REPO])
@pytest.mark.parametrize("title", ["First Note", "Second Note"])
def test_should_delete_user_note(owner, repo, title):
    steps.create_issue_with_title(owner, repo, title)
    steps.close_issue_with_title(owner, repo, title)

