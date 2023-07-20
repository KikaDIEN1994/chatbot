from requests import get

class WikiRequest:

    def __init__(self,lat,lng):
        self.lat = lat
        self.lng = lng

    def _get_pageid(self):
        lat_lng = "|".join([str(self.lat), str(self.lng)])
        parameters = {
            "action": "query",
            "list": "geosearch",
            "gscoord": lat_lng,
            "format": "json",
        }
        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()

        print(data,(

        ),"data 1")
        pageid = data["query"]["geosearch"][0]["pageid"]
        #print(pageid)
        return pageid

    def get_summary(self):
        pageid = self._get_pageid()
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
        print(data,"data 2")
        summary = data["query"]["pages"][str(pageid)]["extract"]
        return summary

wikirequest = WikiRequest(48.85837009999999,2.2944813)

print(wikirequest.get_summary())