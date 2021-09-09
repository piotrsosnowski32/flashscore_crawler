import telegram_send

def send_message(teams, score):
    if score[0] != "-":
        telegram_send.send(messages=[teams[0] + " " + score[0] + " " + " - " + score[1] + " " + teams[1]])
    else:
        telegram_send.send(messages=[teams[0] + " - " + teams[1]])

