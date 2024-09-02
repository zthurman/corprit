#!venv/bin/python

"""
corprit

References:
    - https://stackoverflow.com/a/67862253
    - https://beautiful-soup-4.readthedocs.io/en/latest/#navigating-the-tree
    - https://stackoverflow.com/a/36768533
    - https://docs.python.org/3/library/statistics.html#statistics.mean
"""

import requests
import bs4
import statistics


def find_sites_for_item(headers: dict, item_query_params: dict) -> list:
    """
    Make a google query with provided params and header.

    :returns: list(str)
    """
    googs = "https://www.google.com/search"
    soup = bs4.BeautifulSoup(
        requests.get(googs, params=item_query_params, headers=headers).content,
        "html.parser",
    )
    sites = list()
    for a in soup.select("a:has(h3)"):
        sites.append(a["href"])
    return sites


class ConsumerItem:
    """
    I believe the buzzword here is `encapsulation`.
    """

    def __init__(self, category, query_param, target_site):
        self.category = category
        self.query_param = query_param
        self.target_site = target_site
        self.name = None
        self.price = None

    @property
    def headers(self):
        """
        It's effectively a global without being global.
        """
        return {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
        }


def find_price_for_item(consumer_item: ConsumerItem):
    """
    Give us the item name and price using a mechanism
    that works for mom and pop sites but is wrecked
    by people who hate scrapers.

    :returns: a modified ConsumerItem
    """
    for target_site in find_sites_for_item(
        consumer_item.headers, consumer_item.query_param
    ):
        if consumer_item.target_site in target_site:
            target_site_request = requests.get(target_site)
            target_site_content = target_site_request.content
            target_soup = bs4.BeautifulSoup(target_site_content, "html.parser")
            consumer_item.name = target_soup.title
            consumer_item.price = target_soup.find(
                "meta", property="product:price:amount"
            )["content"]


consumer_items = [
    ConsumerItem(
        category="moderate_moderate",
        query_param={"q": "grumman 17 foot double ender canoe"},
        target_site="marathon",
    ),
    ConsumerItem(
        category="moderate_high",
        query_param={"q": "york 5 ton package"},
        target_site="hvacdirect",
    ),
]

moderate_prices = list()
for each in consumer_items:
    find_price_for_item(each)
    # print(each.name)
    # print(each.price)
    moderate_prices.append(float(each.price))

print(statistics.mean(moderate_prices))
