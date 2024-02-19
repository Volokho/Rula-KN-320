import numpy as np
print(f"Ура програма запустилася! Ми користуємося бібліотекою numpy {np.__version__}", np.arange(10))

import requests;

response = requests.get('https://httpbin.org/')
for line in response.iter_lines():
    print(line)

    import os
playload ={'name':os.environ.get("Env_Name"), 'cpu': os.environ.get("CPU")}
r = requests.get('https://httpbin.org/get', params= playload)
