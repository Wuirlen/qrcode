import pyqrcode

link = 'https://rocketseat.com.br/'

pyqrcode.create(link).svg('qrcode.svg',scale=10)