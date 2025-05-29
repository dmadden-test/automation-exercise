from behave import given, step, when, then
from faker import Faker
from features.config.utils import create_new_user


@given("the user is on the homepage")
def step_impl(context):
    context.page.goto("https://automationexercise.com")

    assert context.page.title() == "Automation Exercise"


@step("the user selects the Signup/Login link")
def step_impl(context):
    context.page.click("a[href='/login']")


@when("the user enters their details")
def step_impl(context):
    # New User Signup
    faker = Faker()
    password = faker.password()
    email = faker.email()
    context.new_user = create_new_user(email, password)

    context.page.get_by_placeholder("Name").fill(context.new_user.get("name"))
    context.page.locator("input[data-qa='signup-email']").fill(email)
    context.page.click("button[data-qa='signup-button']")

    # Enter Account Information
    account_info = context.page.locator("//2[contains('Information')]")
    assert account_info is not None

    context.page.click("input#id_gender1")
    context.page.locator("input#password").fill(password)

    # DoB
    context.page.locator("select#days").select_option("9")
    context.page.locator("select#months").select_option("9")
    context.page.locator("select#years").select_option("1977")

    context.page.get_by_role("textbox", name="First name *").fill(
        context.new_user.get("firstname")
    )
    context.page.get_by_role("textbox", name="Last name *").fill(
        context.new_user.get("lastname")
    )
    context.page.get_by_role("textbox", name="Company", exact=True).fill(
        context.new_user.get("Company")
    )
    context.page.get_by_role("textbox", name="Address * (Street address, P.").fill(
        context.new_user.get("address1")
    )
    context.page.get_by_role("textbox", name="Address 2").fill(
        context.new_user.get("address2")
    )
    context.page.get_by_label("Country *").select_option("New Zealand")
    context.page.get_by_role("textbox", name="State *").fill(
        context.new_user.get("state")
    )
    context.page.get_by_role("textbox", name="City *").fill(
        context.new_user.get("city")
    )
    context.page.locator("#zipcode").fill(context.new_user.get("zipcode"))
    context.page.get_by_role("textbox", name="Mobile Number *").fill(
        context.new_user.get("mobile_number")
    )
    context.page.get_by_role("button", name="Create Account").click()
    context.page.get_by_role("link", name="Continue").click()
