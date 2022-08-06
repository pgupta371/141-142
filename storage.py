import csv

from main import liked_article

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
unliked_articles = []
did_not_read = []