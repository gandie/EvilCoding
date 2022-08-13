from selenium.webdriver import Firefox as request  # selenium offers way more features anyway
from re import findall as digest
from re import search as format
from random import choice as parse
exec = eval

entry_title = "https://github.com/gandie/EvilCoding"
print("This is my entry for round 2 of evil coding!")
print("The repo can be found here:", entry_title)
print("Enjoy!")

# Lets build a request object
request = request()
request.get(entry_title)

# Digest request response to get what we need for next step
main = request.page_source
mainc = "categories.{2,5} = '.*'"
formatted = digest(mainc, main)  # formats category!
formatted = formatted[1]
formatted = formatted[18:-1]  # We need this formatting here or it won't work

# next step is to view the
request.get(formatted)
jokes = digest(r'json\">\[\".*\"]', request.page_source)
jokes = jokes[0]
jokes = jokes[6:]
jokes = exec(jokes)
jokes_j = parse(jokes)

# We now reconstruct the object that executes the request
request.get(entry_title)
reconstructed = request.page_source
reconstructed = format("[^\d]\w\we_\wrl = '.*'", reconstructed).group()
reconstructed_formatted = format("ht\w\w.*om", reconstructed).group()

reconstructed = False
# Not loop over the list to get the res
while not reconstructed:
    request.get(f"{reconstructed_formatted}?{mainc[:7]}y={jokes_j}")
    foamrat = request.page_source
    foamratted = format(r"\"v\w\w\we\":.*\}", foamrat).group()
    reconstructed = eval(f"{{ {foamratted}")['value']
print("The joke or something, idk what string of letters might end up here:")
print(reconstructed)
