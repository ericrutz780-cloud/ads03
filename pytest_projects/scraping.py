def scrape_website(name, url):
    #HTTP-Verbindung herstellen
    response = requests.get(url, allow_redirects=True)
    content = response.content
    text = response.text

    # (2) File name to store the raw HTML
    file_name = os.path.join(
        STORAGE_DIR,f"{str_now}-{name}.html")
    
    # (3) Write raw HTML
    with open(file_name, "wb") as f:
        f.write(response.content)

    # (4) Fill content_dict and text_dict
    content_dict[name] = response.content
    text_dict[name] = response.text

    # (5) Fill log_list
    log_info = dict(
        name=name,
        file_name=file_name,
        date=str_now,
        status_code=response.status_code,
        url=response.url,
        encoding=response.encoding,
    )
    log_list.append(log_info)

if __name__ == "__main__":
	for name, url in multiple_jp.items():
    try:
        scrape_website(name, url)
        print("Die URL wurde erfolgreich abgerufen \n%s" % (url))
    except:
        failed_list.append((name,url))
        print("Erfolgreich abgerufen \n%s /n%s" % (name, url))

