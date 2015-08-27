import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = 'http://habrahabr.ru/top/'

def get_html(url):
	response = urllib.request.urlopen(url);
	return response.read();

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
	return posts;

def main():
	print(parse(get_html(BASE_URL)));


if __name__ == '__main__':
	main();