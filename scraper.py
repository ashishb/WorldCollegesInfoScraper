""" World Colleges Info pages vary from
http://www.worldcolleges.info/college/page/0/0?field_colleges_name_value=&field_colleges_category_value=All&field_colleges_city_value=All&page=0
to
http://www.worldcolleges.info/college/page/0/0?field_colleges_name_value=&field_colleges_category_value=All&field_colleges_city_value=All&page=1217
"""

from bs4 import BeautifulSoup
import os
import urllib2

# Just add page number to this prefix to fetch the page.
_BASE_URL_PREFIX = (
    'http://www.worldcolleges.info/college/page/0/0?field_colleges_name_value=&'
    'field_colleges_category_value=All&field_colleges_city_value=All&page=')

_FIRST_PAGE = 0
# This might change over time.
_LAST_PAGE = 1217

_COLLEGE_NAME = 1
_UNIVERSITY = 2
_GRADUATION = 3
_COLLEGE_CATEGORY = 4


def FetchPage(page_num, colleges_dict):
    url = _BASE_URL_PREFIX + str(page_num)
    print 'Fetching %s' % url
    try:
      result = urllib2.urlopen(url)
      if result.getcode() == 200:
        data = result.read()
        soup = BeautifulSoup(data)
        for td_elem in soup.find_all('td'):
          # A hacky way to skip all logo containing useless entries.
          if str(td_elem).find('div') == -1:
            continue
          else:
            for child in td_elem.children:
              if str(child).startswith('<div'):
                  import pdb; pdb.set_trace()
    except urllib2.URLError as e:
      print 'Fetch failed:',
      print str(e)
      return False
    return True


def FetchPages(first_page, last_page, colleges_dict):
  for page_num in range(first_page, last_page + 1):
      FetchPage(page_num, colleges_dict)


def main():
  # A dictionary of college dictionaries.
  colleges_dict = dict()
  FetchPages(_FIRST_PAGE, _LAST_PAGE, colleges_dict)


if __name__ == '__main__':
  main()
