import unittest
import sys
sys.path.append('E:\\Test_framework')
from tools.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from tools.log import logger
from tools.client import HTTPClient
from tools.assertion import assertHTTPCode

class TestBaidu(unittest.TestCase):
	url = Config().get('url')

	def setUp(self):
		self.client = HTTPClient(url=self.url, method='GET')

	def test_baidu_http(self):
		res = self.client.send()
		# logger.debug(res.text)
		# self.assertIn('百度一下', res.text)
		assertHTTPCode(res,[200])

if __name__ == '__main__':
	unittest.main()