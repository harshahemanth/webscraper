from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urequest

url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient = urequest(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "_3O0U0u"})

filename = "products.csv"
f = open(filename, "w")

headers = "Product_Name, Price, Rating\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container[0].text

    rating_container = container.findAll("div", {"class": "hGSR34"})
    rating = rating_container[0].text

    print("product_name:" + product_name)
    print("price:" + price)
    print("rating:" + rating)

    # Parsing
    trim_price = ''.join(price.split(','))
    print(trim_price)
    trim_symbol = trim_price.split('₹')
    print(trim_symbol[1])
    add_rs = 'Rs.' + trim_symbol[1]
    print(add_rs)
    trim_E = add_rs.split('E')
    print(trim_E)
    final_price = trim_E[0]
    print(final_price)

    # print(product_name.replace(",", "|") + "," + final_price + "," + rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + rating + "\n")
f.close()
