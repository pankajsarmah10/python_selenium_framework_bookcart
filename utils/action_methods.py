import time
from selenium.common.exceptions import WebDriverException
from utils.logger import Logger

logger = Logger().get_logger()

def find_element_with_retry(driver, by, value, retries=3, delay=1):
    attempt = 0
    while attempt < retries:
        try:
            element = driver.find_element(by, value)
            logger.info(f"Element found: {value}")
            return element
        except WebDriverException as e:
            attempt += 1
            logger.error(f"Error finding element {value}: {e}. Retrying ({attempt}/{retries}) ...")
            time.sleep(delay)
    logger.error(f"Failed to find element {value} after {retries} attempts.")
    raise Exception(f"Failed to find element {value} after {retries} attempts.")

def click_element(driver, by, value, retries=3, delay=1):
    """
    Tries to click an element with retries and error handling.
    """
    attempt = 0
    while attempt < retries:
        try:
            element = find_element_with_retry(driver, by, value)
            element.click()
            logger.info(f"Clicked on element: {value}")
            return
        except WebDriverException as e:
            attempt += 1
            logger.error(f"Error clicking element {value}: {e}. Retrying ({attempt}/{retries})...")
            time.sleep(delay)
    logger.error(f"Failed to click on element {value} after {retries} attempts.")
    raise Exception(f"Failed to click element {value} after {retries} attempts.")

def send_keys_to_element(driver, by, value, text, retries=3, delay=1):
    """
    Tries to send keys to an element with retries and error handling.
    """
    attempt = 0
    while attempt < retries:
        try:
            element = find_element_with_retry(driver, by, value)
            element.send_keys(text)
            logger.info(f"Sent text to element: {value}")
            return
        except WebDriverException as e:
            attempt += 1
            logger.error(f"Error sending keys to element {value}: {e}. Retrying ({attempt}/{retries})...")
            time.sleep(delay)
    logger.error(f"Failed to send keys to element {value} after {retries} attempts.")
    raise Exception(f"Failed to send keys to element {value} after {retries} attempts.")

def get_text_from_element(driver, by, value, retries=3, delay=1):
    attempt = 0
    while attempt < retries:
        try:
            element = find_element_with_retry(driver, by, value)
            text_val = element.text.strip()
            logger.info(f"Got text {text_val} from element: {value}")
            return text_val
        except WebDriverException as e:
            attempt += 1
            logger.error(f"Error retrieving text from element {value}: {e}. Retrying ({attempt}/{retries})...")
            time.sleep(delay)
    logger.error(f"Failed to retrieve text from element {value} after {retries} attempts.")
    raise Exception(f"Failed to retrieve text from element {value} after {retries} attempts.")