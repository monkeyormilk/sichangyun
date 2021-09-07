from flask import Flask,render_template
import sqlite3
import datetime
import re


app = Flask(__name__)


@app.route('/')
def index():
    datalist = []
    lastdatalist = []
    conn = sqlite3.connect('sichangyun.db')
    cur = conn.cursor()
    dayt = datetime.datetime.now()
    today = dayt.day
    month = dayt.month
    year =dayt.year

    # 判断表是否存在
    table_check = "SELECT name FROM sqlite_master WHERE type='table';"
    cur.execute(table_check)
    # 返回所有表名[[('cq_2021_1',), ('cq_2021_2',), ('cq_2021_3',), ('cq_2021_4',), ('cq_2021_5',), ('cq_2021_6',), ('cq_2021_7',), ('cq_2021_8',)]]
    tables = [cur.fetchall()]
    # 返回所有的表名["'cq_2021_1'", "'cq_2021_2'", "'cq_2021_3'", "'cq_2021_4'", "'cq_2021_5'", "'cq_2021_6'", "'cq_2021_7'", "'cq_2021_8'"]
    table_list = re.findall('(\'.*?\')', str(tables))
    # 去掉双引号
    table_list = [re.sub("'", '', each) for each in table_list]

    sql = ''
    if month == 1 and today == 1:
        year -= 1
        month = 12
    for m in range(month):
        if ('cq_' + str(year) + '_' + str(12 - m)) in table_list:
            sql = '''select * from {}'''.format('cq_' + str(year) + '_' + str(12 - m))
            lastsql = '''select * from {}'''.format('cq_' + str(year) + '_' + str(12 - m - 1))
            month = 12 - m
            break
    data = cur.execute(sql)
    for num in data:
        datalist.append(num)
    lastdata = cur.execute(lastsql)
    for lastnum in lastdata:
        lastdatalist.append(lastnum)

    # 确定最近更新的数据的日期,及存放本月及上月销量总和
    totalsal = 0
    lasttotalsal = 0
    totalfaqi = 0
    day_suo = 0
    for d in range(31):
        if datalist[d][1] == 0 and d > 0 and day_suo == 0:
            today = d
            day_suo += 1
    for d in range(today):
        totalsal += datalist[d][1]
        lasttotalsal += lastdatalist[d][1]
        totalfaqi += datalist[d][9]
    cur.close()
    conn.close()
    return render_template('index.html',month = month, today = today, datalist = datalist, totalsal = totalsal, lasttotalsal = lasttotalsal,lastdatalist = lastdatalist,totalfaqi=totalfaqi)


@app.route('/hebei')
def hebei():
    datalist = []
    lastdatalist = []
    conn = sqlite3.connect('sichangyun.db')
    cur = conn.cursor()
    dayt = datetime.datetime.now()
    today = dayt.day
    month = dayt.month
    year =dayt.year

    # 判断表是否存在
    table_check = "SELECT name FROM sqlite_master WHERE type='table';"
    cur.execute(table_check)
    # 返回所有表名[[('cq_2021_1',), ('cq_2021_2',), ('cq_2021_3',), ('cq_2021_4',), ('cq_2021_5',), ('cq_2021_6',), ('cq_2021_7',), ('cq_2021_8',)]]
    tables = [cur.fetchall()]
    # 返回所有的表名["'cq_2021_1'", "'cq_2021_2'", "'cq_2021_3'", "'cq_2021_4'", "'cq_2021_5'", "'cq_2021_6'", "'cq_2021_7'", "'cq_2021_8'"]
    table_list = re.findall('(\'.*?\')', str(tables))
    # 去掉双引号
    table_list = [re.sub("'", '', each) for each in table_list]

    sql = ''
    if month == 1 and today == 1:
        year -= 1
        month = 12
    for m in range(month):
        if ('hb_' + str(year) + '_' + str(12 - m)) in table_list:
            sql = '''select * from {}'''.format('hb_' + str(year) + '_' + str(12 - m))
            lastsql = '''select * from {}'''.format('hb_' + str(year) + '_' + str(12 - m - 1))
            month = 12 - m
            break
    data = cur.execute(sql)
    for num in data:
        datalist.append(num)
    lastdata = cur.execute(lastsql)
    for lastnum in lastdata:
        lastdatalist.append(lastnum)

    # 确定最近更新的数据的日期,及存放本月及上月销量总和
    totalsal = 0
    lasttotalsal = 0
    totalfaqi = 0
    day_suo = 0
    for d in range(31):
        if datalist[d][1] == 0 and d > 0 and day_suo == 0:
            today = d
            day_suo += 1
    for d in range(today):
        totalsal += datalist[d][1]
        lasttotalsal += lastdatalist[d][1]
        totalfaqi += datalist[d][12]
    cur.close()
    conn.close()
    return render_template('hebei.html',month = month, today = today, datalist = datalist, totalsal = totalsal, lasttotalsal = lasttotalsal,lastdatalist = lastdatalist,totalfaqi=totalfaqi)


