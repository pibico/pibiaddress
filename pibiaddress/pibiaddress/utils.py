import requests
import frappe

@frappe.whitelist()
def get_geojson_from_address(address_line1=None, city=None, state=None, country=None, pincode=None):
  base_url = "https://nominatim.openstreetmap.org/search"
  headers = {
    "User-Agent": "pibiAddress/0.0.1"
  }
  params = {
    "format": "json",
    "limit": 1
  }

  # Add the address components to the parameters if they're provided
  if address_line1:
    params["street"] = address_line1
  if city:
    params["city"] = city
  if state:
    params["state"] = state
  if country:
    params["country"] = country
  if pincode:
    params["postalcode"] = pincode

  response = requests.get(base_url, headers=headers, params=params)
  
  if response.status_code == 200:
    data = response.json()
  
    if data:
      featureCollection = {
        "type":"FeatureCollection",
        "features":[
          {
            "type":"Feature",
            "properties":{},
            "geometry":{
              "type":"Point",
              "coordinates":[float(data[0]["lon"]), float(data[0]["lat"])]
            }
          }
        ]
      }
      
      return featureCollection
      
  else:
    frappe.log_error(f"Failed to fetch geolocation for address: {address}", "Nominatim API Error")
    return None