# encoding: utf-8
"""
get poems with uuid
"""

import json
import requests
import uuid

url = 'https://crl.ptopenlab.com:8800/poem/getpoems?seed=%s&type=3&uuid=%s' % ('千里心', uuid.uuid4())

res = requests.get(url)

poems = json.loads(res.text)
poem = poems['poems'][0]
for a in range(len(poem)):
    print(poem[a])
