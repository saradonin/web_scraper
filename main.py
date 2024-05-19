import requests
from bs4 import BeautifulSoup


URL = 'https://luxuryforless.pl/przedsprzedaz'
prev_list = [{'name': 'Goldfield & Banks Sunset Hour woda perfumowana 100 ml', 'link': 'https://luxuryforless.pl/p/55/81715/goldfield-amp-banks-sunset-hour-woda-perfumowana-100-ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '417,60'}, {'name': 'Bon Parfumeur 003 yuzu feuilles de violette, vétiver woda perfumowana 100 ml', 'link': 'https://luxuryforless.pl/p/55/81710/bon-parfumeur-003-yuzu-feuilles-de-violette-vetiver-woda-perfumowana-100-ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '160,80'}, {'name': 'Bon Parfumeur 002 Neroli Jasmine White Amber woda perfumowana 100 ml', 'link': 'https://luxuryforless.pl/p/55/81709/bon-parfumeur-002-neroli-jasmine-white-amber-woda-perfumowana-100-ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '159,20'}, {'name': 'Berdoues 1902 THE VERT woda kolońska 125 ml', 'link': 'https://luxuryforless.pl/p/27/81708/berdoues-1902-the-vert-woda-kolonska-125-ml-perfumy-niszowe-dla-kobiet-.html', 'price': '31,60'}, {'name': 'Theodoros Kalotinis Cherry Powder woda perfumowana 50 ml', 'link': 'https://luxuryforless.pl/p/27/81707/-theodoros-kalotinis-cherry-powder-woda-perfumowana-50-ml-perfumy-niszowe-dla-kobiet-.html', 'price': '176,00'}, {'name': 'Theodoros Kalotinis Caramel Oud woda perfumowana 50 ml', 'link': 'https://luxuryforless.pl/p/27/81705/theodoros-kalotinis-caramel-oud-woda-perfumowana-50-ml-perfumy-niszowe-dla-kobiet-.html', 'price': '176,00'}, {'name': 'EIGHT & BOB La Musique de Christie Extrait de Parfum 50 ml', 'link': 'https://luxuryforless.pl/p/55/81694/eight-amp-bob-la-musique-de-christie-extrait-de-parfum-50-ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '600,00'}, {'name': 'Giardino Benesserer Hera Extrait de Parfum 100 ml', 'link': 'https://luxuryforless.pl/p/55/81693/giardino-benesserer-hera-extrait-de-parfum-100-ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '388,00'}, {'name': 'Astrophil & Stella Shanghai 1930 Extrait de Parfum 50 ml', 'link': 'https://luxuryforless.pl/p/27/81688/astrophil-amp-stella-shanghai-1930-extrait-de-parfum-50-ml-perfumy-niszowe-dla-kobiet-.html', 'price': '324,00'}, {'name': 'Lengling Munich Sekushi No. 7 ekstrakt perfum 100 ml', 'link': 'https://luxuryforless.pl/p/27/81685/lengling-munich-sekushi-no-7-ekstrakt-perfum-100-ml-perfumy-niszowe-dla-kobiet-.html', 'price': '708,00'}, {'name': 'DS & Durga D.S. woda perfumowana 50 ml', 'link': 'https://luxuryforless.pl/p/55/81680/ds-amp-durga-d-s-woda-perfumowana-50-ml--wyprzedaz-dla-kobiet-outlet.html', 'price': '674,40'}, {'name': 'DS & Durga Durga woda perfumowana 50 ml', 'link': 'https://luxuryforless.pl/p/55/81679/ds-amp-durga-durga-woda-perfumowana-50-ml--wyprzedaz-dla-kobiet-outlet.html',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'price': '706,40'}, {'name': 'DS & Durga Rose Atlantic woda perfumowana 100 ml', 'link': 'https://luxuryforless.pl/p/55/81676/ds-amp-durga-rose-atlantic-woda-perfumowana-100-ml--wyprzedaz-dla-kobiet-outlet.html', 'price': '481,60'}, {'name': 'Giardino Benessere Hestia Extrait de Parfum 100 ml', 'link': 'https://luxuryforless.pl/p/55/81670/giardino-benessere-hestia-extrait-de-parfum-100-ml--wyprzedaz-dla-kobiet-outlet.html', 'price': '481,60'}, {'name': 'Gritti Beyond The Wall Extrait de Parfum 100 ml', 'link': 'https://luxuryforless.pl/p/55/81669/gritti-beyond-the-wall-extrait-de-parfum-100-ml--wyprzedaz-dla-kobiet-outlet.html', 'price': '546,40'}, {'name': "EIGHT & BOB Le Geste d'Edmond Extrait de Parfum 50 ml", 'link': 'https://luxuryforless.pl/p/55/81665/eight-amp-bob-le-geste-d-edmond-extrait-de-parfum-50-ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '600,00'}, {'name': 'Serge Lutens La Dompteuse Encagee woda perfumowana 50 ml', 'link': 'https://luxuryforless.pl/p/27/81657/serge-lutens-la-dompteuse-encagee-woda-perfumowana-50-ml-perfumy-niszowe-dla-kobiet-.html', 'price': '224,80'}, {'name': 'Rosendo Mateu 1968 woda perfumowana 100ml', 'link': 'https://luxuryforless.pl/p/55/81649/rosendo-mateu-1968-woda-perfumowana-100ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '528,00'}, {'name': 'Rosendo Mateu 1970 woda perfumowana 100ml', 'link': 'https://luxuryforless.pl/p/55/81648/rosendo-mateu-1970-woda-perfumowana-100ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '528,00'}, {'name': 'Viktor&Rolf Spicebomb Infrared woda toaletowa 90 ml', 'link': 'https://luxuryforless.pl/p/56/81535/viktor-amp-rolf-spicebomb-infrared-woda-toaletowa-90-ml-wyprzedaz-dla-mezczyzn-outlet.html', 'price': '246,80'}, {'name': 'Regalien Diamond Of Velvet Extrait de Parfum 50 ml', 'link': 'https://luxuryforless.pl/p/27/81507/-regalien-diamond-of-velvet-extrait-de-parfum-50-ml-perfumy-niszowe-dla-kobiet-.html', 'price': '680,00'}, {'name': 'V Canto Giullare Extrait de Parfum 100ml', 'link': 'https://luxuryforless.pl/p/55/81505/-v-canto-giullare-extrait-de-parfum-100ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '640,00'}, {'name': 'Baldessarini Baldessarini Black woda toaletowa 75ml', 'link': 'https://luxuryforless.pl/p/56/81315/baldessarini-baldessarini-black-woda-toaletowa-75ml-wyprzedaz-dla-mezczyzn-outlet.html', 'price': '40,00'}, {'name': '4711 Acqua Colonia Lychee White Mint woda kolońska 170 ml', 'link': 'https://luxuryforless.pl/p/55/81165/4711-acqua-colonia-lychee-white-mint-woda-kolonska-170-ml-wyprzedaz-dla-kobiet-outlet.html', 'price': '39,04'}]


def request_content(url):
    r = requests.get(url)

    # check status code for response received
    print(r)

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def extract_product_into(content):
    s = content.find('div', class_='listning-boxes container-fluid')
    products = s.find_all('div', class_='product-info row')

    list = []

    for item in products:
        name_h2 = item.find('h2', class_='product-name')
        name_a = name_h2.find('a')
        price_1 = item.find('span', class_='price_1')
        price_2 = item.find('span', class_='price_2')

        name_title = name_a.get('title', 'N/A').strip() if name_a else 'N/A'
        name_href = name_a.get('href', 'N/A') if name_a else 'N/A'
        price_1_text = price_1.get_text(strip=True) if price_1 else 'N/A'
        price_2_text = price_2.get_text(strip=True) if price_2 else 'N/A'
        price_text = price_1_text + price_2_text

        object = {
            "name": name_title,
            "link": name_href,
            "price": price_text
        }

        list.append(object)

        # print(f"{name_title} - {price_text} PLN \n {name_href} \n")
    return list


def print_list(list):
    for item in list:
        print(f"{item['name']} - {item['price']} PLN\n {item['link']}")


def compare_lists(list_1, list_2):
    return [item for item in list_1 if item not in list_2]


content = request_content(URL)
list = extract_product_into(content)
# print_list(list)
new_content = print(compare_lists(list, prev_list))
