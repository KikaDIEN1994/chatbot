from requests import get

class WikiRequest:
    
    def __init__(self, lat, lng):
        self.status = "NOK"
        
        pageid = self.get_pageid(lat, lng)
        if pageid:
            self.summary = self.get_summary(pageid)
            self.status = "OK"
            print("status = OK")
        else:
            self.status = "NOK"
        print("An exeption occured")
        print("status NOK")

    def get_pageid(self, lat, lng): # doit etre en private
        lat_lng = "|".join([str(lat), str(lng)])
        parameters = {
            "action": "query",
            "list": "geosearch",
            "gscoord": lat_lng,
            "format": "json",
        }
        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()

        pageid = data["query"]["geosearch"][0]["pageid"]
        print(pageid)
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

        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        summary = data["query"]["pages"][str(pageid)]["extract"]
        print(summary)
        return summary

wikirequest = WikiRequest(0,2.2950275)
print(WikiRequest)
