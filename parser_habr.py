import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://habrahabr.ru/top/'

def get_html(url):
	response = urllib.request.urlopen(url);
	return response.read();

def parse(html):
	soup = BeautifulSoup(html)
	print(soup);

def main():
	parse(get_html(BASE_URL));


if __name__ == '__main__':
	main();