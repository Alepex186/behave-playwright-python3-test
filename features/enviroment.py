from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv



load_dotenv()

BROWSER = os.environ.get("browser","chromium").lower()
HEADLESS = os.environ.get("headless","False")


def before_all(context):
    context.playwright=sync_playwright().start()

    if(BROWSER=="chromium"):
        context.browser=context.playwright.chromium.launch(headless=bool(HEADLESS))
    elif(BROWSER=="firefox"):
        context.browser=context.playwright.firefox.launch(headless=bool(HEADLESS))
    else:
        raise ValueError("EL NEVEGADOR QUE DEFINISTES NO ES VALIDO")


def before_scenario(context,scenario):
    context.browser_context=context.browser.new_context()
    context.page=context.browser_context.new_page()


def after_scenario(context,scenario):
    context.page.close()
    context.browser_context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()

