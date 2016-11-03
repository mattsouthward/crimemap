class MockDBHelper:
    def connect(self, database="crimemap"):
        pass

    def get_all_inputs(self):
        return []

    def add_input(self):
        pass

    def clear_all(self):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        pass

    def get_all_crimes(self):
        return [{
            'latitude': 33.921959,
            'longitude': -78.416977,
            'date': '2016-10-29',
            'category': 'mugging',
            'description': 'mock description.'
        }]
