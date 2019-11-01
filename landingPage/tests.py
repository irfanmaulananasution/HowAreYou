from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from datetime import date
from . import views
from .forms import StatusForms
from .models import StatusModels
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from django.test import TestCase, Client, LiveServerTestCase


class FunctionalTest(LiveServerTestCase):
	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument('--dns-prefetch-disable')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('disable-gpu')
		self.selenium = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
		self.selenium.get(self.live_server_url)
		super(FunctionalTest, self).setUp()
		
	def tearDown(self):
		self.selenium.quit()
		super(FunctionalTest, self).tearDown()
		
	def test_input_todo(self):
		selenium = self.selenium
		#opening the web
		selenium.get(self.live_server_url)
		#find the form element
		status = selenium.find_element_by_id('id_status')#tergangtung kaya diatas
		submit = selenium.find_element_by_id('submit')
		
		#fill the form with data
		status.send_keys('Coba coba')
		
		#submitting the form
		submit.send_keys(Keys.RETURN)
		self.assertIn('Coba coba', selenium.page_source)
		
		
class TestimonyTest(TestCase):
    def setUp(self):
        StatusModels.objects.create(status = "Irfan anak yang sebatang kara, pergi mencari IPK")

    def test_announcement_amount(self):
        status = StatusModels.objects.all()
        self.assertEqual(status.count(), 1)
        
    def test_landing_page_response(self):
        self.response = Client().get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.found = resolve('/')
        self.assertEqual(self.found.url_name, 'landingPage')

    def test_page_header_is_exist(self):
        self.response = Client().get('/')
        self.assertIn('Halo, apa kabar?</h1>', self.response.content.decode())

    def test_form_is_exist(self):
        self.response = Client().get('/')
        self.assertIn('</form>', self.response.content.decode())

    def test_template_is_landingPage(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'landingPage.html')

