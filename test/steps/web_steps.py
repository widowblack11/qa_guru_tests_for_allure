import os
import time
import random
import pytest
import allure

this_path = os.path.dirname(os.path.realpath(__file__))
index_html_path = os.path.join(this_path, "../resource/index.html");


@allure.step("Starting web driver")
def start_driver():
    maybe_throw_selenium_timeout_exception()


@allure.step("Stopping web driver")
def stop_driver():
    maybe_throw_selenium_timeout_exception()


@allure.step("Open issues page `{owner}/{repo}`")
def open_issues_page(owner, repo):
    allure.attach.file(index_html_path, "page")
    maybe_throw_element_not_found_exception()


@allure.step("Open pull requests page `{owner}/{repo}`")
def open_pull_requests_page(owner, repo):
    allure.attach.file(index_html_path, "page")
    maybe_throw_element_not_found_exception()


@allure.step("Create pull request from branch `{branch}`")
def create_pull_request_from_branch(branch):
    maybe_throw_element_not_found_exception()


@allure.step("Create issue with title `{title}`")
def create_issue_with_title(title):
    maybe_throw_assertion_exception(title)


@allure.step("Close pull request for branch `{branch}`")
def close_pull_request_for_branch(branch):
    maybe_throw_assertion_exception(branch)


@allure.step("Close issue with title `{title}`")
def close_issue_with_title(title):
    maybe_throw_assertion_exception(title)


@allure.step("Check pull request for branch `{branch}` exists")
def should_see_pull_request_for_branch(branch):
    maybe_throw_assertion_exception(branch)


@allure.step("Check issue with title `{title}` exists")
def should_see_issue_with_title(title):
    maybe_throw_assertion_exception(title)


@allure.step("Check pull request for branch `{branch}` not exists")
def should_not_see_pull_request_for_branch(branch):
    maybe_throw_assertion_exception(branch)


@allure.step("Check issue with title `{title}` not exists")
def should_not_see_issue_with_title(title):
    maybe_throw_assertion_exception(title)

def is_time_to_trow_exception():
    return random.choice([False, True]) and random.choice([False, True]) and random.choice([False, True])


def maybe_throw_selenium_timeout_exception():
    if is_time_to_trow_exception():
        pytest.fail(web_driver_is_not_reachable.format(text="Allure"))


def maybe_throw_element_not_found_exception():
    time.sleep(1)
    if is_time_to_trow_exception():
        pytest.fail(element_not_found_message.format(selector="[//div[@class='something']]"))


def maybe_throw_assertion_exception(text):
    if is_time_to_trow_exception():
        pytest.fail(text_equal.format(expected=text, actual="another text"))


web_driver_is_not_reachable = """WebDriverException: chrome not reachable
Element not found {{By.xpath: //a[@href='/eroshenkoam/allure-example']}}
Expected: text '{text}'
Page source: file:/Users/eroshenkoam/Developer/eroshenkoam/webdriver-coverage-example/build/reports/tests/1603973861960.0.html
Timeout: 4 s."""

text_equal = """Element should text '{expected}' {{By.xpath: //a[@href='/eroshenkoam/allure-example']}}
Element: '<a class=\"v-align-middle\">{actual}</a>'
Screenshot: file:/Users/eroshenkoam/Developer/eroshenkoam/webdriver-coverage-example/build/reports/tests/1603973703632.0.png
Page source: file:/Users/eroshenkoam/Developer/eroshenkoam/webdriver-coverage-example/build/reports/tests/1603973703632.0.html
Timeout: 4 s."""

element_not_found_message = """Element not found {{By.xpath: {selector}}}
Expected: visible or transparent: visible or have css value opacity=0
Screenshot: file:/Users/eroshenkoam/Developer/eroshenkoam/webdriver-coverage-example/build/reports/tests/1603973516437.0.png
Page source: file:/Users/eroshenkoam/Developer/eroshenkoam/webdriver-coverage-example/build/reports/tests/1603973516437.0.html
Timeout: 4 s."""