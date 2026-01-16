import sys
import urllib.request

if len(sys.argv) < 2:
    print("Please provide a URL")
    sys.exit()

url = sys.argv[1]

try:
    response = urllib.request.urlopen(url)
    print("Website is working. Status code:", response.getcode())
except:
    print("Website is not reachable")