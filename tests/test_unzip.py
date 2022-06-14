from zipfile import ZipFile

if __name__ == '__main__':
    flag = 'wechat'
    if flag == 'alipay':
        try:
            with ZipFile('/Users/cheng/Developer/bc-convert/input/alipay_record_20220613_155548.zip', 'r') as myzip:
                file_list = myzip.namelist()
                csv_file = myzip.read(name=file_list[0], pwd=b'167411')
                content = csv_file.decode('gbk')
                lines = content.split('\n')
                for line in lines:
                    print(line)
        except Exception as e:
            print(e)
    elif flag == 'wechat':
        try:
            with ZipFile('/Users/cheng/Developer/bc-convert/input/微信支付账单(20220424-20220613).zip', 'r') as myzip:
                file_list = myzip.namelist()
                csv_file = myzip.read(name=file_list[1], pwd=b'829597')
                content = csv_file.decode('utf-8-sig')
                lines = content.split('\n')
                for line in lines:
                    print(line)
        except Exception as e:
            print(e)
    else:
        pass
