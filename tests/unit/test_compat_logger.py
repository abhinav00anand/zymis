from aiswarm.utils.compat_log import get_logger


def test_get_logger_returns_structlog_logger():
    """Ensure get_logger returns a structlog logger with expected methods.

    The logger should expose the standard logging methods and allow calls without
    raising exceptions. This test validates the public contract of the utility.
    """
    logger_name = "test_logger"
    logger = get_logger(logger_name)

    # Verify that the returned object has the typical logging methods.
    for method_name in ("debug", "info", "warning", "error", "critical"):
        assert hasattr(logger, method_name), f"Logger missing method {method_name}"
        # Call the method with a simple message to ensure it does not raise.
        getattr(logger, method_name)(f"{method_name} message from {logger_name}")

    # The logger should retain the name it was created with (if the implementation
    # binds it as a context variable). This is optional but useful for debugging.
    # Some structlog configurations expose the name via a bound attribute.
    if hasattr(logger, "_name"):
        assert logger._name == logger_name
