def start_driver(account):
    """Starts a driver for the given account.

    Args:
        account: The account to start the driver for.

    Returns:
        The started driver.
    """

    driver = webdriver.Chrome()
    driver.get(account.url)
    driver.implicitly_wait(10)
    return driver

