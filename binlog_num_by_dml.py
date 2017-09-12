# encoding:utf-8

import sys
import os
import datetime


def handler_binlog_to_dml_num(startime,endtime,filename):
    # 定义字典存储每个表dml的次数
    num_dml = dict()
    cmd = "/usr/bin/mysqlbinlog --base64-output=decode-rows -v -v  --start-datetime='%s' --stop-datetime='%s' %s" % (
        starttime, endtime, filename)
    binlogtxtfile = os.popen(cmd).readlines()
    for line in binlogtxtfile:
        line =  line[3:].lstrip()
        if line.startswith('UPDATE') or line.startswith('INSERT INTO') or line.startswith('DELETE FROM'):
            line = (line.strip(),)
            num_dml[line] = num_dml.get(line,0)+1
    
    #筛选出top10的dml的表
    res = num_dml.items()
    data = sorted(res,key=lambda res:res[1],reverse=True)[:10]
    for k,v in data:
        print "dml:%s-%s次数"%(k[0].replace('FROM','').replace('`',''),v)

if __name__=="__main__":
    dt = datetime.datetime.now()
    ds = datetime.datetime.strftime(dt,'%Y-%m-%d %H:%M:%S')
    if len(sys.argv) == 1:
        print "Usage: python %s '%s' '%s' %s"%(sys.argv[0],ds,ds,'mysql-bin.000001')
    elif sys.argv[1] == '' or sys.argv[2] =='' or sys.argv[3] == '':
        print "参数不能为空"
    else:
        starttime = sys.argv[1]
        endtime = sys.argv[2]
        filename = sys.argv[3]
        handler_binlog_to_dml_num(starttime,endtime,filename)