from itertools import count
from math import prod
import os.path as path
import urllib.request
import json
import requests
import os

countryNameToId = {}
countryIdToName = {}
productNameToId = {}
productIdToName = {}

def main():
  csv = loadCSV(path.join(path.dirname(__file__), 'input.csv'))

  data = []
  
  outputFile = open(path.join(path.dirname(__file__), 'output.csv'), "w")
  for line in csv:
    countryName, productName = line.split(';')
    productId = getProductId(productName)
    countryId = getCountryId(countryName)

    if countryId == None or productId == None: 
      print("Skipping {}, {}.".format(countryName, productName))
      continue

    report = getReport(productId, countryId)
    if report == None:
      continue

    data = parseReport(report)
    for line in data:
      outputFile.write(";".join(line) + "\n")
      
  outputFile.close()


def loadCSV(path):
  """Load the input CSV file and return its content.

  Args:
      path (str): Input csv file path.

  Returns:
      str: Csv file content.
  """
  csv = None
  file = open(path)
  csv = file.readlines()
  return csv


def getProductId(productName, language="en"):
  """Retrieve the internal product id of the product.
  Endpoints (GET): 
    - https://www.mvorisicochecker.nl/de/api/products/{input}?hideFirstLevel=true
    - https://www.mvorisicochecker.nl/en/api/products/{input}?hideFirstLevel=true

  Args:
      productName (str): The name of the product (e.g. 'Edible products and preparations of food').
      language (str, optional): The language code ('en', 'de') (default: 'en').

  Returns:
      int: The interneal id of the product.
  """
  id = None
  productName = productName.replace("\n", "")

  if (productName in productNameToId):
    print("Found {} in cache.".format(productName))
    return productNameToId[productName]

  url = "https://www.mvorisicochecker.nl/{}/api/products/{}?hideFirstLevel=true".format(language, productName.replace(' ', '%20'))
  content = urllib.request.urlopen(url).read()
  contentJson = json.loads(content)
  products = contentJson["products"]
  if (len(products) > 0) :
    children = products[0]["children"]
    if "1" in children:
      firstChild = children["1"]
    else:
      if (len(children) > 0):
        firstChild = children[0]
      else:
        return None
    id = int(firstChild["id"])

    productNameToId[productName] = int(id)
    productIdToName[int(id)] = productName

    print("Found product ID {} for {}.".format(id, productName))
    return id

  return id


def getCountryId(countryName, language="en"):
  """Retrieve the internal country id of the product.
  Endpoints (GET): 
    - https://www.mvorisicochecker.nl/de/api/countries/{input}?hideFirstLevel=true
    - https://www.mvorisicochecker.nl/en/api/countries/{input}?hideFirstLevel=true

  Args:
      countryName (str): The name of the country (e.g. 'Taiwan').
      language (str, optional): The language code ('en', 'de') (default: 'en').

  Returns:
      int: The interneal id of the country.
  """
  id = None
  countryName = countryName.replace("\n", "")
  
  if (countryName in countryNameToId):
    print("Found {} in cache.".format(countryName))
    return countryNameToId[countryName]

  url = "https://www.mvorisicochecker.nl/{}/api/countries/{}?hideFirstLevel=true".format(language, countryName.replace(' ', '%20'))

  content = urllib.request.urlopen(url).read()
  contentJson = json.loads(content)

  countries = contentJson["countries"]
  if (len(countries) > 0) :
    firstCountry = countries[0]
    id = int(firstCountry["id"])

    countryNameToId[countryName] = int(id)
    countryIdToName[int(id)] = countryName

    print("Found country ID {} for {}.".format(id, countryName))
    return id

  return id


def getReport(productId, countryId, language="en"):
  """Retrieve report.
  Endpoints (POST):
    - https://www.mvorisicochecker.nl/de/ajax/generate-report
    - https://www.mvorisicochecker.nl/en/ajax/generate-report
  
  Payload (example):
    - product: 810
    - country: 307
    - language: en
    - report: 33

  Args:
      productId (int): The product id for this report.
      countryId (int): The country id for this report.
      language (str, optional): The language code for this report. Defaults to "en".

  Returns:
      str: Report returned by api.
  """
  report = None
  print("Retrieving report for {} ({}) and {} ({})...".format(productIdToName[productId], productId, countryIdToName[countryId], countryId), end="")
  url = "https://www.mvorisicochecker.nl/{}/ajax/generate-report".format(language)
  
  payload={'product': productId,
    'country': countryId,
    'language': language,
    'report': '33'}

  response = requests.request("POST", url, headers={}, data=payload, files=[])

  if response.status_code == 200:
    report = json.loads(response.text)
    print("OK")
  else: print("NOK")

  return report

def parseReport(report):
  """Parse the given report and extract needed information.

  Args:
      report (str): The report as a string (json).

  Returns:
      dict: Extracted information from report.
  """
  data = []
  
  for chapter, chapterContent in report["chapters"].items():
    for category, categoryContent in chapterContent.items():
      for riskBody in categoryContent["risks"]:
        risk = riskBody["body"]
        risk = risk.replace("<p>", "").replace("</p>", "").replace("\r\n", "").replace("\n", "")
        data.append([report["country"], report["product"], chapter, category, risk])
        # print(report["country"], report["product"], chapter, category, risk)

  return data


if __name__ == '__main__':
    main()
    