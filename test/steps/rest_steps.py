import allure

ISSUE = 10


@allure.step("Create issue with title `{title}`")
def create_issue_with_title(owner, repo, title):
    with allure.step(f"POST /repos/{owner}/{repo}/issues"):
        pass


@allure.step("Close issue with title `{title}`")
def close_issue_with_title(owner, repo, title):
    with allure.step(f"GET /repos/{owner}/{repo}/issues?text={title}"):
        pass
    with allure.step(f"PATCH /repos/{owner}/{repo}/issues/{ISSUE}"):
        pass


@allure.step("Check note with content `{title}` exists")
def should_see_issue_with_title(owner, repo, title):
    with allure.step(f"GET /repos/{owner}/{repo}/issues?text={title}"):
        pass
    with allure.step(f"GET /repos/{owner}/{repo}/issues/{ISSUE}"):
        pass

