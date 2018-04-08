参考 https://blog.csdn.net/huilan_same?t=1 

config
  --config.yml:配置文件；使用tools/config.py进行读取

data
  --test_data.xlsx：测试数据

drivers:驱动文件夹
  --chormedriver.exe 

log:日志文件夹

test
  --case:用例文件
  --common:跟项目、页面无关的封装
  --page:页面
  --suite:测试套件，用来组织用例

interface:接口用例文件夹

report:测试报告存放目录

tools:工具类
  --assertion.py:断言
  --client:接口测试类封装
  --config.py:配置文件读取
  --data.py:数据文件，存放 行政编码、地区、民族、常用姓名
  --file_reager.py:文件读取
  --generator.py:测试数据生成
  --HTMLTestRunner.py:测试报告
  --log.py:日志打印
  --mail.py:邮件类封装