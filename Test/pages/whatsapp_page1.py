from pages.base_page import BasePage
from data.locators import WhatsappPageLocator
from data.data import *
from time import sleep
from utils.excel_utils_pandas import *
from utils.gspread_utils import *
from utils.readUserData import *


class WhatsAppPage(BasePage):

    def __init__(self, driver):
        self.locator = WhatsappPageLocator
        self.data = Data
        self.wdata = Whatsapp
        super().__init__(driver)

    def send_different_person_different_message(self):
        available_phone_number, message = read_person_message(self.wdata.file_for_availability, self.wdata.sheet_for_availability)
        print(available_phone_number)
        print(message)

        for i in range(0, len(available_phone_number)):
            self.click(self.locator.search)
            sleep(self.data.one_second)
            self.send_data(f'{self.wdata.country_code_BD}{int(available_phone_number[i])}', self.locator.search_input)
            self.driver.hide_keyboard()
            try:
                self.click(self.locator.chat_person)
                self.send_data(message[i], self.locator.chat_message)
                sleep(self.data.point_five)
                self.click(self.locator.post_message)
                self.go_back()
                sleep(self.data.point_five)
            except Exception as e:
                print(e)
