"""
exercise_06  Scraping and Saving

In this class you will write a class that scrapes and saves URLs. If the item to be scraped has been saved, it will
be opened from the save and returned without making a new web request.

This class will be named "Scrape_Saver" and has 3 definitions:

 1) an __init__ function that accepts a base_url to scrape and a save_location, both are strings
    * The base URL should be of the format "http://www.uniprot.org/uniprot/{}.fasta" where each item to be scraped
       will replace the {} in the base url ( this is done with base_url.format(item) )
    * The save location is the folder path where the text scraped will be saved

 2) a "retrieve" function that accepts a single argument, the name to be scraped. EX: 'P69892'
    * The retrieve definition should first check if the item to be scraped has already been scraped and saved
       to the save_location.
    * If it exists, then this function should read the file and return the contents without
       making a new web requests.
    * If the save does not exist, then the url should be scraped and saved as a string in a plain text file.

 3) a __str__ function that returns a list of files in the save_location


"""
import os
import urllib.request as ur


class Scrape_Saver:
    def __init__(self, base_url, save_location):
        self.url = base_url
        self.saveSpot = save_location
        if not os.path.exists(self.saveSpot):
            os.makedirs(self.saveSpot)
        return

    def retrieve(self, item):
        s = self.saveSpot + item
        if os.path.exists(s):#(item in os.listdir(self.saveSpot)):
            with open(s) as f:
                return f.readlines()
        else:
            url = self.url.format(item)
            value = ur.urlopen(url).read().decode()
            with open(self.saveSpot + item, 'w') as f:
                f.writelines(value)
            return value

    def __str__(self):
        return [file for file in os.listdir(self.saveSpot)]


if __name__ == '__main__':
    """
    Here is where the Scrape_Saver class is tested.
    """

    url = "http://www.uniprot.org/uniprot/{}.fasta"
    item = 'P69892'

    x = Scrape_Saver(url, 'saves/')
    print(x.retrieve(item))
    files = x.__str__()
    quitter = 0