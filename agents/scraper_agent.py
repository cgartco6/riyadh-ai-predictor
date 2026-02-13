import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

class ScraperAgent:

    def scrape(self, url):
        options = uc.ChromeOptions()
        options.headless = True

        driver = uc.Chrome(options=options)
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        horses = []

        rows = soup.find_all("div", class_="runner-row")

        for r in rows:
            horses.append({
                "name": r.find("span", class_="name").text.strip(),
                "weight": float(r.find("span", class_="weight").text),
                "draw": int(r.find("span", class_="draw").text),
                "rating": float(r.find("span", class_="rating").text),
                "form": r.find("span", class_="form").text
            })

        return horses
