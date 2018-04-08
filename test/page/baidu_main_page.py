from selenium.webdriver.common.by import By
from common.page import Page
import sys

class BaiDuMainPage(Page):
	'''百度搜索页面'''
	loc_search_input = (By.ID, 'kw')
	loc_search_btn = (By.ID, 'su')

	def search(self, word):
		self.send_keys(self.loc_search_input, word)
		self.click(self.loc_search_btn)

