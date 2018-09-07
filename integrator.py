class SIGN:
    def __init__(self, category, s_id, name, url):
        self.category = category
        self.s_id = s_id
        self.name = name
        self.url = url

    @classmethod
    def write(cls, txt_final):
        something = txt_final
        return something


TXT_URL = open("final_url.txt", "r").readlines()
TXT_NONURL = open("final_nonurl.txt", "r").readlines()

TXT_W = open("final.txt", "w")

for x in enumerate(TXT_URL):
    p_first = TXT_NONURL[x][:-1]
    p_second = TXT_URL[x]

    TXT_W.write(f"{p_first}|{p_second}")
