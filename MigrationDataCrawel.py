# -*- coding:utf-8 -*-
# author:Changing Xu
# file:WuhanCoronavirusDataCrawel-MigrationDataCrawel
# datetime:2020/2/9 22:41
# software: PyCharm
# describe:中国人口迁徙数据爬取，数据来源：百度迁徙数据
from Auxiliary.crawelFunc import loadCSV, getRandomNum, createAssistDate
import random
import time
import datetime
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json
import os

random_num_0_length = 13
random_num_1_length = 7
PreDate = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime('%Y%m%d')
URL_MIGRATION = {
    # date范围：[20200101-currDate-1]
    'migration_city_prec_movein': 'https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id={cityID}&type=move_in&date={date}&callback=jsonp_{random_num_0}_{random_num_1}',
    'migration_city_prec_moveout': 'https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id={cityID}&type=move_out&date={date}&callback=jsonp_{random_num_0}_{random_num_1}',
    'migration_index_movein': 'https://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={cityID}&type=move_in&startDate=20190112&endDate={endDate}&callback=jsonp_{random_num_0}_{random_num_1}',
    'migration_index_moveout': 'https://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={cityID}&type=move_out&startDate=20190112&endDate={endDate}&callback=jsonp_{random_num_0}_{random_num_1}',

}


def saveJson(path, data):
    try:
        file = open(path, 'w', encoding='utf-8')
        json.dump(data, file, ensure_ascii=False)
        file.close()
        print(f"SAVE SUCCESS; PATH:{path}")
    except Exception as e:
        print(data)
        print(e)


def getMigrationIndex(cityInfos, task, savePath):
    DATA = []
    URL = URL_MIGRATION[task]
    session = requests.Session()
    ua = UserAgent()
    savePath = os.path.join(savePath, f"{task}_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.json")
    for index, cityInfo in cityInfos.iterrows():
        target_headers = {'User-Agent': ua.random}
        para = {'headers': target_headers, 'timeout': 20}
        provinceName, cityID, cityName = cityInfo[0], cityInfo[1], cityInfo[2]
        random_num_0 = getRandomNum(random_num_0_length)
        random_num_1 = getRandomNum(random_num_1_length)
        url = URL.format(cityID=cityID, endDate=PreDate, random_num_0=random_num_0, random_num_1=random_num_1)
        try:
            response = session.get(url, **para)
            info = {}
            info['province'] = provinceName
            info['city'] = cityName
            info.update(json.loads(response.text[28:-1]))
            if info['errmsg'] == 'SUCCESS':
                del info['errno']
                del info['errmsg']
                DATA.append(info)
                print(f"{provinceName}-{cityName} Done")
        except Exception as e:
            print(f'{provinceName}-{cityName} failure；URL：{url};ERROR:{e}')
        time.sleep(int(random_num_0[-1]) / 5.0)
    saveJson(savePath, {'infoName': task, 'num': DATA.__len__(), 'data': DATA})


def getMigrationCityPrec(cityInfos, task, savePath):
    DATA = []
    URL = URL_MIGRATION[task]
    session = requests.Session()
    ua = UserAgent()
    savePath = os.path.join(savePath, f"{task}_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.json")
    for index, cityInfo in cityInfos.iterrows():
        provinceName, cityID, cityName = cityInfo[0], cityInfo[1], cityInfo[2]
        cityDict = {}
        cityDict['province'] = provinceName
        cityDict['city'] = cityName
        cityDict['startDate'] = '20200101'
        cityDict['endDate'] = PreDate
        cityDict['date'] = {}
        for date in createAssistDate('20200101', PreDate):
            target_headers = {'User-Agent': ua.random}
            para = {'headers': target_headers, 'timeout': 30}
            random_num_0 = getRandomNum(random_num_0_length)
            random_num_1 = getRandomNum(random_num_1_length)
            url = URL.format(cityID=cityID, date=date, random_num_0=random_num_0, random_num_1=random_num_1)
            try:
                response = session.get(url, **para)
                info = json.loads(response.text[28:-1])
                if info['errmsg'] == 'SUCCESS':
                    cityDict['date'][date] = info['data']['list']
                else:
                    cityDict['date'][date] = ''
            except Exception as e:
                print(f'{provinceName}-{cityName} failure；URL：{url};ERROR:{e}')
            time.sleep(int(random_num_0[-1]) / 10.0)
        DATA.append(cityDict)
        print(f"{provinceName}-{cityName} Done")
    saveJson(savePath, {'infoName': task, 'num': DATA.__len__(), 'data': DATA})


if __name__ == '__main__':
    cityInfos = loadCSV('data/csv/cityID_china.csv')
    # getMigrationIndex(cityInfos, 'migration_index_movein', 'data/json')
    # getMigrationCityPrec(cityInfos, 'migration_city_prec_movein', 'data/json')
    getMigrationCityPrec(cityInfos, 'migration_city_prec_moveout', 'data/json')

