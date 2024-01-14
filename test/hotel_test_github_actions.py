import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestHotelCICD:

    def setup_method(self):

        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        url = 'http://hotel-v3.progmasters.hu/'

        self.browser.get(url)
        self.browser.maximize_window()

        hotel_list_btn = self.browser.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list_btn.click()
        time.sleep(1)

    def teardown_method(self):
        self.browser.quit()

    def test_hotel_list(self):
        # 1) Navigáljunk el a hotelek listájához.

        hotel_list = self.browser.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotel_list) != 0
        assert len(hotel_list) == 10

    def test_checkboxes(self):
        # 2) Ellenőrizzük le a checkboxok működését: mindet kattintsuk be, majd a "Szoba szolgáltatás szűrések törlése" gombra kattintva távolítsuk el a kiválaszott szolgáltatásokat, és ellenőrizzük is le, hogy megtörtént.

        checkbox_list = self.browser.find_elements(By.XPATH, '//input[@type="checkbox"]')
        for checkbox in checkbox_list:
            checkbox.click()
        assert checkbox.is_selected()

        erase_selection_btn = self.browser.find_element(By.ID, 'redstar')
        erase_selection_btn.click()

        for checkbox in checkbox_list:
            check_class = checkbox.get_attribute('class')
            if 'ng-pristine' in check_class:
                print('A checkbox nincs kijelölve.')

    def test_random_hotel_page(self):
        # 3) Navigáljunk el egy tetszőleges hotel oldalára.
        first_hotel = self.browser.find_element(By.XPATH, '//h4[@style="cursor: pointer"]')
        first_hotel.click()
        time.sleep(1)

        # 4) Írjuk ki a terminálra a hosszú leírását.
        hotel_description = self.browser.find_elements(By.XPATH, '//p[@class="card-text"]')[1]
        print(hotel_description.text)

        assert 500 <= len(hotel_description.text) <= 2000