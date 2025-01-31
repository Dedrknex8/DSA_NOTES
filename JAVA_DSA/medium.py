import re

def replace_url(url):
    return re.sub(r"https://medium\.com", "https://readmedium.com", url)

# Example usage
url = "https://medium/whatever"
new_url = replace_url(url)
print(new_url)  # Output: https://readhello.com/whatever

