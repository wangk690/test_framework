'''一些生成器方法，生成随机数，手机号码等'''

import time
from random import randint, choice
from faker import Faker
from data import *

fake = Faker('zh_CN')

def random_phone_num():
    '''随机手机号'''
    return fake.phone_number()

def random_name():
    '''随机姓名'''
    return fake.name()

def random_mac():
    '''随机mac地址'''
    return fake.mac_address()

def random_email():
    '''随机邮件地址'''
    return fake.safe_email()

def random_address():
    """随机地址"""
    return fake.address()

def random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()

def generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids


def choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
    def choice_generator():
        my_list = list(values)
        # rand = random.Random()
        while True:
            yield choice(my_list)
    return choice_generator

def return_nation_data(nation=None):
    '''
    返回民族 键值对，如 HA 汉族
    
    nation参数说明：
        None 打印natiaon_dic键值对
        code 打印code所对应的民族名称
    '''
    if nation == None:
        for nation,code in nation_dic.items():
            print(nation + ':' + code)
    
    if nation in nation_dic.keys():
        print(nation+ ':' + nation_dic[nation])
    else:
        print('%s 不存在' % nation)


def return_nation_by_choice():
    '''随机返回一个民族代码'''
    code_list = []
    for code in nation_dic.keys():
        code_list.append(code)

    nation_code = choice(code_list)
    nation_name = nation_dic[nation_code]
    return nation_code,nation_name

def creat_name():
    '''随机生成姓名'''
    last_name=choice(last_names)
    length=choice(['2','3'])
    if length =='2':
        first_name=choice(first_names)
        name=last_name+first_name
    else:
        first_name_one=choice(first_names)
        first_name_two=choice(first_names)
        name=last_name+first_name_one+first_name_two

    return name

def create_id_card():
    '''
    随机生成身份证信息
    返回值：姓名，身份证号，地址，出生日期，民族代码，民族
    '''    
    #生成身份证号
    year = time.localtime()[0] #当前年份，如2018
    day = time.strftime('%m%d',time.localtime()) #当天,如1201
    choice_num=randint(0, len(area)-1) #随机获取一个正整数，用于获取区域代码和行政区地址
    
    #身份证前17位拼接
    x = (area[choice_num]+'%04d'+day+'%03d') % (randint(year-60, year-18),randint(1,999))

    #前17位对应的系数
    modulus = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
    #最后一位校验码(前17位，每一位上的值乘以系数，累加，对11求余)
    total = 0
    for i in range(17):
        total += int(x[i]) * modulus[i]
    remainder = total % 11
    #根据 求余所得值，决定最后一位校验码
    last = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    card_num = x + last[remainder]

    name = creat_name()
    #获取行政编码对应的行政地区地址
    card_address=address[choice_num]
    #获取生日
    birth_date = card_num[6:10]+'-'+card_num[10:12]+'-'+card_num[12:14]
    #随机获取民族信息
    nation = return_nation_by_choice()
    nation_code = nation[0]
    nation_name = nation[1]

    return name,card_num,card_address,birth_date,nation_code,nation_name

if __name__ == '__main__':
    print(random_phone_num())
    print(random_name())
    print(random_address())
    print(random_email())
    print(random_ipv4())
    print(random_mac())

    id_gen = generate_ids(starting_id=111, increment=1)()
    for i in range(6):
        print(next(id_gen))

    choices = ['John', 'Sam', 'Lily', 'Rose']
    choice_gen = choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))

    print(return_nation_by_choice())
    print(creat_name())
    print(create_id_card())