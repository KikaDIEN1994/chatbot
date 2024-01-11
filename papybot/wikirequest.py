import requests

class WikiRequest:

    def __init__(self,lat,lng):
        self.lat = lat
        self.lng = lng

    def get_pageid(self):
        lat_lng = "|".join([str(self.lat), str(self.lng)])
        parameters = {
            "action": "query",
            "list": "geosearch",
            "gscoord": lat_lng,
            "format": "json",
        }

        response = requests.get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        pageid = data["query"]["geosearch"][0]["pageid"]
        return pageid

    def get_summary(self, pageid):
        parameters = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1,
            "exsentences": "5",
            "pageids": pageid,
        }

        response = requests.get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        summary = data["query"]["pages"][str(pageid)]["extract"]
        #print(data)
        #print(data["query"]["pages"])
       # print(data["pages"])
       # print(data["extract"])
        return summary

"""
wikirequest = WikiRequest(48.85837009999999,2.2944813)
pageid = wikirequest.get_pageid()
print(wikirequest.get_summary(pageid))
"""
