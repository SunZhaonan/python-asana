# This file is automatically generated by generate.py using api.json

class _Events:
    def __init__(self, client=None):
        self.client = client

    def get(self, params={}, **options):
        """Dispatches a GET request to /events of the API to get a set of recent changes to a resource."""
        options = self.client._merge_options({u'full_payload': True})
        return self.client.get('/events', params, **options)
