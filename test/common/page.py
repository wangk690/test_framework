#coding:utf-8
import time,os
from time import sleep

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Page(object):
    '''
    页面基础类，用于所有页面的继承。基于原生的selenium进行二次封装。
    '''
    def __init__(self, driver, timeout=20):
        '''
        启动浏览器参数化，默认启动chrome
        '''
        self.driver = driver
        self.timeout = timeout

    def save_screen_shot(self,screen_path, name='screen_shot'):
        '''
        截图并保存
        Usage：
        driver.save_screen_shot(REPORT_PATH)
        '''
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = screen_path + '\screenshot_%s' %day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' %(name, tm))
        return screenshot

    def back(self):
        '''浏览器后退操作'''
        self.driver.back()

    def forward(self):
        '''浏览器前进操作'''
        self.driver.forward()

    def close(self):
        '''关闭当前窗口'''
        self.driver.close()

    def quit(self):
        '''关闭浏览器'''
        self.driver.quit()   

    def wait(self, w_time=10):
        '''等待特定的时间'''
        sleep(w_time)

    def open(self,url,t=''):
        '''
        使用get打开url后，最大化窗口，判断title符合预期
        Usage:
        driver = Page()
        driver.open(url, t='')
        '''
        self.driver.get(url)
        self.driver.maximize_window()

        try:
            WebDriverWait(self.driver, self.timeout,1).until(EC.title_contains(t))
        except TimeoutError:
            print("open %s title error." %url)
        except Exception as msg:
            print("Error: %s" %msg)

    def find_element(self,locator):
        '''
        定位元素，参数locator是元组类型
        Usage:
        locator = ('id', 'xxx')
        driver.find_element(locator)
        '''
        element = WebDriverWait(self.driver, self.timeout, 1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator):
        '''定位一组元素'''
        element = WebDriverWait(self.driver, self.timeout, 1).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self, locator):
        '''
        点击操作
        Usage:
        locator = ('id','xxx')
        driver.click(locator)
        '''
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        '''
        发送文本，清空后输入
        Usage:
        locator = ('id','xxx')
        driver.send_keys(locator, text)
        '''
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text):
        '''
        判断文本在元素里，没定位到元素返回False,定位到返回判断结果布尔值

        result = driver.is_text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self, self.timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutError:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_text_in_value(self, locator, value):
        '''
        判断文本的value值，没定位到元素返回False,定位到返回判断结果布尔值

        result = driver.is_text_in_value(locator, text)
        '''
        try:
            result = WebDriverWait(self, self.timeout, 1).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutError:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_title(self, title):
        '''
        判断title完全等于
        '''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title):
        '''
        判断title包含
        '''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, locator):
        '''判断元素被选中，返回布尔值'''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True):
        '''判断元素的状态，selected是期望的参数true/false'''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.element_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self):
        '''
        判断页面是否有alert，有返回alert，没有返回false
        '''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator):
        '''元素可见返回本身，不可见返回False'''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator):
        '''元素可见返回本身，不可见返回True，没有找到也返回True'''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickalbe(self, locator):
        '''元素可点击返回本身，不可点击返回false'''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator):
        '''判断元素没有被定位到(并不意味可见)，定位到返回element，没定位到返回false'''
        result = WebDriverWait(self.driver, self.timeout, 1).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        Usage:
        locator = ('id','xxx')
        driver.move_to_element(locator)
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self,locator):
        '''获取定位元素文本'''
        element = self.find_element(locator)
        return element.text

    def get_attribute(self,locator, name):
        '''获取元素的属性值'''
        element = self.find_element(locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_foucs_element(self, locator):
        '''js聚焦元素'''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index):
        '''通过索引index选择'''
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_text(self, locator, text):
        '''通过文本定位'''
        element = self.find_element(locator)
        Select(element).select_by_text(text)   

    def select_by_value(self, locator, value):
        '''
        通过value定位
        '''
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def get_url(self):
        '''获取当前网页的url'''
        return self.driver.current_url

    def get_page_source(self):
        '''获取当前页面的源码'''
        return self.driver.page_source

    def get_driver_name(self):
        '''获取执行浏览器名称'''
        return self.driver.name

    def switch_to_iframe(self, locator):
        '''切换到frame/iframe中'''
        self.driver.switch_to.frame(locator)

    def click_node_by_name(self,name):
        '''点击特定的node,专用于选择机构'''
        self.click_element(*(By.XPATH,'//span[text()="'+name+'"]'))

if __name__ == '__main__':
    # driver = browser()
    driver_n = Page(browser_type='chrome')
    driver_n.open('https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F')