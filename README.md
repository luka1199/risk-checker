# risk-checker

## Installation
```
pip install -r requirements.txt
```

## Endpoints

### Produktnamen (GET)
- https://www.mvorisicochecker.nl/de/api/products/{input}?hideFirstLevel=true
- https://www.mvorisicochecker.nl/en/api/products/{input}?hideFirstLevel=true

### Ländernamen (GET)
- https://www.mvorisicochecker.nl/de/api/countries/{input}?hideFirstLevel=true
- https://www.mvorisicochecker.nl/en/api/countries/{input}?hideFirstLevel=true

### Form submit (POST) (not needed)
- https://www.mvorisicochecker.nl/de/ajax/submit-form
- https://www.mvorisicochecker.nl/en/ajax/submit-form

Payload: 
  - product: 810
  - country: 307
  - language: en
  - submissionToken: e8zgo5dOWWMjTjqeQpGa2mxZ3lSHYBrrEUInsGTJgSN
  - report: 33

### Ergebnisse (POST)
- https://www.mvorisicochecker.nl/de/ajax/generate-report
- https://www.mvorisicochecker.nl/en/ajax/generate-report

Payload: 
  - product: 810
  - country: 307
  - language: en
  - submissionId: e8zgo5dOWWMjTjqeQpGa2mxZ3lSHYBrrEUInsGTJgSN (not needed)
  - report: 33