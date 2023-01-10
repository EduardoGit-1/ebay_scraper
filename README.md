# Ebay Scrapper

This repo contains all the code used for web scrapping [ebay.com](https://www.ebay.com/).

## Installation
In order to run this project you'll need to have ```Python``` installed.
There's no need to manually install packages, once you run the ```main.py``` all the required python modules will be automatically installed by using [pip](https://pip.pypa.io/en/stable/) package manager.

## Usage

To  run this project simply run the following bash command after you set all the [search parameters](#search-parameters) that you desire.

```bash
python3 main.py
```
### Search parameters
In order to search the desired items add a ```dict``` to the ```SEARCH_ITEMS_LIST``` array on the ```items.py``` file. All the required keys are described on the following table.

| Key         | Possible values|
| :------------------:|---------------|
| ```item_name``` | Insert a ```str``` that describes the item that you want to search.
| ```min_price``` | Insert an ```integer``` or ```None``` if you don't want to specify a minimum value.
| ```max_price``` | Insert an ```integer``` or ```None``` if you don't want to specify a maximum value.
| ```location``` | ```"Any"```, ```"Europe"```, ```"North America"```, ```"US Only"``` or ```"Asia"``` depending on the location you want to search on.
| ```type``` | ```"Any"```, ```"Buy Now"```, ```"Auction"``` or ```"Offer"```. This key filters the type of buying options, select accordingly.
| ```output_file_name``` | ```str``` that specifies the output sheet name for this item.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
