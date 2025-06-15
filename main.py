from flask import Flask, render_template, request

app = Flask(__name__)
chat_log = []

@app.route("/", methods=["GET", "POST"])
def chatbot():
    global chat_log
    if request.method == "POST":
        user_input = request.form["user_input"]

        if user_input.strip().lower() == "reset":
            chat_log = []
        else:
            chat_log.append({"role": "user", "text": user_input})
            response = genera_risposta(user_input)
            chat_log.append({"role": "bot", "text": response})

    return render_template("chatbot.html", chat_log=chat_log)

def genera_risposta(testo):
    testo = testo.lower()

    if "ciao" in testo or "buongiorno" in testo:
        return "👋 Benvenuto da SicuraPiù Assicurazioni! Come posso aiutarti oggi? Puoi chiedere info o preventivi su auto, moto, casa, vita, infortuni o viaggi."

    elif "auto" in testo:
        return "🚗 Ecco un preventivo per RC Auto + Furto: 480€/anno. Vuoi includere anche Kasko?"

    elif "moto" in testo:
        return "🏍️ Per la tua moto: RC + Furto a partire da 320€/anno. Ti interessa?"

    elif "casa" in testo:
        return "🏠 Assicurazione Casa (Incendio + Danni Acqua): 250€/anno. Vuoi maggiori dettagli?"

    elif "vita" in testo:
        return "❤️ Polizza vita base: 100.000€ di copertura per 280€/anno."

    elif "infortuni" in testo:
        return "🦴 Copertura infortuni con diaria + invalidità permanente: da 180€/anno."

    elif "viaggi" in testo:
        return "🌍 Assicurazione viaggio con spese mediche + annullamento: da 25€/settimana."

    elif "grazie" in testo or "a presto" in testo or "ci vediamo" in testo:
        return "🤖 Grazie a te! Rimango a disposizione per ogni dubbio o preventivo."

    else:
        return "🤖 Mi dispiace, non ho capito. Puoi chiedere info o preventivi su auto, moto, casa, vita, infortuni o viaggi. Scrivi ad esempio: 'preventivo auto'."

if __name__ == "__main__":
    app.run(debug=True)

