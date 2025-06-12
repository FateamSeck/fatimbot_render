from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Utilisation d'Ollama local
OLLAMA_MODEL = "mistral"  # tu peux remplacer par phi3 si tu veux

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Appel au modèle local via Ollama
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {"role": "system", "content": "Tu es FatimBot : un assistant personnel bienveillant qui accompagne Fatim dans son quotidien."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response['message']['content']
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
