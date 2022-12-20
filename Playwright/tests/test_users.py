from playwright.sync_api import Page, expect

def test_user(page: Page):
    page.goto('http://users.bugred.ru/user/register/index')
    page.fill('input[name ="name"]', 'test.test')
    page.fill('input[name ="email"]', 'test.test@mail.ru') 
    page.fill('input[name ="password"]', 'test.test')
    page.click('input[type=submit]')