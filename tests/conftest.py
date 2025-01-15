import os
import pytest
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from api.auth import Auth


def get_worker_id(request):
    """Get the worker ID from pytest-xdist or return None for single-process runs"""
    try:
        worker_id = request.node.config.workerinput['workerid']
        return worker_id
    except (AttributeError, KeyError):
        return 'master'


@pytest.fixture(scope="function")
def logger(request):
    """Create a worker-specific logger instance"""
    worker_id = get_worker_id(request)
    return Logger().get_logger(worker_id)


@pytest.fixture(scope="function")
def driver(request, logger):
    worker_id = get_worker_id(request)
    logger.info(f"Running test in worker: {worker_id}")

    browser = request.config.getoption("--browser", default="chrome").lower()
    headless = request.config.getoption("--headless", default="true").lower() == "true"
    factory = DriverFactory(browser, headless, logger)
    driver_instance = factory.get_driver()

    driver_instance.implicitly_wait(10)
    driver_instance.maximize_window()

    yield driver_instance

    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item):
    """Wrapper to ensure proper test boundary logging"""
    worker_id = get_worker_id(item._request)
    logger = Logger().get_logger(worker_id)

    # Log test start
    logger.info(f"{'#' * 10} Test {item.nodeid} started {'#' * 10}")

    # Run the test
    yield

    # Log test end
    logger.info(f"{'#' * 10} Test {item.nodeid} ended {'#' * 10}")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests (e.g., chrome, firefox).",
    )
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="Run tests in headless mode (true/false). Default is true.",
    )


@pytest.fixture(scope="session")
def no_gui_login(driver, logger):
    try:
        response = Auth.login()
        token = response["token"]
        user_id = response["userDetails"]["userId"]

        driver.get(os.getenv('URL'))
        driver.execute_script(f"window.localStorage.setItem('authToken', '{token}');")
        driver.execute_script(f"window.localStorage.setItem('userId', '{user_id}');")
        driver.refresh()

        logger.info("No GUI Login is successful")
        return driver

    except KeyError as e:
        logger.error(f"KeyError occurred while extracting values from response: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"An error occurred during no GUI login: {str(e)}")
        raise