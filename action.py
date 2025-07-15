import datetime
import speak
import webbrowser
import weather
import os
import pyjokes
import requests
import random
import time


def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn or "name" in data_btn:
      speak.speak("my name is Field Marshal Aasim Munir")  
      return "my name is Field Marshal Asim Munir"

    if "password" in   data_btn :
      speak.speak("Nice Try Diddy!")  
      return "Nice Try Diddy!"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 
    elif "you know about raza" in data_btn: 
        speak.speak("OH! Raza is my friend")  
        return "OH! Raza is my friend!"
    
    elif "khesham" in data_btn: 
        speak.speak("OH! khesham is my friend")  
        return "OH! khesham is my friend!"
    
   
    elif 'flip a coin' in data_btn or 'toss a coin' in data_btn:
        result = random.choice(['Heads', 'Tails'])
        speak.speak(f"It's {result}")
        return result
    
    elif 'motivate' in data_btn:
        quotes = [
            "Keep going — you're doing great!",
            "Success comes to those who keep trying.",
            "One step at a time. You've got this!"
        ]
        line = random.choice(quotes)
        speak.speak(line)
        return line
    
    elif 'tell me a story' in data_btn:
        story = "Once upon a time, a curious coder built a talking AI. One day, the AI became so clever it started telling stories. Just like this one!"
        speak.speak(story)
        return story
    
    elif 'tell me a fact' in data_btn or 'did you know' in data_btn:
        facts = [
            "Did you know? Honey never spoils — archaeologists found 3000-year-old honey that was still good.",
            "Did you know? Octopuses have three hearts.",
            "Did you know? A bolt of lightning contains enough energy to toast 100,000 slices of bread."
        ]
        fact = random.choice(facts)
        speak.speak(fact)
        return fact
    
    elif "sher ali" in data_btn: 
        speak.speak("OH! sher ali is my friend")  
        return "OH! sher ali is my friend!"
    
    elif 'time' in data_btn:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak.speak(f"The time is {current_time}")
        return f"The time is {current_time}"
    
    elif 'compliment' in data_btn:
        compliments = [
            "You're amazing!",
            "You have a great sense of humor!",
            "You're smarter than you think!",
            "You're doing great — keep going!",
            "Your energy is contagious!"
        ]
        line = random.choice(compliments)
        speak.speak(line)
        return line
    
    elif 'fortune' in data_btn or 'magic ball' in data_btn:
        fortunes = [
            "Yes, definitely!",
            "Ask again later.",
            "No, not today.",
            "Absolutely!",
            "Very doubtful."
        ]
        response = random.choice(fortunes)
        speak.speak(response)
        return response
    
    elif 'date' in data_btn:
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak.speak(f"Today's date is {current_date}")
        return f"Today's date is {current_date}"
    
    elif 'start timer' in data_btn:
        speak.speak("Timer started for 10 seconds.")
        time.sleep(10)
        speak.speak("Time's up!")
        return "Timer complete."
    
    elif 'quote' in data_btn or 'quote of the day' in data_btn:
        try:
            response = requests.get('https://zenquotes.io/api/today')
            if response.status_code == 200:
                quote_data = response.json()[0]
                quote = f"{quote_data['q']} — {quote_data['a']}"
                speak.speak(quote)
                return quote
            else:
                speak.speak("Sorry, I couldn't fetch a quote right now.")
                return "API error"
        except Exception as e:
            speak.speak("Something went wrong while fetching the quote.")
            return f"Error: {e}"
    
    elif "mustafa" in data_btn: 
        speak.speak("OH! mustafa is my friend. Meri jind meri jaan")  
        return "OH! mustafa is my friend! Meri jind meri jaan"
    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 
    elif 'joke' in data_btn or 'make me laugh' in data_btn:
        joke = pyjokes.get_joke()
        speak.speak(joke)
        return joke    
    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open('https://open.spotify.com/')   
        speak.speak("spotify.com is now ready for you, enjoy your music")                   
        return "spotify.com is now ready for you, enjoy your music"


    elif 'rock paper scissors' in data_btn:
        options = ["Rock", "Paper", "Scissors"]
        bot_choice = random.choice(options)
        speak.speak(f"I choose {bot_choice}")
        return f"I choose {bot_choice}"

    
    if "messi or ronaldo" in   data_btn :
      speak.speak("Offcourse messi.he is the greatest player of all time unlike that player who never won the worldcup")  
      return "Ofcourse Messi. He is the greatest player of all time unlike that player who never won the Worldcup"
  
    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    elif 'facebook' in data_btn or 'open facebook' in data_btn:
        url = 'https://facebook.com/'
        webbrowser.get().open(url)
        speak.speak("Facebook opened")
        return "Facebook opened"

    elif 'instagram' in data_btn or 'open instagram' in data_btn:
        url = 'https://instagram.com/'
        webbrowser.get().open(url)
        speak.speak("Instagram opened")
        return "Instagram opened"

    elif 'spotify' in data_btn or 'open spotify' in data_btn:
        url = 'https://open.spotify.com/'
        webbrowser.get().open(url)
        speak.speak("Spotify opened")
        return "Spotify opened"

    elif 'gmail' in data_btn or 'open gmail' in data_btn:
        url = 'https://mail.google.com/'
        webbrowser.get().open(url)
        speak.speak("Gmail opened")
        return "Gmail opened"

    elif 'twitter' in data_btn or 'open twitter' in data_btn or 'x' in data_btn:
        url = 'https://twitter.com/'
        webbrowser.get().open(url)
        speak.speak("Twitter opened")
        return "Twitter opened"

    elif 'linkedin' in data_btn or 'open linkedin' in data_btn:
        url = 'https://linkedin.com/'
        webbrowser.get().open(url)
        speak.speak("LinkedIn opened")
        return "LinkedIn opened"

    elif 'horizon ucp' in data_btn or 'open horizon ucp' in data_btn or 'ucp' in data_btn:
        url = 'https://horizon.ucp.edu.pk/web/login'
        webbrowser.get().open(url)
        speak.speak("horizon ucp opened")
        return "horizon ucp opened"

    elif 'reddit' in data_btn or 'open reddit' in data_btn:
        url = 'https://reddit.com/'
        webbrowser.get().open(url)
        speak.speak("Reddit opened")
        return "Reddit opened"
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'riddle' in data_btn:
        riddles = [
            "What has to be broken before you can use it? An egg.",
            "I’m tall when I’m young, and I’m short when I’m old. What am I? A candle.",
            "What gets wetter the more it dries? A towel."
        ]
        riddle = random.choice(riddles)
        speak.speak(riddle)
        return riddle

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    elif 'give me advice' in data_btn:
        tips = [
            "Start before you’re ready.",
            "Don't compare your beginning to someone else's middle.",
            "Drink more water, seriously!"
        ]
        tip = random.choice(tips)
        speak.speak(tip)
        return tip
   

    elif 'roll a dice' in data_btn:
        result = random.randint(1, 6)
        speak.speak(f"You rolled a {result}")
        return f"Dice roll: {result}"

    elif 'tell my fortune' in data_btn or 'fortune' in data_btn:
        fortunes = [
            "You will have a great day!",
            "A surprise is coming your way.",
            "Be careful with your decisions today.",
            "Something unexpected will make you smile."
        ]
        fortune = random.choice(fortunes)
        speak.speak(fortune)
        return fortune
    elif "mam"  in data_btn or "maam" in data_btn or "madiha" in data_btn:
           speak.speak("Mam Madiha is soo nice. She will give you full marks")
           return "Maam Madiha is soo nice. She will give you full marks"
        
    if "vigo" in   data_btn or "veego" in data_btn or "we go" in data_btn:
      speak.speak("Vigo Daala always on top")  
      return "Vigo Daala always on top"
  
    else :
        speak.speak( "i'm unable to understand!")
        return "i'm unable to understand!"       

