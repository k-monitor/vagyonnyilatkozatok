import codecs
import json

from urllib import unquote

from bs4 import BeautifulSoup


def read_file_contents(path):
    with codecs.open(path, encoding='utf-8') as infile:
        return infile.read().strip()


def get_soup(html_file):
    html_str = read_file_contents(html_file)
    return BeautifulSoup(html_str, 'html.parser')


def write_json(path, data):
    with codecs.open(path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False, sort_keys=True)



html_file = 'kepviselok.html'

soup = get_soup(html_file)
table = soup.find('table')
links = table.find_all('a', href=True)

pdf_url_template = 'http://www.parlament.hu/egy-kepviselo-adatai?p_p_id=pairproxy_WAR_pairproxyportlet_INSTANCE_9xd2Wc9jP4z8&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_pairproxy_WAR_pairproxyportlet_INSTANCE_9xd2Wc9jP4z8_pairAction=%2Finternet%2Fcplsql%2Fogy_vagyonpub.vagyon_kiir_egys%3FP_FNEV%3D%2F2014%2F{}_j0141231k.pdf%26p_cont%3Dapplication%2Fpdf'
person_url_template = 'http://www.parlament.hu/aktiv-kepviseloi-nevsor?p_auth=wpyC4gC6&p_p_id=pairproxy_WAR_pairproxyportlet_INSTANCE_9xd2Wc9jP4z8&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_pairproxy_WAR_pairproxyportlet_INSTANCE_9xd2Wc9jP4z8_pairAction=%2Finternet%2Fcplsql%2Fogy_kpv.kepv_adat%3Fp_azon%3D{}%26p_stilus%3D%26p_head%3D'

data = {}

for l in links:
    name = l.text
    href = unquote(l.attrs['href'])
    id = href.split('p_azon=')[1].split('&p_stilus')[0]
    pdf_url = pdf_url_template.format(id)
    person_url = person_url_template.format(id)

    data[id] = {
        'name': name,
        'pdf_url': pdf_url,
        'person_url': person_url
    }

write_json('data.json', data)


