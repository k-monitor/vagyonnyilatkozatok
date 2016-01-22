from bs4 import BeautifulSoup
import codecs
import json


def read_file_contents(path):
    with codecs.open(path, encoding='utf-8') as infile:
        return infile.read().strip()


def get_person_names(links):
    person_list = []
    for item in links:
        if 'href' in item.attrs:
            if 'Ex1HAm6I' in item.attrs['href']:
                name = item.string.encode('utf-8')
                person_list.append(name)
    return person_list


def get_person_links(links):
    person_links = []
    for item in links:
        if 'href' in item.attrs:
            if 'Ex1HAm6I' in item.attrs['href']:
                person_links.append(item.attrs['href'])
    return person_links


def get_person_ids(links):
    p_links = get_person_links(links)
    id_list = []
    for link in p_links:
        person_id = find_id(link, '3D')
        id_list.append(person_id)
    return id_list


def find_id(str, substr):
    place = str.find(substr) + len(substr)
    str_id = str[place:place + 4]

    return str_id


def get_paper_list(links):
    ids = get_person_ids(links)
    paper_list = []

    for item in ids:
        id_to_replace = find_id(paper_url, '2014%2F')
        paper = paper_url.replace(id_to_replace, item)
        paper_list.append(paper)

    return paper_list


def create_json():
    names = get_person_names(links)
    papers = get_paper_list(links)

    list_to_json = [{'name': name, 'paper': paper} for name, paper in zip(names, papers)]

    jsonfile = 'PDFadatlapok.json'

    with open(jsonfile, 'wb') as outfile:
        json.dump(list_to_json, outfile)


webcim = 'kepviselo_list.html'
weblap = read_file_contents(webcim)
soup = BeautifulSoup(weblap, 'html.parser')
links = soup.find_all('a')
paper_url = 'http://www.parlament.hu/egy-kepviselo-adatai?p_p_id=pairproxy_WAR_pairproxyportlet_INSTANCE_9xd2Wc9jP4z8&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1&_pairproxy_WAR_pairproxyportlet_INSTANCE_9xd2Wc9jP4z8_pairAction=%2Finternet%2Fcplsql%2Fogy_vagyonpub.vagyon_kiir_egys%3FP_FNEV%3D%2F2014%2Fa716_j0141231k.pdf%26p_cont%3Dapplication%2Fpdf'

create_json()

