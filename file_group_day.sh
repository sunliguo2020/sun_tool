#########################################################################
# File Name: /mnt/sdb3/bin/groupByDay.sh
# Author: sunliguo
# mail: sunliguo2006@qq.com
# Created Time: Mon 15 Jan 2018 01:18:05 PM CST
#2019-05-14:添加shuf随机。
#2019-05-18:添加统计文件个数file_count
#2019-05-19:增加处理带有空格的文件名
#2019-11-13:将移动文件放到后台执行
########################################################################
#!/bin/bash

PWD='./'
oldIFS=${IFS}

file_list=`find $PWD  -maxdepth 1 -name \*t -type f|shuf`

#带有空格的文件名会统计2次
file_count=`echo $file_list |wc -w`

Total=$file_count

IFS=$'\n'
for i in $file_list
do
    echo  Total:$Total#
    {
	MOD_TIME=`stat -c %y $i|awk '{print $1}'`
	if [ ! -d $MOD_TIME ];then
		mkdir $MOD_TIME
	fi
	#\mv -iv $i $MOD_TIME/ >/dev/null 2>&1
	\mv -iv $i $MOD_TIME/ 
     }
    	Total=$(($Total-1))
done 

wait

IFS=${oldIFS}
