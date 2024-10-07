import requests
from bs4 import BeautifulSoup

# List of URLs to check
urls = [
    "https://www.pacertboard.org/class/recovery-specialist-240",
    "https://www.pacertboard.org/class/recovery-specialist-241"
    "https://www.pacertboard.org/class/recovery-specialist-242"
    "https://www.pacertboard.org/class/recovery-specialist-243"
    "https://www.pacertboard.org/class/recovery-specialist-244"
    "https://www.pacertboard.org/class/recovery-specialist-245"
    "https://www.pacertboard.org/class/recovery-specialist-246"
    "https://www.pacertboard.org/class/recovery-specialist-247"
    "https://www.pacertboard.org/class/recovery-specialist-248"
    "https://www.pacertboard.org/class/recovery-specialist-249"
    "https://www.pacertboard.org/class/recovery-specialist-250"
    "https://www.pacertboard.org/class/recovery-specialist-251"
    "https://www.pacertboard.org/class/recovery-specialist-252"
    "https://www.pacertboard.org/class/recovery-specialist-253"
    "https://www.pacertboard.org/class/recovery-specialist-254"
    "https://www.pacertboard.org/class/recovery-specialist-255"
    "https://www.pacertboard.org/class/recovery-specialist-256"
    "https://www.pacertboard.org/class/recovery-specialist-257"
    "https://www.pacertboard.org/class/recovery-specialist-258"
    "https://www.pacertboard.org/class/recovery-specialist-259"
    "https://www.pacertboard.org/class/recovery-specialist-260"
    "https://www.pacertboard.org/class/recovery-specialist-261"
    "https://www.pacertboard.org/class/recovery-specialist-262"
    "https://www.pacertboard.org/class/recovery-specialist-263"
    "https://www.pacertboard.org/class/recovery-specialist-264"
    "https://www.pacertboard.org/class/recovery-specialist-265"
    "https://www.pacertboard.org/class/recovery-specialist-266"
    "https://www.pacertboard.org/class/recovery-specialist-267"
    "https://www.pacertboard.org/class/recovery-specialist-268"
    "https://www.pacertboard.org/class/recovery-specialist-269"
    "https://www.pacertboard.org/class/recovery-specialist-270"
    "https://www.pacertboard.org/class/recovery-specialist-271"
    "https://www.pacertboard.org/class/recovery-specialist-272"
    "https://www.pacertboard.org/class/recovery-specialist-273"
    "https://www.pacertboard.org/class/recovery-specialist-274"
    "https://www.pacertboard.org/class/recovery-specialist-275"
    "https://www.pacertboard.org/class/recovery-specialist-276"
    "https://www.pacertboard.org/class/recovery-specialist-277"
    "https://www.pacertboard.org/class/recovery-specialist-278"
    "https://www.pacertboard.org/class/recovery-specialist-279"
    "https://www.pacertboard.org/class/recovery-specialist-280"
    "https://www.pacertboard.org/class/recovery-specialist-281"
    "https://www.pacertboard.org/class/recovery-specialist-282"
    "https://www.pacertboard.org/class/recovery-specialist-283"
    "https://www.pacertboard.org/class/recovery-specialist-284"
    "https://www.pacertboard.org/class/recovery-specialist-285"
    "https://www.pacertboard.org/class/recovery-specialist-286"
    "https://www.pacertboard.org/class/recovery-specialist-287"
    "https://www.pacertboard.org/class/recovery-specialist-288"
    "https://www.pacertboard.org/class/recovery-specialist-289"
    "https://www.pacertboard.org/class/recovery-specialist-290"
    "https://www.pacertboard.org/class/recovery-specialist-291"
    "https://www.pacertboard.org/class/recovery-specialist-292"
    "https://www.pacertboard.org/class/recovery-specialist-293"
    "https://www.pacertboard.org/class/recovery-specialist-294"
    "https://www.pacertboard.org/class/recovery-specialist-295"
    "https://www.pacertboard.org/class/recovery-specialist-296"
    "https://www.pacertboard.org/class/recovery-specialist-297"
    "https://www.pacertboard.org/class/recovery-specialist-298"
    "https://www.pacertboard.org/class/recovery-specialist-299"
    "https://www.pacertboard.org/class/recovery-specialist-300"
    "https://www.pacertboard.org/class/recovery-specialist-301"
    "https://www.pacertboard.org/class/recovery-specialist-302"
    "https://www.pacertboard.org/class/recovery-specialist-303"
    "https://www.pacertboard.org/class/recovery-specialist-304"
    "https://www.pacertboard.org/class/recovery-specialist-305"
    "https://www.pacertboard.org/class/recovery-specialist-306"
    "https://www.pacertboard.org/class/recovery-specialist-307"
    "https://www.pacertboard.org/class/recovery-specialist-308"
    "https://www.pacertboard.org/class/recovery-specialist-309"
    "https://www.pacertboard.org/class/recovery-specialist-310"
    "https://www.pacertboard.org/class/recovery-specialist-311"
    "https://www.pacertboard.org/class/recovery-specialist-312"
    "https://www.pacertboard.org/class/recovery-specialist-313"
    "https://www.pacertboard.org/class/recovery-specialist-314"
    "https://www.pacertboard.org/class/recovery-specialist-315"
    "https://www.pacertboard.org/class/recovery-specialist-316"
    "https://www.pacertboard.org/class/recovery-specialist-317"
    "https://www.pacertboard.org/class/recovery-specialist-318"
    "https://www.pacertboard.org/class/recovery-specialist-319"
    "https://www.pacertboard.org/class/recovery-specialist-320"
    "https://www.pacertboard.org/class/recovery-specialist-321"
    "https://www.pacertboard.org/class/recovery-specialist-322"
    "https://www.pacertboard.org/class/recovery-specialist-323"
    "https://www.pacertboard.org/class/recovery-specialist-324"
    "https://www.pacertboard.org/class/recovery-specialist-325"
    "https://www.pacertboard.org/class/recovery-specialist-326"
    "https://www.pacertboard.org/class/recovery-specialist-327"
    "https://www.pacertboard.org/class/recovery-specialist-328"
    "https://www.pacertboard.org/class/recovery-specialist-329"
    "https://www.pacertboard.org/class/recovery-specialist-330"
    "https://www.pacertboard.org/class/recovery-specialist-331"
    "https://www.pacertboard.org/class/recovery-specialist-332"
    "https://www.pacertboard.org/class/recovery-specialist-333"
    "https://www.pacertboard.org/class/recovery-specialist-334"
    "https://www.pacertboard.org/class/recovery-specialist-335"
    "https://www.pacertboard.org/class/recovery-specialist-336"
    "https://www.pacertboard.org/class/recovery-specialist-337"
    "https://www.pacertboard.org/class/recovery-specialist-338"
    "https://www.pacertboard.org/class/recovery-specialist-339"
    "https://www.pacertboard.org/class/recovery-specialist-340"
]

# List of counties to check
counties = ["Berks", "Bucks", "Chester", "Delaware", "Lancaster", "Montgomery", "Schuylkill"]

# Function to check if a class is in one of the specified counties
def check_counties(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    page_text = soup.get_text()
    for county in counties:
        if county in page_text:
            return county
    return None

# Iterate through the URLs and print those that mention the specified counties
for url in urls:
    county = check_counties(url)
    if county:
        print(f"Class found in {county} County: {url}")
