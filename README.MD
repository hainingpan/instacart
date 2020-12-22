
# Search items across stores on **Instacart** (`search.py`)
By default, **Instacart** does not provide users with the ability to search items across different store. This python code will automatically open all the search pages of a particular thing for you, for example, to compare prices and check availabilities.
## Usage
1. Log in your **Instacart** account
2. Download and unzip to local directory
3. Locate that directory, and type `python search.py` in the command line
4. Search pages will open as new tabs in your default browser

## Limits
This code is constructed based on my neighborhood. Searching based on any zip code might be considered in the future version. The code needs to read the html of the receipt to convert.

# Convert receipt of instacart to csv file (`receipt2csv.py`)
`receipt2csv.py` will automatically convert the receipt of instacart to csv file, which can be further copied to, e.g., Google sheets, to split the bill with others.
## Usage
1. Log in your **Instacart** account
2. Click `Your orders`->`View order detail`->`View Receipt`. Once the receipt is loaded, download the whole webpage by right-clicking and choosing `Save as..`
3. Copy the downloaded html file to the same directory as the code's
4. Type `python receipt2csv.py` in the command line
5. The prompt asks for the file name. Type the filename of download html file or leave it blank by just pressing `Enter`, which will automatically convert all html files in the code directory
6. The output csv files are in the same directory. To reuse the csv files, open it from app like Excel, select all the data, copy and paste to Google sheets
## Limits
* Acquiring token may be bothersome to this lightweight code, so it requires you to download the webpage first
* Pipeline from obtaining the token to acquiring the access of Google Sheets to directly read and write may be considered in the future version
