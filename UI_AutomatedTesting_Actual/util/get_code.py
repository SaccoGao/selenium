import pytesseract
from UI_AutomatedTesting_Actual.util import code_demo_API
from PIL import Image
from UI_AutomatedTesting_Actual.page.resgister_page import ResgisterPage

class GetCode():
    def __init__(self, driver):
        self.driver = driver
        self.resgister_p = ResgisterPage(driver)

    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.resgister_p.get_code_text_image()
        left = code_element.location['x'] * 1.25
        top = code_element.location['y'] * 1.25
        right = code_element.size['width'] * 1.25 + left
        height = code_element.size['height'] * 1.25 + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    def code_online(self, file_name):
        self.get_code_image(file_name)
        return code_demo_API.code_demo(file_name)

