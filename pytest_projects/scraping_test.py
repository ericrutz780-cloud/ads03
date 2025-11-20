from scraping import scrape_website

multiple_jp = dict(
    stps= "https://www.stepstone.de",
    idd= "https://de.indeed.com",
    lkn= "https://www.linkedin.com/jobs",
    mst= "https://www.monster.de",
    abg= "https://jobboerse.arbeitsagentur.de"
)

for name, url in multiple_jp.items():
    try:
        scrape_website(name, url)
        print("Die URL wurde erfolgreich abgerufen \n%s" % (url))
    except:
        failed_list.append((name,url))
        print("Erfolgreich abgerufen \n%s /n%s" % (name, url))
