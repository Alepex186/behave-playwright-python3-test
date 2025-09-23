from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv
from faker import Faker

from pages.CartPage import CartPage
from pages.ContactUsPage import ContactUsPage
from pages.HomePage import HomePage
from pages.LogOutPage import LogOutPage
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.RegisterPage import RegisterPage
from pages.SearchProductPage import SearchProductPage
from pages.SubscriptionPage import SubscriptionPage
from pages.TestCasesPage import TestCasesPage

load_dotenv()

BROWSER = os.environ.get("browser","chromium").lower()
HEADLESS = os.environ.get("headless", "false").lower() == "true"
HOME_PAGE_URL=os.environ.get("HOME_PAGE_URL","https://www.automationexercise.com/")

def before_all(context):
    context.playwright=sync_playwright().start()
    context.faker=Faker()
    context.HOME_PAGE_URL=HOME_PAGE_URL

    print(bool(HEADLESS))


    if(BROWSER=="chromium"):
        context.browser=context.playwright.chromium.launch(headless=bool(HEADLESS))
    elif(BROWSER=="firefox"):
        context.browser=context.playwright.firefox.launch(headless=bool(HEADLESS))
    else:
        raise ValueError("EL NEVEGADOR QUE DEFINISTES NO ES VALIDO")


def before_scenario(context,scenario):
    context.browser_context=context.browser.new_context()
    context.page=context.browser_context.new_page()

    context.home_page=HomePage(context)
    context.login_page=LoginPage(context)
    context.register_page=RegisterPage(context)
    context.log_out_page=LogOutPage(context)
    context.contact_us_page=ContactUsPage(context)
    context.test_cases_page=TestCasesPage(context)
    context.products_page=ProductsPage(context)
    context.search_product_page=SearchProductPage(context)
    context.subscription_page=SubscriptionPage(context)
    context.cart_page=CartPage(context)

def after_scenario(context,scenario):
    context.page.close()
    context.browser_context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()

