import allure


def microservice(name):
    return allure.label("msrv", name)


def owner(name):
    return allure.label("owner", name)


def layer(name):
    return allure.label("layer", name)


def tm4j(issue):
    return allure.label("tm4j", issue)


def jira_issues(*issues):
    return allure.label("jira", *issues)
