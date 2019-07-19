# Bus Tracker (NextBus)

[![PyPI version](https://badge.fury.io/py/bustracker.svg)](https://badge.fury.io/py/bustracker)
[![Build Status](https://travis-ci.org/dalenguyen/bustracker.svg?branch=master)](https://travis-ci.org/dalenguyen/bustracker)

Python module to get bus data from [NextBus](http://webservices.nextbus.com/)

*This is an ongoing project. If you have any requests or contributions, please create a [ticket](https://github.com/dalenguyen/bustracker/issues)*

## Install

From PyPI with pip

```sh
pip install bustracker
```

## Usage examples

```python
from bustracker import BusTracker
# Agency list is from http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList
agency = 'ttc'
bus = BusTracker(agency)

# get prediction for bus stops
stops = [
    {'routeTag': 506, 'stopTag': 3292}
]

predictions = bus.get_prediction(stops)

print(predictions)
```

The result is a dictionary of predictions

```JSON
{
    "predictions": {
        "message": {
            "text": "TTC Information 416-393-4636 (INFO)",
            "priority": "Normal"
        },
        "agencyTitle": "Toronto Transit Commission",
        "routeTag": "506",
        "routeTitle": "506-Carlton",
        "direction": {
            "title": "West - 506 Carlton towards High Park",
            "prediction": [
                {
                    "isDeparture": "false",
                    "minutes": "2",
                    "seconds": "134",
                    "tripTag": "38216487",
                    "vehicle": "4189",
                    "block": "506_9_90",
                    "branch": "506",
                    "dirTag": "506_1_506",
                    "epochTime": "1563543576881"
                },
                ...
            ]
        },
        "stopTitle": "Gerrard St East At Jones Ave",
        "stopTag": "3292"
    },
    "copyright": "All data copyright Toronto Transit Commission 2019."
}
```

## For development

### Testing

```bash
pytest tests/test.py
```

## References

[NextBus Guide](http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf)
[Get Agency List](http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList)
