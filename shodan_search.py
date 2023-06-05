import shodan

class ShodanSearch:
    def __init__(self, api_key):
        self.api_key = "dWSLATqJ3YtwvUMR5BJA5pxGuYzN7t3e"

    def search(self):
        """
        Searches Shodan for potential targets using the provided API key.
        Returns a list of IP addresses.
        """
        targets = []

        try:
            api = shodan.Shodan(self.api_key)
            results = api.search("http.html:'papercut' http.html:'print'")
            targets = [result['ip_str'] for result in results['matches']]
        except shodan.APIError as e:
            print(f"Shodan search failed: {e}")

        return targets
