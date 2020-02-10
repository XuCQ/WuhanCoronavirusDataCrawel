# 2019-nCoV疫情数据说明

1. **官方新闻数据**

   - 数据来源
     - 丁香医生
     - 页面：https://ncov.dxy.cn/ncovh5/view/pneumonia_timeline?whichFrom=dxy
     - 数据：https://file1.dxycdn.com/2020/0130/492/3393874921745912795-115.json?t=26355088
   - 格式：JSON、CSV
   - 数据名称样例：case_timeline_list 202002101130
   - 代码支撑：../Auxiliary/crawelFunc.py/jsonTOcsv
   - 数据字段说明：
     - code：json调用状态
     - data：数据
       - adoptType
       - createTime：新闻创建时间（时间戳格式）  PS：CSV中已对时间戳进行转换
       - dataInfoOperator
       - dataInfoState：信息状态（时间戳格式）
       - dataInfoTime：数据时间（时间戳格式）
       - entryWay
       - id：编号
       - infoSource：数据来源
       - infoType
       - modifyTime
       - provinceId：省份ID
       - provinceName：省份名称
       - pubDate：公开日期（时间戳格式）
       - pubDateStr：公开日期str格式
       - sourceUrl：信息员链接
       - summary：信息概要
       - title：标题
       - createLocalTime：对createTime时间戳进行转换后str格式创建时间（仅CSV）
       - dataInfocLocalTime：对dataInfoTime时间戳进行转换后str格式数据时间（仅CSV）

2. **人口迁徙数据**

   - 数据来源

     - 百度迁徙

     - 页面：https://qianxi.baidu.com/

     - 数据

       - ```python
         URL_MIGRATION = {
             # migration_city_prec_movein date范围：[20200101-currDate-1]
             'migration_city_prec_movein': 'https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id={cityID}&type=move_in&date={date}&callback=jsonp_{random_num_0}_{random_num_1}',
             'migration_city_prec_moveout': 'https://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id={cityID}&type=move_out&date={date}&callback=jsonp_{random_num_0}_{random_num_1}',
             'migration_index_movein': 'https://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={cityID}&type=move_in&startDate=20190112&endDate={endDate}&callback=jsonp_{random_num_0}_{random_num_1}',
             'migration_index_moveout': 'https://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id={cityID}&type=move_out&startDate=20190112&endDate={endDate}&callback=jsonp_{random_num_0}_{random_num_1}',
         
         }
         ```

   - 格式：JSON

   - 数据名称样例

     - migration_city_prec_movein_202002100307.json
     - migration_index_movein_202002100217.json
     - migration_index_moveout_202002100201.json

   - 代码支撑：../MigrationDataCrawel.py

   - 数据字段说明

     - migration_city_prec_movein_{date}.json	某市迁入来源地

       - infoName：信息名称

       - num：信息数量

       - data：数据

         - province：被迁入城市对应省份
         - city：被迁入城市名称
         - startDate：数据采集起始时间
         - endDate：数据采集终止时间
         - data：数据
           - 20200101：当日某市迁入来源地数据（共50城市）
             - city_name：迁入来源地
             - province_name：迁入来源省
             - value：占比
           - ...

       - migration_city_prec_moveout_{date}.json	某市迁出来源地  【同迁入地】

       - migration_index_movein_{date}.json 某市迁入指数（包括去年对应农历日期数据）

         - infoName：信息名称

         - num：信息数量

         - data：数据

           - province：城市对应省份

           - city：城市
           - data：数据
             - list：数据
               - 20190112：该日迁入指数
               - ...

         - migration_index_moveout_{date}.json 某市迁出指数（包括去年对应农历日期数据）

3.  **每日新增病例数据（北京大学）**

   - 数据来源：
     - 北京大学 新型冠状病毒肺炎疫情 可视分析系列
     - 页面：http://vis.pku.edu.cn/ncov/home.html
     - 数据：https://tanshaocong.github.io/2019-nCoV/map.csv
   - 格式：CSV
   - 代码支撑：无
   - 数据名称样例：每日新增病例数据（北京大学）202002101130.csv
   - 字段说明
     - 公开时间
     - 类别
     - 省份
     - 城市
     - 新增确诊病例
     - 新增治愈出院数
     - 新增死亡数
     - 核减

4. **确诊人员位置数据**

   - 数据来源
     - 第一财经商业数据中心
     - 页面：https://z.cbndata.com/2019-nCoV/index.html?from=singlemessage&isappinstalled=0&t=1581304752232
     - 数据：https://assets.cbndata.org/2019-nCoV/data.json?t=1581303777663

   - 格式：json
   - 代码支撑：无
   - 数据名称样例：确诊人员位置数据_202002101100.json
   - 字段说明
     - data：数据
       - province：省
       - city：市
       - district：区
       - address：详细地址
       - longitude：经度
       - latitude：维度
       - count：确诊数量

5. **每日新增病例数据（哈工大）**

   - 数据来源
     - 哈工大
     - 页面：http://101.200.120.155:8765/info
     - 数据：http://101.200.120.155:8765/2019-nCoV-data
   - 格式：json
   - 代码支撑：无
   - 数据名称样例：每日新增病例数据（哈工大）202002101250.json
   - 字段说明
     - 省/直辖市
     - 市/区
     - 新增死亡
     - 新增治愈
     - 新增疑似
     - 新增确诊
     - 时间：（20200124-currDate）
     - 死亡
     - 治愈
     - 疑似
     - 疑似增幅
     - 确诊
     - 确诊增幅

