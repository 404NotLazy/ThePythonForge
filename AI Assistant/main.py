import pyttsx3
import speech_recognition as sr
import os
import subprocess
import time
import psutil
import datetime
import webbrowser
import requests
from openai import OpenAI

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
            return None

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

def chat_with_openrouter(user_message):
    try:
        completion = client.chat.completions.create(
            extra_body={},
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are a super chill and supportive best friend (BSF) who loves to help with coding, life advice, and anything else with a friendly vibe.",
                },
                {"role": "user", "content": user_message},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        speak("Sorry, there was an error with the AI response.")
        print(f"Error: {e}")
        return None

def open_application(app_name):
    app_dict = {
        "calculator": "gnome-calculator",
        "chrome": "google-chrome-stable",
        "firefox": "firefox",
        "terminal": "gnome-terminal",
        "vlc": "vlc",
        "gedit": "gedit",
        "nautilus": "nautilus",
        "thunderbird": "thunderbird",
        "discord": "discord",
        "slack": "slack",
        "zoom": "zoom",
        "steam": "steam",
        "spotify": "spotify",
        "libreoffice": "libreoffice",
        "gedit": "gedit",
        "code": "code",
        "telegram": "telegram-desktop",
        "teams": "teams",
    }
    
    app = app_dict.get(app_name)
    if app:
        subprocess.run([app])
        speak(f"Opening {app_name}")
    else:
        speak(f"Sorry, I can't open {app_name} right now.")

def system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    battery_status = battery.percent if battery else "No battery data available"
    speak(f"CPU usage is {cpu}%, RAM usage is {memory}%, and battery is at {battery_status}%.")

def get_weather(city):
    api_key = "e46d6b1c945f2e9983f0735f8928ea2f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        description = weather["description"]
        temp = main["temp"] - 273.15
        speak(f"The temperature in {city} is {temp:.2f} degrees Celsius, with {description}.")
    else:
        speak(f"Sorry, I couldn't find weather information for {city}.")

def take_notes():
    speak("What would you like to note down?")
    note = listen()
    if note:
        with open("notes.txt", "a") as note_file:
            note_file.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note added successfully.")
    else:
        speak("Sorry, I didn't catch that note.")

def set_reminder():
    speak("What reminder would you like to set?")
    reminder_text = listen()
    speak("In how many minutes should I remind you?")
    reminder_time = listen()

    try:
        minutes = int(reminder_time)
        reminder_time_in_seconds = minutes * 60
        speak(f"Reminder set for {minutes} minutes from now.")
        time.sleep(reminder_time_in_seconds)
        speak(f"Reminder: {reminder_text}")
    except ValueError:
        speak("Sorry, I couldn't understand the time for the reminder.")

def web_search(query):
    query = query.replace("search", "")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching for {query} on Google.")

def chat():
    while True:
        speak("How can I assist you today?")
        command = listen()

        if command:
            if "open" in command:
                app_name = command.split("open")[-1].strip()
                open_application(app_name)
            elif "system" in command and "info" in command:
                system_info()
            elif "weather" in command:
                speak("Which city do you want the weather for?")
                city = listen()
                get_weather(city)
            elif "note" in command:
                take_notes()
            elif "reminder" in command:
                set_reminder()
            elif "search" in command:
                web_search(command)
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                response = chat_with_openrouter(command)
                if response:
                    speak(response)
                else:
                    speak("Sorry, I couldn't understand that.")

if __name__ == "__main__":
    speak("Hello! I am your assistant.")
    chat()