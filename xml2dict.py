#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/4/6 17:15
"""
import xmltodict,json,time,os,csv,sys



def parse_xml(file_path):
    '''
    给定一个文件的路径，返回分析结果的字典
    '''

    phone_deal = {       'PROD_INST_ID':'',
                         'LATN':'',
                         'BUSI_NBR':"",
                         'USER_NAME':'',
                         'CUST_NAME':'',
                         'CUST_ID':'',
                         'INSTALL_ADDR':'',
                         'PROD':'',
                         'BRAND':'',
                         'COMBO':'',
                         'CITY_TYPE':'',
                         'CUST_TYPE':'',
                         'STRATE_GROUP':'',
                         'VIP_LEVEL':'',
                         'CUST_LEVEL':'',
                         'USER_STATE':'',
                         'ORG_ID':'',
                         'CERTIFICATES_NBR':''
                         }

    file_modtime = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(os.path.getmtime(file_path)+8*3600))

    with open(file_path,encoding='gb2312') as f:
        mystr = f.read()
    xml_dict = xmltodict.parse(mystr)
    phone_dict = xml_dict['root']['data']['Users']['entity']
    file_dict = {}
    for i in phone_deal.keys():
        file_dict[i] = phone_dict[i]
    file_dict['mod_time'] = file_modtime

    return file_dict


if __name__ == '__main__':
    if len(sys.argv) == 0:
        sys.exit(11)
    count=1
    fileStruct = ("PROD_INST_ID",
                      "CUST_ID",
                      "LATN",
                      "BUSI_NBR",
                      "USER_NAME",
                      "CUST_NAME",
                      "INSTALL_ADDR",
                      "CERTIFICATES_NBR",
                      "mod_time")
    content=[]
    for root,dirs,files in os.walk(sys.argv[1]):
        for i in files:
            file_path = os.path.join(root,i)
            print('count={0}:{1}'.format(count, file_path))
            file_parse = parse_xml(file_path)
           # print(file_parse)
            content_row = []
            for j in fileStruct:
                content_row.append(file_parse.get(j))
            print(content_row)
            content.append(content_row)
    with open('./{0}.csv'.format('186'), 'w', newline='', encoding='utf-8') as f2:
        csv_write = csv.writer(f2)
        csv_write.writerows(content)

