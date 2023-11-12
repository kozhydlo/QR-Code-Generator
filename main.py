import qrcode

def get_qrcode(url='http://google.com', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')
    
    return f'QR code was created! Open the {name}.png'

def main():
    print(get_qrcode(url='https://kozhydlo.github.io/', name='WEBSITE'))
    print(get_qrcode(url='https://t.me/kozhydlo_mark', name='TELEGRAM'))
    

if __name__ == '__main__':
    main()
    

