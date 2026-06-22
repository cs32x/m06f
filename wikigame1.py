### m06/wikigame1.py
import requests
import json

def main():
    print('Searching wikipedia for "The Cat in the Hat"')

    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'https'
    hostname = 'en.wikipedia.org'
    path = '/w/api.php'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'action': 'query',
             'list': 'search',
             'srsearch': 'The Cat in the Hat',
             'srlimit': 1,
             'format': 'json'
    }

    response = requests.get(url, params=query, headers={'user-agent':'cs32x educational demo'})

    # Read the response body in JSON format and print it
    j = response.json()
    print("response.json() =", json.dumps(j, indent=4))


if __name__ == '__main__':
    main()