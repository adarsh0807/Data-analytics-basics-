import requests
import speech_recognition as sr
import pyttsx3
import threading
import time

# ===============================
# CONFIGURATION
# ===============================

API_KEY = "YOUR_API_KEY_HERE"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
USER_NAME = "Adarsh"

# ===============================
# GLOBAL CONTROLS
# ===============================

stop_speaking_event = threading.Event()
tts_lock = threading.Lock()

# ===============================
# TEXT TO SPEECH (PRO LEVEL)
# ===============================

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts_worker(text):
    with tts_lock:
        stop_speaking_event.clear()

        for sentence in text.split("."):
            if stop_speaking_event.is_set():
                engine.stop()
                return

            engine.say(sentence.strip())
            engine.runAndWait()

        engine.stop()

def speak(text):
    print("Jarvis:", text)
    t = threading.Thread(target=tts_worker, args=(text,))
    t.daemon = True
    t.start()

# ===============================
# SPEECH TO TEXT (INTERRUPTS TTS)
# ===============================

recognizer = sr.Recognizer()

def listen():
    # 🔥 Interrupt Jarvis immediately
    stop_speaking_event.set()
    engine.stop()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Speech service error")
        return ""

# ===============================
# OPENROUTER AI
# ===============================

def get_ai_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Jarvis Pro Voice Assistant"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": f"You are Jarvis, a professional AI assistant. Speak concisely and clearly to {USER_NAME}."
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 200
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=data)
    result = response.json()

    return result["choices"][0]["message"]["content"]

# ===============================
# MAIN LOOP
# ===============================

speak(f"Hello {USER_NAME}. Jarvis is online. How can I help you?")

while True:
    user_text = listen()

    if not user_text:
        continue

    user_text_lower = user_text.lower()

    if user_text_lower in ["stop", "exit", "quit"]:
        speak(f"Goodbye {USER_NAME}. Have a nice day.")
        time.sleep(1)
        break

    reply = get_ai_response(user_text)
    speak(reply)
