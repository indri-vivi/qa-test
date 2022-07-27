## Indriani Test

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): #login with the correct username and passowrd

        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the site
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)

    def test_b_login_with_blank_input(self): #login with no input 

        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the site
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)
        response_message = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text #find the response message
        self.assertEqual(response_message, "Epic sadface: Username is required") # validate the message
        time.sleep(2)

    def test_c_login_with_wrong_username(self): #login with wrong username

        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the site
        driver.find_element(By.ID,"user-name").send_keys("standardice_user") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)
        response_message = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text #find the response message
        self.assertEqual(response_message, "Epic sadface: Username and password do not match any user in this service")  # validate the message
        time.sleep(2)

    def test_d_locked_out_user(self): #login with the lock out user
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the site
        driver.find_element(By.ID,"user-name").send_keys("locked_out_user") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)
        response_message = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text #find the response message
        self.assertEqual(response_message, "Epic sadface: Sorry, this user has been locked out.")  # validate the message
        time.sleep(2)


    def test_e_open_product_detail(self): # open the product detail
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the sites
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # fill  username
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # fill  password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/a/img").click() # open the product detail 
        time.sleep(3)

    def test_f_add_to_cart(self): # add to cart from the product detail
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the sites
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # fill  username
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # fill  password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/a/img").click() # open the product detail 
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[2]/button").click() #click the add to cart button
        time.sleep(2)

    def test_g_add_to_cart_2(self): # add to cart from catalogue
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the sites
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # fill  username
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # fill  password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click() # add to cart 
        time.sleep(3)

    def test_h_open_the_cart_2(self): # open the cart
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # open the sites
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # fill  username
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # fill  password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click() # add to cart 
        time.sleep(3)
        driver.find_element(By.ID,"shopping_cart_container").click() # open the cart
        time.sleep(2)

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()