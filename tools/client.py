'''
添加用于接口测试的client，对于HTTP接口添加HTTPClient，发送http请求。
'''
import requests
import sys
sys.path.append('E:\\Test_framework')
from tools.log import logger

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']

class UnSupportMethodException(Exception):
    """当传入的method的参数不是支持的类型时抛出此异常。"""
    pass

class HTTPClient(object):
	'''
	http请求的client。初始化时传入url、method等，可以添加header和cookies。
	'''
	def __init__(self, url, method='GET', headers=None, cookies=None):
		self.url = url
		self.session = requests.session()
		self.method = method
		if self.method not in METHODS:
			raise UnSupportMethodException('不支持的method:{0}，请检查传入参数！'.format(self.method))

		self.set_headers(headers)
		self.set_cookies(cookies)

	def set_headers(self, headers):
		if headers:
			self.session.headers.update(headers)

	def set_cookies(self, cookies):
		if cookies:
			self.session.cookies.update(cookies)

	def send(self, params=None, data=None, **kwargs):
		response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
		response.encoding = 'utf-8'
		logger.debug('{0} {1}'.format(self.method, self.url))
		logger.debug('请求成功：{0}\n{1}'.format(response, response.text))
		return response