
from flask import Flask, render_template, request

app = Flask(__name__)
chat_log = []

@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.form["user_input"]
        chat_log.append({"role": "user", "text": user_input})

        response = genera_risposta(user_input)
        chat_log.append({"role": "bot", "text": response})

    return render_template("chatbot.html", chat_log=chat_log)

def genera_risposta(testo):
    testo = testo.lower()

    if "ciao" in testo or "buongiorno" in testo:
        return "👋 Benvenuto da SicuraPiù Assicurazioni! Come posso aiutarti oggi? Puoi chiedere info su auto, casa, vita, infortuni o viaggi."

    elif "auto" in testo:
        return "🚗 Offriamo assicurazioni RC Auto, furto e incendio, Kasko e assistenza stradale. Vuoi un preventivo?"

    elif "moto" in testo:
        return "🏍️ Proteggi la tua moto con RC base, furto, incendio e tutela conducente. Ti serve un preventivo?"

    elif "casa" in testo:
        return "🏡 Coperture per incendio, furto, responsabilità civile, eventi atmosferici. Vuoi sapere i prezzi?"

    elif "vita" in testo:
        return "❤️ Polizze vita per proteggere i tuoi cari: temporanee caso morte, mutuo o a capitale garantito."

    elif "infortuni" in testo:
        return "💼 Polizze infortuni 24/7, valide a lavoro, nel tempo libero e in viaggio. Vuoi info dettagliate?"

    elif "viaggi" in testo:
        return "✈️ Assicurazioni viaggio: spese mediche, bagagli, annullamento. Dove vuoi andare?"

    elif any(k in testo for k in ["grazie", "perfetto", "ottimo"]):
        return "🙏 Grazie a te! Se hai bisogno di altro, sono qui."

    elif any(k in testo for k in ["a presto", "arrivederci", "ci sentiamo"]):
        return "👋 A presto! SicuraPiù è sempre con te."

    else:
        return "🤖 Mi dispiace, non ho capito. Puoi chiedere info su auto, moto, casa, vita, infortuni o viaggi."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
