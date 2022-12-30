# Conftest -  Fișier de tip config pentru configurarea testelor. Acest config file va fi modificat în timp, aducând
# îmbunătățiri substanțiale și analize obiective asupra testelor rulate

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):  # add-option, it's not a typo
    parser.addoption("--browser_name", action="store", default="Chrome", help="command info")


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("browser_name")

    if browser_name == "Chrome":
        service_obj = Service \
            ("C:/Users/Bulzan's Omen/PycharmProjects/Bulzan_TAZZ_AUTOMATION/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "Edge":
        service_obj = Service \
            ("C:/Users/Bulzan's Omen/PycharmProjects/Bulzan_TAZZ_AUTOMATION/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    else:
        print("Browser not available or installed. Check the webdrivers and also if the browser is properly installed")

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://tazz.ro")

    request.cls.driver = driver

    yield

    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# Run with this: 'pytest --html=report.html' in order to generate a report

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
