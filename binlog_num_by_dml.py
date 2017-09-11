#encoding:utf-8

import sys
import subprocess

def convert_mysqlbinlog_txt_format(starttime,endtime,filename):
	# 二进制日志binlog转成文本格式binlog
	cmdstr = "mysqlbinlog --base64-output=decode-rows -v -v --start-datetime='%s' --stop-datetime='%s' %s"%(starttime,endtime,filename)
	file_binlog = subprocess.Popen(cmdstr)
	# return file_binlog
	handler_file_binlog(file_binlog)

def handler_file_binlog(file_binlog):
	# 过滤出insert/update/delete 
	with open(file_binlog) as f:
		for line in f:
			line = line.strip()
			if line.startswith(''):
				group_by_dml(line)

def group_by_dml(line):
	# 统计dml在表上操作的次数
	dml = dict()
	if line not in dml:
		dml[line] = dml.setdefault(line,1)
	else:
		dml[line] = dml.get(line)+1
	return dml

def top10():
	# 筛选出对表最频繁dml
	res = group_by_dml(line)
	data = res.items()
	print sorted(data,key=lambda data:data[1],reverse=True)[:10]

if __name__=="__main__":
	if len(sys.argv)==1:
		print 'python binlog_num_by_dml.py "2017-01-01 12:00:01" "2017-01-01 13:00:01" mysql-bin.000002'
	elif sys.argv[1] == '' or sys.argv[2] == '' or sys.argv[3] == '':
		print "缺少参数"
	else:
		convert_mysqlbinlog_txt_format(sys.argv[1],sys.argv[2],sys.argv[3])
		print sys.argv[1:]




