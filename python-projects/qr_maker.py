import qrcode

# insert link of the website of choice
# link = 'https://haileyrthomas01.github.io/'

print("Enter the link you'd like to create a QR code for:" )
link = input()

# create qr code
# the version parameter is an integer from 1 to 40 that controls the size of the QR code.
# the box_size parameter controls how many pixels each “box” of the QR code is.
# the border parameter controls how many boxes thick the border should be.
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

# data (link) is added
qr.add_data(link)

# qr code is made
qr.make()

# save the created QR code in an img pillow object using qr.make_image()
img = qr.make_image(fill_color = '#567f69', back_color = 'white')

# file name
img.save('portfolio_qr.png')