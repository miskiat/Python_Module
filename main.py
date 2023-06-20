# fw = open('sample.txt','w')
# fw.write('writing some stuffs in the text\n')
# fw.write('i like juice \n')
# fw.close()
#
#
# fr = open('sample.txt','r')
# text = fr.read()
# print(text)
# fr.close()


from urllib import request
goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1655402674&period2=1686938674&interval=1d&events=history&includeAdjustedClose=true'
def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()
download_stock_data(goog_url)

# import random
# import urllib.request
# def download_web_image(url):
#     name = random.randrange(1, 1000)
#     full_name = str(name) + ".jpg"
#     urllib.request.urlretrieve(url,full_name)
#
# download_web_image("https://galafruit.net/wp-content/uploads/galafruit_mele.jpg")
