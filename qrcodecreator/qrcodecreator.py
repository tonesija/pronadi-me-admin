import pyqrcode
from PIL import Image
import hashlib
from pathlib import Path
import os

print('Upisite ime natjecanja:')
competitionName = input()

print('Upisite broj kodova:')
numofcodes = input()

logo = Image.open('logo-za-qr.png')
logomask = Image.open('logo-mask.png')

logo_size = 420

folderpath = Path(competitionName + '/')

if(os.path.isdir(folderpath) == False):
    os.mkdir(folderpath)

textfile = open(folderpath / (competitionName + '.json'), 'w+')
textfile.write('[\n')

for x in range(int(numofcodes)):

    codename = competitionName + '-' + str(x + 1).zfill(len(numofcodes))

    h = hashlib.new('ripemd160')
    h.update(codename.encode('utf-8'))
    codecode = h.hexdigest()

    strtowrite = '\t{\n\t\t"name": "' + codename + '",\n\t\t"password": "' + codecode + '",\n\t\t"hint": ""\n\t}'

    textfile.write(strtowrite)

    if(x+1 != int(numofcodes)):
        textfile.write(',')

    textfile.write('\n')

    qrcodeobj = pyqrcode.create('http://pronadi.me/#/claim/?code=' + codecode)

    qrcodepath = folderpath / (codename + '.png')
    # print(qrcodepath)s
    
    with open(qrcodepath, 'wb+') as qrcodefile:
        qrcodeobj.png(qrcodefile, scale=23, module_color=[41, 29, 54, 255], background=[0xe8, 0xd2, 0xcd])


    qrcodeimg = Image.open(qrcodepath)
    qrcodeimg = qrcodeimg.convert('RGBA')
    width, height = qrcodeimg.size
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    logo = logo.resize((xmax - xmin, ymax - ymin))
    logomask = logomask.resize((xmax - xmin, ymax - ymin))

    qrcodeimg.paste(logo, (xmin, ymin, xmax, ymax), logomask)
    # qrcodeimg.show()
    qrcodeimg.save(qrcodepath)


    
textfile.write(']')
textfile.close()