@app.route('/shanxi')
def shanxi():
    datalist = []
    lastdatalist = []
    conn = sqlite3.connect('sichangyun.db')
    cur = conn.cursor()
    dayt = datetime.datetime.now()
    today = dayt.day
    month = dayt.month
    year =dayt.year

    # 判断表是否存在
    table_check = "SELECT name FROM sqlite_master WHERE type='table';"
    cur.execute(table_check)
    # 返回所有表名[[('cq_2021_1',), ('cq_2021_2',), ('cq_2021_3',), ('cq_2021_4',), ('cq_2021_5',), ('cq_2021_6',), ('cq_2021_7',), ('cq_2021_8',)]]
    tables = [cur.fetchall()]
    # 返回所有的表名["'cq_2021_1'", "'cq_2021_2'", "'cq_2021_3'", "'cq_2021_4'", "'cq_2021_5'", "'cq_2021_6'", "'cq_2021_7'", "'cq_2021_8'"]
    table_list = re.findall('(\'.*?\')', str(tables))
    # 去掉双引号
    table_list = [re.sub("'", '', each) for each in table_list]

    sql = ''
    if month == 1 and today == 1:
        year -= 1
        month = 12
    for m in range(month):
        if ('sx_' + str(year) + '_' + str(12 - m)) in table_list:
            sql = '''select * from {}'''.format('sx_' + str(year) + '_' + str(12 - m))
            lastsql = '''select * from {}'''.format('sx_' + str(year) + '_' + str(12 - m - 1))
            month = 12 - m
            break
    data = cur.execute(sql)
    for num in data:
        datalist.append(num)
    lastdata = cur.execute(lastsql)
    for lastnum in lastdata:
        lastdatalist.append(lastnum)

    # 确定最近更新的数据的日期,及存放本月及上月销量总和
    totalsal = 0
    lasttotalsal = 0
    totalfaqi = 0
    day_suo = 0
    for d in range(31):
        if datalist[d][1] == 0 and d > 0 and day_suo == 0:
            today = d
            day_suo += 1
    for d in range(today):
        totalsal += datalist[d][1]
        lasttotalsal += lastdatalist[d][1]
        totalfaqi += datalist[d][8]
    cur.close()
    conn.close()
    return render_template('shanxi.html',month = month, today = today, datalist = datalist, totalsal = totalsal, lasttotalsal = lasttotalsal,lastdatalist = lastdatalist,totalfaqi=totalfaqi)


@app.route('/heilongjiang')
def heilongjiang():
    datalist = []
    lastdatalist = []
    conn = sqlite3.connect('sichangyun.db')
    cur = conn.cursor()
    dayt = datetime.datetime.now()
    today = dayt.day
    month = dayt.month
    year =dayt.year

    # 判断表是否存在
    table_check = "SELECT name FROM sqlite_master WHERE type='table';"
    cur.execute(table_check)
    # 返回所有表名[[('cq_2021_1',), ('cq_2021_2',), ('cq_2021_3',), ('cq_2021_4',), ('cq_2021_5',), ('cq_2021_6',), ('cq_2021_7',), ('cq_2021_8',)]]
    tables = [cur.fetchall()]
    # 返回所有的表名["'cq_2021_1'", "'cq_2021_2'", "'cq_2021_3'", "'cq_2021_4'", "'cq_2021_5'", "'cq_2021_6'", "'cq_2021_7'", "'cq_2021_8'"]
    table_list = re.findall('(\'.*?\')', str(tables))
    # 去掉双引号
    table_list = [re.sub("'", '', each) for each in table_list]

    sql = ''
    if month == 1 and today == 1:
        year -= 1
        month = 12
    for m in range(month):
        if ('hlj_' + str(year) + '_' + str(12 - m)) in table_list:
            sql = '''select * from {}'''.format('hlj_' + str(year) + '_' + str(12 - m))
            lastsql = '''select * from {}'''.format('hlj_' + str(year) + '_' + str(12 - m - 1))
            month = 12 - m
            break
    data = cur.execute(sql)
    for num in data:
        datalist.append(num)
    lastdata = cur.execute(lastsql)
    for lastnum in lastdata:
        lastdatalist.append(lastnum)

    # 确定最近更新的数据的日期,及存放本月及上月销量总和
    totalsal = 0
    lasttotalsal = 0
    totalfaqi = 0
    day_suo = 0
    for d in range(31):
        if datalist[d][1] == 0 and d > 0 and day_suo == 0:
            today = d
            day_suo += 1
    for d in range(today):
        totalsal += datalist[d][1]
        lasttotalsal += lastdatalist[d][1]
        totalfaqi += datalist[d][11]
    cur.close()
    conn.close()
    return render_template('heilongjiang.html',month = month, today = today, datalist = datalist, totalsal = totalsal, lasttotalsal = lasttotalsal,lastdatalist = lastdatalist,totalfaqi=totalfaqi)



if __name__ == '__main__':
    app.run()
