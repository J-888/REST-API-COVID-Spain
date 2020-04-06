# REST API COVID Spain

> Simplest way to access the official Spanish COVID-19 data

[![License](https://img.shields.io/github/license/J-888/REST-API-COVID-Spain?color=blue&style=flat-square)](LICENSE)

## API endpoints

### Report [GET]

``` javascript
https://jmtg888.pythonanywhere.com/reports/{id}
```

Response example:
```json
{
    "id": 1186,
    "ca": "Madrid",
    "date": "2020-03-31",
    "cases": 27509,
    "deceases": 3603,
    "cured": 9330,
    "hospitalized": 15140,
    "uci": 1514,
    "accIncidence": 339,
    "diffCases": 3419
}
```

### Report List [GET]
Returns a list with all the reports
``` javascript
http://jmtg888.pythonanywhere.com/reports/
```
Link: http://jmtg888.pythonanywhere.com/reports/

#### Filter queries
Add this queries at the end of the url to filter the response (report list). They can be combined:

``` html
http://jmtg888.pythonanywhere.com/reports/?querty
http://jmtg888.pythonanywhere.com/reports/?querty1&query2&query3
```

| Query     | Description                 | Example              |
|-----------|-----------------------------|----------------------|
| ca        | Comunidad Autonoma (region) | ca=madrid            |
| date      | Exact date                  | date=2020-03-31      |
| startdate | After a date                | startdate=2020-03-31 |
| enddate   | Before a date               | enddate=2020-03-31   |
