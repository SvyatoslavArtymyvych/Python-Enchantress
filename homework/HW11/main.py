import requests
from bs4 import BeautifulSoup
from re import finditer, M

pattern = r"<p>([А-яіїЇ -]*)\s<b>(\w*@vsau.vin.ua)"
url = 'http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83'


def find_strings(site_url: str, regex_pattern: str, html_tag: str, html_element_class: str):
    soup = BeautifulSoup(requests.get(site_url).text, 'html.parser')

    html_element = soup.find_all(html_tag, class_=html_element_class)

    result = finditer(pattern=regex_pattern,
                      string=str(html_element),
                      flags=M)

    strings = []
    for line in result:
        strings.append(f"{str(line.group(1)).strip()}, {line.group(2)}")

    return strings


if __name__ == '__main__':
    for string in find_strings(url, pattern, 'div', 'mw-content-ltr'):
        print(string)
