import requests
from copy import deepcopy
import pandas as pd
from bs4 import BeautifulSoup
from settings import URL, LOCATION, TYPE, RESULTS, HEADERS
from items import SEARCH_ITEMS_LIST
from requirements import check_requirements

def set_search_params(item_name = "", min_price = None, max_price = None, location = None, type = None):
    if min_price : min_price_param = "&_udlo={}".format(min_price)
    if max_price : max_price_param = "&_udhi={}".format(max_price)
    location_param = LOCATION[location] if location else ""
    type_param = TYPE[type] if type else ""
    return URL.format(item_name, min_price_param, max_price_param, location_param, type_param)


#s-item__dynamic s-item__purchaseOptionsWithIcon;;;; este é onde está o "comprar já" ou com "oferta direta"
#s-item__bids s-item__bidCount;; isto seria para caso houvesse bid_count
#s-item__dynamic s-item__buyItNowOption; se tiver auction e a opção de comprar já
#s-item__shipping s-item__logisticsCost; span onde tem o shipping cost ("+EUR 90,00 de frete" ou "Frete não especificado")


def get_results(url, file_name, item_name):
    html_elements = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html_elements, "lxml")
    items_list = soup.find("ul", class_ = "srp-results srp-list clearfix")
    items = items_list.find_all("li", {"class": ["s-item s-item__pl-on-bottom", "s-item__before-answer"]})
    results_dict = deepcopy(RESULTS)
    result_count = 0
    for item in items:
        item_title = item.find("div", class_="s-item__title").find("span").text #s-item__info clearfix
        item_state = item.find("span", class_ = "SECONDARY_INFO").text
        item_url = item.find("a", class_ = "s-item__link", href = True)['href']
        item_price_text = item.find("span", class_="s-item__price").text.replace(",", ".").replace("\xa0", "").split()
        for price_text in item_price_text:
            try:
                item_price = int(float(price_text))
                break 
            except ValueError:
                pass
        item_location = item.find("span", class_ = "s-item__location s-item__itemLocation").text
        is_auction = "Yes" if item.find("span", class_="s-item__bids s-item__bidCount") else "No"
        purchase_options = item.find("span", class_="s-item__dynamic s-item__purchaseOptionsWithIcon")
        purchase_options = purchase_options.text if purchase_options else "No other purchase options"
        
        try : # in some cases the item does not have any message regarding shipping 
            shipping_cost_text =  item.find("span", class_="s-item__shipping s-item__logisticsCost").text.replace(",", ".").split()
        except:
            shipping_cost = "Shipping cost was not specified"
            total_cost = item_price

        for string in shipping_cost_text: #can either have the shipping cost or "shipping cost was not specified"
            try:
                shipping_cost = int(float(string))
                total_cost = shipping_cost + item_price
                break 
            except ValueError:
                shipping_cost = "Shipping cost was not specified"
                total_cost = item_price

        results_dict["Title"].append(item_title)
        results_dict["URL"].append(item_url)
        results_dict["Item State"].append(item_state)
        results_dict["Item Price"].append(item_price)
        results_dict["Item Location"].append(item_location)
        results_dict["Shipping Cost"].append(shipping_cost) 
        results_dict["Total Cost"].append(total_cost)
        results_dict["Type Auction"].append(is_auction)
        results_dict["Purchase Options"].append(purchase_options)
        result_count +=1
        if "s-item__before-answer" in item["class"] : break
        
    df = pd.DataFrame.from_dict(results_dict).sort_values(['Type Auction', 'Total Cost'],
              ascending = [True, True]).to_excel("results/" + file_name + ".xlsx")

        

if __name__ == "__main__":
    check_requirements()
    for item in SEARCH_ITEMS_LIST:
        item_name = item["item_name"].replace(" ", "+")
        url = set_search_params(item_name, item["min_price"], item["max_price"], item["location"], item["type"])
        print("Searching on ebay for:", item["item_name"], "using the following URL:",url)
        get_results(url, item["output_file_name"], item["item_name"])
