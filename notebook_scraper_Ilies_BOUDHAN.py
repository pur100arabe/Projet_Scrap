import asyncio
import aiohttp
import feedparser
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def charger_flux(rss_file):
    with open(rss_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("RSS_URL")]

def charger_mots_cles(fichier_mots):
    with open(fichier_mots, "r", encoding="utf-8") as f:
        return [mot.lower().strip() for mot in f if mot.strip()]

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            content = await response.read()
            return url, content
    except Exception as e:
        logging.warning(f"Erreur de récupération pour {url} : {e}")
        return url, None

def parse_feed_content(content):
    try:
        feed = feedparser.parse(content)
        articles = []
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", "N/A")
            })
        return articles
    except Exception as e:
        logging.error(f"Erreur de parsing : {e}")
        return []

def filtrer_articles(articles, mots_cles):
    resultats = []
    for article in articles:
        texte = f"{article['title']} {article['summary']}".lower()
        for mot in mots_cles:
            if mot in texte:
                resultats.append({
                    "title": article["title"],
                    "published": article["published"],
                    "link": article["link"],
                    "keyword": mot
                })
                break
    return resultats

async def main_async():
    rss_urls = charger_flux("rss_list.txt")
    mots_cles = charger_mots_cles("mots_cles.txt")
    resultat_final = []

    logging.info(f"{len(rss_urls)} flux à scanner avec {len(mots_cles)} mots-clés.")

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in rss_urls]
        responses = await asyncio.gather(*tasks)

        for url, content in responses:
            if content:
                articles = parse_feed_content(content)
                resultat_final.extend(filtrer_articles(articles, mots_cles))

    for r in resultat_final:
        print(f"{r['published']} - {r['title']} ({r['keyword']})")
        print(f"URL : {r['link']}")
        print("-" * 80)

    with open("resultat.txt", "w", encoding="utf-8") as f:
        for r in resultat_final:
            f.write(f"{r['title']}\n{r['published']}\n{r['link']}\nMot-clé : {r['keyword']}\n\n")

    logging.info(f"{len(resultat_final)} articles sauvegardés dans resultat.txt.")

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main_async())
    logging.info(f"Terminé en {time.time() - start:.2f} secondes.")