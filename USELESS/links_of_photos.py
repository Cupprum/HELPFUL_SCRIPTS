txt = open("scraped_html.txt", "r")
final = open("final_html.txt", "w")

list_a = []
counter_rest = 0
last = ""

for y in txt:
    for x in y:
        if last + x == "id":
            counter_rest = 11

        if counter_rest != 0:
            counter_rest -= 1

        if counter_rest > 0 and counter_rest < 8:
            list_a.append(x)
            if counter_rest == 1:
                print(''.join(list_a))
                final.write(f"https://i.imgur.com/{''.join(list_a)}.png\n")
                list_a = []
        last = x
