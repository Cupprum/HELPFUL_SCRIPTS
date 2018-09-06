class sign:
    def __init__(self, category, id, name, url):
        self.category = category
        self.id = id
        self.name = name
        self.url = url

    def write(self, txt_final):
        wtw = f"{self.category}, {self.id}, {self.name}, {self.url}"


txt_url = open("final_url.txt", "r").readlines()
txt_nonurl = open("final_nonurl.txt", "r").readlines()

txt_w = open("final.txt", "w")

for x in range(len(txt_url)):
    p_first = txt_nonurl[x][:-1]
    p_second = txt_url[x]

    txt_w.write(f"{p_first}|{p_second}")
