# binlog_num_by_dml
分析MySQL binlog中某个时间段dml次数,以便了解表访问情况

###使用
python binlog_num_by_dml.py '2017-09-11 16:37:21' '2017-09-11 16:45:38' mysql-bin.000016

###结果
dml:DELETE  myapp.slow_log-2次数
dml:UPDATE myapp.slow_log-1次数











