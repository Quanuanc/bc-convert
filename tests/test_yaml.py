import yaml

if __name__ == '__main__':
    try:
        with open('/Users/cheng/Developer/bc-convert/config/alipay.yaml', 'rb') as f:
            config = yaml.load(f, Loader=yaml.Loader)
            for item in config['alipay']['rules']:
                for k, v in item.items():
                    print(k + ' = ' + v)

    except Exception as e:
        print(e)
