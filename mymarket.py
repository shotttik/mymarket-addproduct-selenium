import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import listdir
from os.path import realpath


def clean_txt(lines):
    data = {}
    for line in lines:
        if line.endswith("\n"):
            line = line[:-1]
        k, v = line.split(":")
        data[k] = v
    return data


def get_user_data():
    with open('user.txt') as f:
        lines = f.readlines()
        f.close()
    user_data = clean_txt(lines)
    email = user_data["email"]
    passwd = user_data["password"]
    location = user_data["location"]
    name = user_data["name"]
    phone = user_data["phone"]
    return email, passwd, location, name, phone


def get_item_data():
    with open('item.txt') as f:
        lines = f.readlines()
        f.close()
    item_data = clean_txt(lines)
    condition = item_data["condition"]
    title = item_data["title"]
    description = item_data["description"]
    price = item_data["price"]
    btype = item_data["type"]
    size = item_data["size"]
    return condition, title, description, price, btype, size


def get_website(driver):
    driver.get("https://mymarket.ge")
    warning_btn = driver.find_element(By.CSS_SELECTOR, ".close-popup")
    warning_btn.click()
    time.sleep(2)
    btn = driver.find_element(By.CSS_SELECTOR,
                              ".navbar-nav .add-statement-btn.auth-btn")
    btn.click()
    time.sleep(2)


def get_profile(driver, email, passwd):
    content = driver.find_element(By.CSS_SELECTOR, "#Box")
    email_input = content.find_element(By.CSS_SELECTOR, "#Email")
    email_input.send_keys(email)
    time.sleep(2)
    passwd_input = content.find_element(By.CSS_SELECTOR, "#Password")
    passwd_input.send_keys(passwd)
    time.sleep(2)
    btn_login = content.find_element(By.CSS_SELECTOR, "button.btn")
    btn_login.click()


def get_add_page(driver):
    time.sleep(5)
    three_d = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".burger-mobile"))
    )
    three_d.click()
    time.sleep(2)
    ad_add = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "li.list-group-item:nth-child(1) > a:nth-child(1)"))
    )
    ad_add.click()
    btn_sell = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.p-32px:nth-child(1)"))
    )
    btn_sell.click()


def enter_details(driver, condition: str, title: str, description: str,):
    content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".add-product-boxs"))
    )
    time.sleep(3)
    btn_category = WebDriverWait(content, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#CatID > div > div > div"))
    )
    btn_category.click()
    time.sleep(5)
    sport_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), 'სპორტი და დასვენება')]"))
    )
    sport_btn.click()
    time.sleep(2)
    bicycle_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), 'ველოსიპედი')]"))
    )
    bicycle_btn.click()
    time.sleep(2)
    condition_btn = driver.find_element(By.XPATH,
                                        f"//*[contains(text(), {condition})]")
    condition_btn.click()
    time.sleep(2)
    title_input = driver.find_element(By.CSS_SELECTOR, "#Title_4 > input")
    title_input.send_keys(title)
    time.sleep(2)
    descption_input = driver.find_element(By.CSS_SELECTOR, ".notranslate")
    descption_input.send_keys(description)


def enter_pics(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(2)
    real_path = realpath("pics")
    paths = [f"{real_path}/{pic}" for pic in listdir("pics")]
    for path in paths:
        pics_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#Photos"))
        )
        pics_input.send_keys(path)
        time.sleep(2)
    time.sleep(10)


def enter_price(driver,  price: int):
    content = driver.find_element(By.CSS_SELECTOR, "div.form_box:nth-child(3)")
    price_input = content.find_element(By.CSS_SELECTOR,
                                       "input.form-control:nth-child(1)")
    price_input.send_keys(price)
    time.sleep(2)


def enter_contact(driver, location: str, name: str, phone: str):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
    time.sleep(2)
    location_grp = driver.find_element(
        By.CSS_SELECTOR, "#LocID > div > div > div")
    location_grp.click()
    time.sleep(2)
    location_list = driver.find_elements(
        By.CSS_SELECTOR, "#LocID > div > div > div.sg-selectbox__menu.css-26l3qy-menu > div > div")
    location_btn = next(l for l in location_list if l.text == location)
    location_btn.click()
    time.sleep(2)
    name_input = driver.find_element(By.CSS_SELECTOR, "#User > input")
    name_input.send_keys(name)
    time.sleep(2)
    phone_input = driver.find_element(By.CSS_SELECTOR, "#Phone > input")
    phone_input.send_keys(phone)


def enter_specs(driver, btype: str, size: int):
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight/2+150);")
    time.sleep(2)
    type_grp = driver.find_element(By.CSS_SELECTOR,
                                   "#Attr-1777 > div > div > div")
    type_grp.click()
    time.sleep(2)
    type_lst = driver.find_elements(By.CSS_SELECTOR,
                                    "#Attr-1777 > div > div > div.sg-selectbox__menu.css-26l3qy-menu > div > div")
    b_type = next(t for t in type_lst if t.text == "მთის")
    b_type.click()
    time.sleep(2)
    size_grp = driver.find_element(By.CSS_SELECTOR,
                                   "#Attr-3329 > div > div > div")
    size_grp.click()
    time.sleep(2)
    size_lst = driver.find_element(By.CSS_SELECTOR,
                                   "#Attr-3329 > div > div")
    b_size = size_lst.find_element(
        By.XPATH, f"//*[contains(number(), {size})]")
    b_size.click()


def submit_item(driver):
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    submit_btn = driver.find_element(
        By.XPATH, f"//*[contains(text(), 'გამოქვეყნება')]")
    submit_btn.click()
    print("Finished! Successfully")


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service("./chromedriver"))
    email, passwd, location, name, phone = get_user_data()
    condition, title, description, price, btype, size = get_item_data()
    get_website(driver)
    get_profile(driver, email, passwd)
    get_add_page(driver)
    enter_details(driver, condition, title, description)
    enter_pics(driver)
    enter_price(driver, price)
    enter_contact(driver, location, name, phone)
    enter_specs(driver, btype, size)
    submit_item(driver)
