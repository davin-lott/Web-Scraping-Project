from urllib.request import urlopen
from bs4 import BeautifulSoup
import re




books_of_scripture = ["ot","nt","bofm"]
the_book_of_scripture = books_of_scripture[2] #change this from 0 to 2 to pick from 0: Old Testament, 1: New Testament 2: Book of Mormon
url = f"https://www.churchofjesuschrist.org/study/scriptures/{the_book_of_scripture}?lang=eng"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


#for one chapter books
    # "sectionTitle-_Dn99 item-U_5Ca"
#for regular books
    # "sectionTitle-_Dn99 sectionDrawer-yKL0i"
urls = list(soup.find_all(class_ = "sectionTitle-_Dn99 sectionDrawer-yKL0i")) #finds all books in the scripture
urls_strings = []
single_chapter_urls = list(soup.find_all(class_ = "sectionTitle-_Dn99 item-U_5Ca")) #finds books in the scripture
#titles = list(soup.find_all(class_ = "sc-42v4-0 caNosj heading-Vx_DR heading-Vx_DR label"))

for thing in urls:
    urls_strings.append(str(thing))

for thing in single_chapter_urls:
    urls_strings.append(str(thing))

urls_strings = ''.join(urls_strings)
results = re.findall(f"{the_book_of_scripture}/.*?\?lang", urls_strings)

names = []
for part in results:
    names.append(re.findall("/.*?\?", part)[0])



for x in range(len(names)):
    book = names[x]   
    print(book)
    url_to_count = f"https://www.churchofjesuschrist.org/study/scriptures/{the_book_of_scripture}/{book}?lang=eng"
    page_for_counting = urlopen(url_to_count)
    html_for_counting = page_for_counting.read().decode("utf-8")
    soup_for_counting = BeautifulSoup(html_for_counting, "html.parser")

    chapters = list(soup_for_counting.find_all(class_ = "sc-omeqik-0 ewktus list-tile listTile-WHLxI", href = True))
    chapters = [x['href'] for x in chapters]
    print(len(chapters))
    print()