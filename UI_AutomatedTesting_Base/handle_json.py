import json

class HandleJson:
    def load_json(self):
        with open('E:\Python_study\\UI_AutomatedTesting_Base\config\cookie.json') as fp:
            data = json.load(fp)
        return data

    def get_data(self):
        return self.load_json()

    def writh_data(self, data):
        with open('E:\Python_study\\UI_AutomatedTesting_Base\config\cookie.json', 'w') as fp:
            fp.write(json.dumps(data))

handle_json = HandleJson()

if __name__ == '__main__':
    handle_json.writh_data()