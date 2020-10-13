from selenium.webdriver.common.by import By


class AccountCreationPageLocators():
    ACCOUNT_CREATION_FORM = (By.CSS_SELECTOR, "#account-creation_form")
    CUSTOMER_FIRSTNAME = (By.CSS_SELECTOR, "#customer_firstname")
    CUSTOMER_LASTNAME = (By.CSS_SELECTOR, "#customer_lastname")
    PASSWORD = (By.CSS_SELECTOR, "#passwd")
    ADDRESS = (By.CSS_SELECTOR, "#address1")
    CITY = (By.CSS_SELECTOR, "#city")
    DROPDOWN_STATE = (By.CSS_SELECTOR, "#id_state")
    ZIP_CODE = (By.CSS_SELECTOR, "#postcode")
    PHONE = (By.CSS_SELECTOR, "#phone_mobile")
    SUBMIT_ACCOUNT = (By.CSS_SELECTOR, "#submitAccount")
    FIRSTNAME_VALID = (By.CSS_SELECTOR, ".form-ok #customer_firstname")
    LASTNAME_VALID = (By.CSS_SELECTOR, ".form-ok #customer_lastname")
    PASSWORD_VALID = (By.CSS_SELECTOR, ".form-ok #passwd")
    ALERT_DANGER = (By.CSS_SELECTOR, ".alert.alert-danger")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".info-account")


class BasePageLocators():
    SIGN_IN_LINK = (By.CSS_SELECTOR, ".login")


class MyAccountPageLocators():
    CREATE_ACCOUNT_FORM = (By.CSS_SELECTOR, "#create-account_form")
    EMAIL_CREATE_FILD = (By.CSS_SELECTOR, "#email_create")
    SUBMIT_CREATE_BUTTON = (By.CSS_SELECTOR, "#SubmitCreate")
    EMAIL_VALID = (By.CSS_SELECTOR, ".form-group.form-ok")
