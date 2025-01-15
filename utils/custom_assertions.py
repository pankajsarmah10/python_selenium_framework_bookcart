from assertpy import assert_that
from utils.logger import Logger

class CustomAssertions:
    logger = Logger().get_logger()

    @staticmethod
    def log_assertion(description, success=True):
        """Logs the result of the assertion."""
        if success:
            CustomAssertions.logger.info(f"Assertion Passed: {description}")
        else:
            CustomAssertions.logger.error(f"Assertion Failed: {description}")

    @staticmethod
    def assert_equal(actual, expected, message=None):
        description = f"Expected: {expected}, Actual: {actual}"
        try:
            assert_that(actual).is_equal_to(expected, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_not_equal(actual, unexpected, message=None):
        description = f"Unexpected: {unexpected}, Actual: {actual}"
        try:
            assert_that(actual).is_not_equal_to(unexpected, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_contains(container, item, message=None):
        description = f"Container: {container}, Expected to contain: {item}"
        try:
            assert_that(container).contains(item, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_not_contains(container, item, message=None):
        description = f"Container: {container}, Expected not to contain: {item}"
        try:
            assert_that(container).does_not_contain(item, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_true(value, message=None):
        description = f"Value: {value}, Expected: True"
        try:
            assert_that(value).is_true(description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_false(value, message=None):
        description = f"Value: {value}, Expected: False"
        try:
            assert_that(value).is_false(description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_starts_with(string, prefix, message=None):
        description = f"String: {string}, Expected to start with: {prefix}"
        try:
            assert_that(string).starts_with(prefix, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_ends_with(string, suffix, message=None):
        description = f"String: {string}, Expected to end with: {suffix}"
        try:
            assert_that(string).ends_with(suffix, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_length(container, length, message=None):
        description = f"Container: {container}, Expected length: {length}"
        try:
            assert_that(container).is_length(length, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_greater_than(actual, value, message=None):
        description = f"Actual: {actual}, Expected greater than: {value}"
        try:
            assert_that(actual).is_greater_than(value, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_less_than(actual, value, message=None):
        description = f"Actual: {actual}, Expected less than: {value}"
        try:
            assert_that(actual).is_less_than(value, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_in_range(value, min_value, max_value, message=None):
        description = f"Value: {value}, Expected in range: {min_value} to {max_value}"
        try:
            assert_that(value).is_between(min_value, max_value, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_instance_of(value, type_, message=None):
        description = f"Value: {value}, Expected instance of: {type_}"
        try:
            assert_that(value).is_instance_of(type_, description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_not_none(value, message=None):
        description = f"Value: {value}, Expected not None"
        try:
            assert_that(value).is_not_none(description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_empty(value, message=None):
        description = f"Value: {value}, Expected to be empty"
        try:
            assert_that(value).is_empty(description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise

    @staticmethod
    def assert_not_empty(value, message=None):
        description = f"Value: {value}, Expected not to be empty"
        try:
            assert_that(value).is_not_empty(description=message)
            CustomAssertions.log_assertion(description)
        except AssertionError:
            CustomAssertions.log_assertion(description, success=False)
            raise