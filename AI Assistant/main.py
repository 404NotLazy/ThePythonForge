import pyttsx3
import speech_recognition as sr
import os
import subprocess
import pygame
import time
import psutil
import datetime
import webbrowser
import requests
from openai import OpenAI

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Configure text-to-speech settings
def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for a voice command and returns it as a string"""
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

# DeepSeek API Client Setup
client = OpenAI(api_key="sk-ca64a4ee94c64fbe885ed7b33a946502", base_url="https://api.deepseek.com")

def chat_with_deepseek(user_message):
    """Send user message to DeepSeek API and return the response"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": user_message},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        speak("Sorry, there was an error with the AI response.")
        print(f"Error: {e}")
        return None

# App Launching Functionality
def open_application(app_name):
    """Opens specified applications on the computer"""
    app_dict = {
        "calculator": "gnome-calculator",
        "chrome": "google-chrome",
        "firefox": "firefox",
        "terminal": "mate-terminal",
        "vlc": "vlc"
    }
    app = app_dict.get(app_name)
    if app:
        subprocess.run([app])
        speak(f"Opening {app_name}")
    else:
        speak(f"Sorry, I can't open {app_name} right now.")

# Music Player Functionality
def play_music(music_file):
    """Play a specified music file"""
    if os.path.exists(music_file):
        pygame.mixer.init()
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        speak(f"Playing music: {music_file}")
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    else:
        speak("Sorry, I couldn't find that music file.")

def stop_music():
    """Stop the currently playing music"""
    pygame.mixer.music.stop()
    speak("Music stopped.")

def pause_music():
    """Pause the current music"""
    pygame.mixer.music.pause()
    speak("Music paused.")

def resume_music():
    """Resume the paused music"""
    pygame.mixer.music.unpause()
    speak("Resuming music.")

# System Information Retrieval
def system_info():
    """Get system information like CPU, RAM, and battery status"""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    battery_status = battery.percent if battery else "No battery data available"
    speak(f"CPU usage is {cpu}%, RAM usage is {memory}%, and battery is at {battery_status}%.")

# Weather Checker using an API
def get_weather(city):
    """Fetch the current weather of a city using OpenWeather API"""
    api_key = "e46d6b1c945f2e9983f0735f8928ea2f"  # Get your free API key from OpenWeather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        description = weather["description"]
        temp = main["temp"] - 273.15  # Convert Kelvin to Celsius
        speak(f"The temperature in {city} is {temp:.2f} degrees Celsius, with {description}.")
    else:
        speak(f"Sorry, I couldn't find weather information for {city}.")

# Note Taking Functionality
def take_notes():
    """Let the assistant take simple notes"""
    speak("What would you like to note down?")
    note = listen()
    if note:
        with open("notes.txt", "a") as note_file:
            note_file.write(f"{datetime.datetime.now()}: {note}\n")
        speak("Note added successfully.")
    else:
        speak("Sorry, I didn't catch that note.")

# Reminders Functionality
def set_reminder():
    """Set up a reminder for a specific time"""
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

# Web Search Functionality
def web_search(query):
    """Search the web using a browser"""
    query = query.replace("search", "")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching for {query} on Google.")

# Chat Functionality (with DeepSeek Integration)
def chat():
    """Main chat loop for voice commands"""
    while True:
        speak("How can I assist you today?")
        command = listen()
        
        if command:
            if "open" in command:
                app_name = command.split("open")[-1].strip()
                open_application(app_name)
            elif "play" in command and "music" in command:
                music_file = "path_to_your_music_file.mp3"  # Replace with your music file
                play_music(music_file)
            elif "stop" in command and "music" in command:
                stop_music()
            elif "pause" in command and "music" in command:
                pause_music()
            elif "resume" in command and "music" in command:
                resume_music()
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
                # Use DeepSeek for AI responses
                response = chat_with_deepseek(command)
                if response:
                    speak(response)
                else:
                    speak("Sorry, I couldn't understand that.")

# Main Program
if __name__ == "__main__":
    speak("Hello! I am your assistant.")
    chat()