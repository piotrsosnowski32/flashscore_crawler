import telegram_send

def send_message(result):
    if result[2] != "-":
        telegram_send.send(messages=[result[0] + " " + result[2] + " : " + result[3] + " " + result[1]])
    #elif result[4] == "Koniec":
    #    telegram_send.send(messages=[f"Ostateczny wynik: {result[0]} {result[2]} : {result[3]} {result[1]}"])

def today_matches(teams):
    telegram_send.send(messages=[teams[0] + " - " + teams[1]])