from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import HttpTrigger1.config as config


def init_scrapper(driver_path, window_height=900, window_width=900, window_pos_x=0, window_pos_y=0):
    browser = webdriver.Chrome(
        executable_path=driver_path)

    browser.set_window_size(window_width, window_height)
    browser.set_window_position(window_pos_x, window_pos_y)

    sleep(1)
    wait = WebDriverWait(browser, 10)
    return browser, wait


def login_certain(browser, wait, username, password):
    browser.get(config.CERTAIN_URL)

    wait.until(EC.presence_of_element_located((By.ID, "username")))

    user_name_text_box = browser.find_element_by_id("username")

    user_name_text_box.send_keys(username)

    password_textbox = browser.find_element_by_id("password")

    password_textbox.send_keys(password)

    sleep(2)

    continue_button = browser.find_elements_by_css_selector(
        'input[value="Continue"]')

    continue_button[0].click()


def login_AIAD_report(browser, wait, unique_report_id):
    wait.until(EC.presence_of_element_located((By.ID, "pro_addr_line1")))

    unique_report_id_field = browser.find_element_by_id("pro_addr_line1")

    unique_report_id_field.send_keys(unique_report_id)

    sleep(2)

    get_report_button = browser.find_elements_by_css_selector(
        'input[value="Get report"]')

    get_report_button[0].click()


def switch_to_report_window(browser, wait):
    sleep(8)

    another_window = list(set(browser.window_handles) -
                          {browser.current_window_handle})[0]
    browser.switch_to.window(another_window)


def get_report_iframe(browser, wait):
    wait.until(EC.presence_of_element_located(
        (By.ID, "iFrameReportListDisplay")))

    browser.switch_to.frame("iFrameReportListDisplay")


def move_to_certain_report(browser, wait, username, password, unique_report_id):
    login_certain(browser, wait, username, password)
    login_AIAD_report(browser, wait, unique_report_id)
    switch_to_report_window(browser, wait)
    get_report_iframe(browser, wait)


def fetch_report_header_main_result(browser, wait):
    sleep(5)
    wait.until(EC.presence_of_element_located((By.ID, "reportResults")))

    table_report_result = browser.find_elements_by_css_selector(
        "#reportResults")

    headers = table_report_result[0].find_elements_by_css_selector('thead tr')

    main_result = table_report_result[0].find_elements_by_css_selector('tbody')

    html_header = headers[0].get_attribute('innerHTML')
    html_table = main_result[0].get_attribute('innerHTML')

    return html_header, html_table


def get_header_list(html_header):
    soup_header = BeautifulSoup(html_header, 'html.parser')

    table_data_header = soup_header.find_all(
        "div", {'class': 'tablesorter-header-inner'})

    header = []

    for header_data in table_data_header:
        try:
            t = header_data.text.strip()
            header.append(t)
        except:
            continue

    return header


def get_table_data(html_table, header):
    soup = BeautifulSoup(html_table, 'html.parser')

    table_data_rows = soup.find_all("tr")

    data = []

    for row in table_data_rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append({header[count]: ele for count,
                     ele in enumerate(cols) if ele})

    return data


def run_scrapper(username, password, uniqure_report_id):

    driver_path = config.DRIVER_PATH
    browser, wait = init_scrapper(driver_path)

    move_to_certain_report(browser, wait, username,
                           password, uniqure_report_id)

    html_header, html_main_table = fetch_report_header_main_result(
        browser, wait)

    headers = get_header_list(html_header)
    data = get_table_data(html_main_table, headers)

    return data
