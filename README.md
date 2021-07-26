# Teqneia Task


## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install all packages.

```bash
pip3 install django
pip3 install djangorestframework
```

## To run server
```bash
python3 manage.py runserver
```
## urls
#### to get top 3 trending repositories
```
http://127.0.0.1:8000/repository/top-repositories
```
##### result example
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 386811486,
        "name": "YOLOX",
        "full_name": "Megvii-BaseDetection/YOLOX",
        "html_url": "https://github.com/Megvii-BaseDetection/YOLOX",
        "languages": {
            "Python": 7602825,
            "C++": 1770987
        }
    },
    {
        "id": 386876190,
        "name": "Laravel-Roadmap-Learning-Path",
        "full_name": "LaravelDaily/Laravel-Roadmap-Learning-Path",
        "html_url": "https://github.com/LaravelDaily/Laravel-Roadmap-Learning-Path",
        "languages": {}
    },
    {
        "id": 388693827,
        "name": "vitesse-webext",
        "full_name": "antfu/vitesse-webext",
        "html_url": "https://github.com/antfu/vitesse-webext",
        "languages": {
            "TypeScript": 2104093,
            "Vue": 617887,
            "HTML": 10614159,
            "CSS": 3359175
        }
    }
]
```
