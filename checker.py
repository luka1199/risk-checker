from bs4 import BeautifulSoup as bs
import os.path as path

def main():
  csv = loadCSV(path.join(path.dirname(__file__), 'MVO-Liste.CSV'))
  # TODO: Iterate csv lines for countryName and productName
  # TODO: Set countryName and productName for each line of csv
  countryName = ""
  productName = ""
  countryId = getCountryId(countryName)
  productId = getProductId(productName)

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
  # TODO: Implement
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
  # TODO: Implement
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
  # TODO: Implement
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
  # TODO: Implement
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
    