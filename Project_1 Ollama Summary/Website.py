from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class Website:
    def __init__(self, url):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless if needed
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.url = url
        self.driver.get(url)

        # Get title
        try:
            self.title = self.driver.title if self.driver.title else "No title found"
        except Exception as e:
            self.title = "Error retrieving title"

        # Remove irrelevant elements (script, style, img, input)
        self._remove_irrelevant_elements()

        # Get visible text
        self.text = self._get_visible_text()

    def _remove_irrelevant_elements(self):
        irrelevant_tags = ["script", "style", "img", "input"]
        for tag in irrelevant_tags:
            elements = self.driver.find_elements(By.TAG_NAME, tag)
            for element in elements:
                self.driver.execute_script("arguments[0].remove();", element)

    def _get_visible_text(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        return body.text.replace("\n", "\n").strip()

    def close(self):
        self.driver.quit()