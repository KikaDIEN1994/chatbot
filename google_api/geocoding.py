import googlemaps

class Geocoding:

    def __init__(self,keywords):
        # variable d'environement
        self.gmaps = googlemaps.Client(key='AIzaSyBdEpqf8TD9vorJAgaWauOG1oNnQmST5Ps')
        self.keywords = keywords

    def geocode(self): # ne pas mettre le meme noms de fonction que l'API ( ici mon geocode)
        geocode_result = self.gmaps.geocode(self.keywords) #(ici le geocode de google a savoir googlemaps.client.Client.geocode)
        result = {}
        print(geocode_result)
        print(self.gmaps)
        if geocode_result:
            first_address = geocode_result[0]
            result["status"] = "OK"
            result["location"] = first_address['geometry']['location']
            result["address"] = first_address['formatted_address']
            lat = result["location"]["lat"]
            lng = result["location"]["lng"]
            print(f"Latitude: {lat}, Longitude: {lng}")
        else:
            result["status"] = "NOK"
        print(result)
        return result
    
#keywords = "Tour Eiffel, Paris"
#geocoding = Geocoding(keywords)
