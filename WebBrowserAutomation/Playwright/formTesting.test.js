const { chromium } = require('playwright');
const LoginPage = require('./loginPage.js');

describe('login testing', () =>{

    let browser = null;
    let page = null;
    let context = null;
    let loginPage = null;

    beforeAll(async() =>{
        browser = await chromium.launch({headless: false});
        context = await browser.newContext();
        page = await context.newPage();
        loginPage = new LoginPage(page);
        await loginPage.navigate();
    });

    afterAll(async() => {
        await browser.close();
    });

    test('should load page', async() =>{
        expect(page).not.toBeNull();
        expect(await page.title()).not.toBeNull();
    });

    test('should enter user information', async() =>{
        await loginPage.login('tomsmith', 'SuperSecretPassword!');
        expect(await page.title()).not.toBeNull();
    });
});