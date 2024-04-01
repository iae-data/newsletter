# Scraper

This is a simple web scraper that ...

## How to use

1. Install the requirements:

```bash
poetry install
```

2. Start Splash, Elasticsearch and Kibana:

```bash
docker compose up -d
```

Elasticsearch will be available at `http://localhost:9200` and Kibana at `http://localhost:5601`.

Splash will be available at `http://localhost:8050`.

3. To run the scraper use the following command:

```bash
poetry shell

scrapy crawl news_br_1 -o news.json
```
