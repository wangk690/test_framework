import os,sys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tools.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from tools.log import logger
from tools.file_reader import ExcelReader
# from tools.HTMLTestRunner import HTMLTestRunner
from tools.HTMLTestRunner import HTMLTestRunner
from tools.mail import Email
from common.browser import browser
from page.baidu_result_page import BaiDuResultPage, BaiDuMainPage

class TestBaiDu(unittest.TestCase):

	url = Config().get('url')
	excel = DATA_PATH + '/test_data.xlsx'
	# base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
	# driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
	# print(driver_path)

	# locator_kw = (By.ID,'kw')
	# locator_su = (By.ID,'su')
	# locator_result = (By.XPATH,'//div[contains(@class,"result")]/h3/a')

	# log = Log()

	# def sub_setUp(self):
	# 	self.dr = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
	# 	self.dr.get(self.url)

	# def sub_tearDown(self):
	# 	self.dr.quit()

	# def test_search(self):
	# 	datas = ExcelReader(self.excel).data
	# 	for d in datas:
	# 		with self.subTest(data=d):
	# 			self.sub_setUp()
	# 			self.dr.find_element(*self.locator_kw).send_keys(d['search'])
	# 			self.dr.find_element(*self.locator_su).click()
	# 			time.sleep(2)
	# 			links = self.dr.find_elements(*self.locator_result)
	# 			for link in links:
	# 				self.log.info(link.text)

	# 			self.sub_tearDown()


	def setUp(self):
		self.dr = browser(browser_type='firefox')
		# self.dr = webdriver.Chrome(executable_path=DRIVER_PATH+'\chromedriver.exe')
		# self.page.get(self.url)

	def tearDown(self):
		self.dr.quit()

	def test_search_0(self):
		# self.dr.find_element(*self.locator_kw).send_keys('selenium')
		# self.dr.find_element(*self.locator_su).click()
		# time.sleep(2)

		# links = self.dr.find_elements(*self.locator_result)
		# for link in links:
		# 	self.log.info(link.text)
		baidu = BaiDuMainPage(self.dr)
		baidu.open(self.url)
		logger.info('open url')

		baidu.search('selenium')
		baidu.save_screen_shot(REPORT_PATH)

		logger.info('search selenium')
		# links = self.page.result_links
		# for link in links:
		# 	self.log.info(link.text)

	# def test_search_1(self):
	# 	self.dr.find_element(*self.locator_kw).send_keys('Python selenium')
	# 	self.dr.find_element(*self.locator_su).click()
	# 	time.sleep(2)

	# 	links = self.dr.find_elements(*self.locator_result)
	# 	for link in links:
	# 		self.log.info(link.text)


if __name__ == '__main__':

	unittest.main()

	# testunit = unittest.TestSuite()
	# testunit.addTest(TestBaiDu('test_search_0'))
	# # testunit.addTest(TestBaiDu('test_search_1'))

	# now = time.strftime("%Y-%m-%d %H_%M_%S")

	# #报告存放目录
	# report = REPORT_PATH + '\\'+ now +'_report.html'

	# with open(report, 'wb') as f:
	# 	runner = HTMLTestRunner(stream=f, verbosity=2, title='搭建测试框架', description='修改html报告')
	# 	# runner.run(TestBaiDu('test_search'))
	# 	runner.run(testunit)

	# e = Email('smtp.sina.com', 'username@xx.com', 'password', 'receiver@xx.com', 'test', path=report)
	# e.send()