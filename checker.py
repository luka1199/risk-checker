from bs4 import BeautifulSoup as bs
import os.path as path
import urllib.request
import json
import requests

def main():
  csv = loadCSV(path.join(path.dirname(__file__), 'input.csv'))
  for line in csv:
    countryName, productName = line.split(';')
    productId = getProductId(productName)
    countryId = getCountryId(countryName)

    report = getReport(countryId, productId)
    data = parseReport(report)

  saveReport(data, path.join(path.dirname(__file__), 'output.csv'))


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
  url = "https://www.mvorisicochecker.nl/{}/api/products/{}?hideFirstLevel=true".format(language, productName.replace(' ', '%20'))
  content = urllib.request.urlopen(url).read()
  contentJson = json.loads(content)
  products = contentJson["products"]
  if (len(products) > 0) :
    children = products[0]["children"]
    if (len(children) > 0):
      firstChild = children[0]
      id = int(firstChild["id"])
      print("found id", id)
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
  url = "https://www.mvorisicochecker.nl/{}/api/countries/{}?hideFirstLevel=true".format(language, countryName.replace(' ', '%20'))

  content = urllib.request.urlopen(url).read()
  contentJson = json.loads(content)

  countries = contentJson["countries"]
  if (len(countries) > 0) :
    firstCountry = countries[0]
    id = int(firstCountry["id"])
    print("found id", id)
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
  print("Retrieving report for product {} and country {}...".format(productId, countryId))
  url = "https://www.mvorisicochecker.nl/{}/ajax/generate-report".format(language)
  

  return report

def parseReport(report):
  """Parse the given report and extract needed information.

  Args:
      report (str): The report as a string (json).

  Returns:
      dict: Extracted information from report.
  """
  data = None
  # TODO: Implement
  return data


def saveReport(data, path):
  """Save given data as csv to given path.

  Args:
      data (dict): Data from report.
      path (str): Output file (csv) path.
  """
  # TODO: implement
  pass


if __name__ == '__main__':
    main()
    