API
===

```json
GET /api/commits

{"commits": [
  {"sha": "1824bbbff1341e253a891a804651b6338f8008e4", "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org", "seen": false},
  ...
]}


GET /api/commits?email=ohtsu@ohtsu.org
{"commits": [
  {"sha": "1824bbbff1341e253a891a804651b6338f8008e4", "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org", "seen": false},
  ...
]}


GET /api/commits?name=Shigeki Ohtsu
{"commits": [
  {"sha": "1824bbbff1341e253a891a804651b6338f8008e4", "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org", "seen": false},
  ...
]}


GET /api/commits/1824bbbff1341e253a891a804651b6338f8008e4

{"sha": "1824bbbff1341e253a891a804651b6338f8008e4", "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org", "seen": false}


PATCH /api/commits/1824bbbff1341e253a891a804651b6338f8008e4 {"seen": true}

{"sha": "1824bbbff1341e253a891a804651b6338f8008e4", "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org", "seen": true}
