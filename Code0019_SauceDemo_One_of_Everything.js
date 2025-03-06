// Code Number 0019
// Function: Check Out One of Everything in SauceDemo
// Browser: Edge
// Author: GPA

// PREREQUISITE CODE (NECESSARY FOR INITIALIZATION) -- do not include in automation test steps

// PRQ 1: Declare variable
const { webkit, chromium, firefox } = require('playwright');

// Main function
(async () => {
    // This launches Edge using the "chromium" engine
    const browser = await chromium.launch({ headless: false, channel: 'msedge' });
    const page = await browser.newPage();

    // AUTOMATION TEST STEPS:

    // Step 1: Go to SauceDemo page.
    await page.goto('https://www.saucedemo.com/');
    await page.waitForTimeout(1000);

    // Step 2: Input email or username.
    await page.waitForSelector('#user-name');
    await page.fill('#user-name', 'standard_user');
    await page.waitForTimeout(1000);

    // Step 3: Input password.
    await page.waitForSelector('#password');
    await page.fill('#password', 'secret_sauce');
    await page.waitForTimeout(1000);

    // Step 4: Click Sign in.
    await page.click('#login-button');
    await page.waitForTimeout(1000);

    // Step 5: Add to cart every item.
    await page.click('#add-to-cart-sauce-labs-bolt-t-shirt');
    await page.click('#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)');
    await page.click('#add-to-cart-sauce-labs-bike-light');
    await page.click('#add-to-cart-sauce-labs-fleece-jacket');
    await page.click('#add-to-cart-sauce-labs-onesie');
    await page.click('#add-to-cart-sauce-labs-backpack');

    // Step 6: Click the cart icon to view the checked-out items.
    await page.click('.shopping_cart_link');
    await page.waitForTimeout(1000);

    // Step 7: Click Checkout.
    await page.click('#checkout');
    await page.waitForTimeout(1000);

    // Step 8: Fill in your First Name, Last Name, and ZIP Code.
    await page.waitForSelector('#first-name');
    await page.fill('#first-name', 'Fe\u00F6d\u00F8\u0159');
    await page.waitForTimeout(1000);

    await page.waitForSelector('#last-name');
    await page.fill('#last-name', 'Dr\u0101\u017E\u00F0\u00E5\u00F1\u00FD');
    await page.waitForTimeout(1000);

    await page.waitForSelector('#postal-code');
    await page.fill('#postal-code', '51881');
    await page.waitForTimeout(1000);

    // Step 9: Click Continue.
    await page.click('#continue');
    await page.waitForTimeout(1000);

    // Step 10: Click Finish.
    await page.click('#finish');
    await page.waitForTimeout(1000);

    // Step 11: Click Back Home.
    await page.click('#back-to-products');
    await page.waitForTimeout(1000);

    // Step X: Prevent the browser from closing.
    console.log("Automation suite completed. Your turn.");
  })();

  // Key Finding: For elements with definite ID, prefix is #, but for XPATH, it's //, and for class, it's '.'.
  // End result: Successful end-to-end checkout of "One of Everything".