

class Symbols:
    def __init__(self, name: str, description: str = ""): #Initializer (name attribute is required) description is optional
        self._name = name
        self._description = description
        self._mentions = {  #Contains all the embedded objects. Theyre called dictionaries in python though.
            "day": {
                "total": 0,
                "scrapes": []
            },
            "week": {
                "total": 0,
                "scrapes": []
            },
            "month": {
                "total": 0,
                "scrapes": []
            }
        }
    

#Below is a function for retrieving data on either day week or month and formatting it nicely so its more readable. Its not really
# necessary for the site but its useful for making sure youre formatting data correctly

    def getDataOn(self, period: str) -> str:  
        startstr =  period.upper() + ": " + self._name + "\n\nTotal: " + str(self._mentions[period]["total"]) + "\n\nScrapes: \n" 
        endstr = ""
        for i in range(len(self._mentions[period]["scrapes"])):
            tempmen = str(self._mentions[period]["scrapes"][i]["mentions"])
            temptime = self._mentions[period]["scrapes"][i]["time"]
            tempsrc = self._mentions[period]["scrapes"][i]["source"]
            endstr += "\n Mentions: " + tempmen + "\n Time: " + temptime + "\n Source: " + tempsrc + "\n" + ("=" * 20) 
        return startstr + endstr


#This function adds a scrape using its data. This function along with the one above have examples below the class.

    def addScrape(self, mentions: int, time, source: str):
        scrape = {}  #empty dictionary created

        scrape["mentions"] = mentions  #fill the dictionary with data
        scrape["time"] = time
        scrape["source"] = source

        self._mentions["day"]["total"] += mentions  #update the overall mentions
        self._mentions["day"]["scrapes"].append(scrape)  #add the dictionary to the list of scrapes within day week or month

        self._mentions["week"]["total"] += mentions
        self._mentions["week"]["scrapes"].append(scrape) #""

        self._mentions["month"]["total"] += mentions
        self._mentions["month"]["scrapes"].append(scrape) #""

#end of class


test = Symbols("TSLA")   #Creates instance of Symbols class with the name set to "TSLA"

test.addScrape(14, "00:00", "reddit") #Adds 2 scrapes using the addScrape function
test.addScrape(4, "00:00", "reddit")

print(test._name) #Uses the getDataOn function to format the data for the week nicely. Run to see results






