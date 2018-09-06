class sign:
    def __init__(self, category, id, name, url):
        self.category = category
        self.id = id
        self.name = name
        self.url = url

    def write(self, txt_final):
        wtw = f"{self.category}, {self.id}, {self.name}, {self.url}"


txt_url = open("final_nurl.txt", "r")
