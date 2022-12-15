URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&rt=nc{}{}{}{}" # item name; min_price; max_price; location; type

LOCATION = {
    "Any" : "",
    "Europe" : "&LH_PrefLoc=5",
    "North America" : "&LH_PrefLoc=4",
    "US Only" : "&LH_PrefLoc=3",
    "Asia" : "&LH_PrefLoc=6"
}

TYPE = {
    "Any" : "",
    "Buy Now" : "&LH_BIN=1",
    "Auction" : "&LH_Auction=1",
    "Offer" : "&LH_BO=1"
}

RESULTS = {
    "Title" : [],
    "URL" : [],
    "Item State" : [],
    "Item Price" : [],
    "Item Location" : [],
    "Shipping Cost" : [],
    "Total Cost" : [],
    "Type Auction" : [],
    "Purchase Options" : [],
}

HEADERS = {'User-Agent': 'Mozilla/5.0'}