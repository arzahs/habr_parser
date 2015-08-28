import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://habrahabr.ru/top/'

def get_html(url):
	response = urllib.request.urlopen(url);
	return response.read();

def get_pages_count(html):
	soup = BeautifulSoup(html,  'html.parser')
	html_nav = soup.find('ul', id='nav-pages')
	count = int(html_nav.findAll('a')[-1].text)
	return count



def parse(html):
	soup = BeautifulSoup(html)
	html_content = soup.find('div', class_='content_left')
	html_posts = html_content.findAll('div', class_='post')
	posts = []
	for html_post in html_posts:
		posts.append({
			'title' : html_post.find('h1', class_='title').a.text,
			#'hubs' : 
			'content' : html_post.find('div', class_='content').text
			})
	return posts

def main():
	page_count = get_pages_count(get_html(BASE_URL))
	print('Найдено страниц %d' % page_count)
	posts = []
	for page in range(1, page_count):
		posts.extend(parse(get_html(BASE_URL + 'page%d' % page)))
	for post in posts:
		print(post);

if __name__ == '__main__':
	main();