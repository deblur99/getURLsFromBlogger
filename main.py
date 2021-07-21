# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

import requests
import bs4


def get_document(url):
    req = requests.get(url)

    if req.status_code == 200:
        html = req.text
        soup = bs4.BeautifulSoup(html, "html.parser")
        return soup # return the instance of bs4

    else:
        print("Getting code is failure")
        return None


def find_image_links(soup):
    # init variables
    paths = list()
    result = list()

    paths = soup.select("div.separator > a")

    for path in paths:
        result.append(path.get('href'))

    return result


url = "https://deblur99.blogspot.com/2021/07/uploading21-07-21.html"
soup = get_document(url)

f = open("./link_list.txt", 'w')

if soup is not None:
    linkList = find_image_links(soup)

    # additional deletion
    # linkList[6] = ""
    # linkList[24] = ""

    for link in linkList:
        if link != "":
            f.write(f'<img src=\"{link}\">\n')

    f.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
