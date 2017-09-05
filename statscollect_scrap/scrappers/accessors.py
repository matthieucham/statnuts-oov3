from faker import Faker
import random
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from statscollect import settings
from .myphantomjs import MyPhantomWebDriver
import os


class BaseContentAccessor():
    def get_content(self, form):
        raise NotImplementedError('get_content must be implemented by subclasses')


class CopyPasteAccessor(BaseContentAccessor):
    def get_content(self, form):
        return form.cleaned_data.get('page_content')


class URLAccessor(BaseContentAccessor):
    def __init__(self, ctrl_pattern, url_pattern):
        self.ctrl_pattern = ctrl_pattern
        self.url_pattern = url_pattern

    def get_content(self, form):
        if form.cleaned_data.get('scraped_url'):
            url_to_scrap = form.cleaned_data.get('scraped_url')
        else:
            url_to_scrap = self.url_pattern % form.cleaned_data.get('identifier')
        # m = re.match(self.ctrl_pattern, url_to_scrap)
        # if not m:
        # raise ValueError('Input url %s does not match the expected url pattern of this scrapper. Scrapper\'s url '
        # 'pattern is %s' % (url_to_scrap, self.ctrl_pattern))
        fake = Faker()
        headers = {
            'User-Agent': random.choice(
                [fake.firefox()])
        }
        page = requests.get(url_to_scrap, headers=headers)
        return page.text


class BrowserWSAccessor(BaseContentAccessor):
    def __init__(self, url_pattern):
        self.entry_point = 'https://www.whoscored.com/Regions/74/Tournaments/22/France-Ligue-1'
        self.url_pattern = url_pattern

    def get_content(self, form):
        if form.cleaned_data.get('scraped_url'):
            url_to_scrap = form.cleaned_data.get('scraped_url')
        else:
            url_to_scrap = self.url_pattern % form.cleaned_data.get('identifier')
        fake = Faker()
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (fake.chrome())
        if settings.ON_OPENSHIFT:
            print('Using phantomJS binary at %s', settings.PHANTOMJS_BIN_PATH)
            # browser = webdriver.PhantomJS(desired_capabilities=dcap, executable_path=settings.PHANTOMJS_BIN_PATH)
            browser = MyPhantomWebDriver(desired_capabilities=dcap, executable_path=settings.PHANTOMJS_BIN_PATH,
                                         service_log_path=settings.PHANTOMJS_LOG_PATH,
                                         ip=os.getenv('OPENSHIFT_PYTHON_IP'), port=15002)
        else:
            print('Using phantomJS binary in PATH')
            browser = MyPhantomWebDriver(desired_capabilities=dcap, ip='127.0.0.1', port=15002)
		
        print('web driver init ok')
        browser.implicitly_wait(3)

        browser.get(self.entry_point)
        my_url_in_page = False
        max_depth = 3
        depth_count = 1
        random.seed()
        while (not my_url_in_page) and (depth_count < max_depth):
            # recherche de l'url visée dans le contenu de la page visible
            match_links = browser.find_element_by_id('tournament-fixture-wrapper').find_elements_by_class_name(
                'result-1')
            # browser.save_screenshot(os.path.join(settings.PHANTOMJS_LOG_PATH,'1.png'))
            for ml in match_links:
                href = ml.get_attribute('href')
                print(href)
                if href == url_to_scrap:
                    # found my game : select !
                    time.sleep(random.random())
                    ml.click()
                    my_url_in_page = True
                    break
            if not my_url_in_page:
                previous = browser.find_element_by_id('date-controller').find_element_by_class_name('previous')
                time.sleep(random.random())
                depth_count += 1
                previous.click()
        # browser.save_screenshot(os.path.join(settings.PHANTOMJS_LOG_PATH,'2.png'))
        if my_url_in_page:
            # access content here
            html_source = browser.page_source
            return html_source