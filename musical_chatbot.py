import sys
from pythonosc import udp_client
import openai
from pythonosc import udp_client
import time
import os

samples = [
    'bd_808',         
    'bd_haus',        
    'sn_dub',         
    'sn_zome',        
    'drum_cymbal_open',
    'drum_cymbal_closed',
    'drum_bass_hard',   
    'drum_snare_hard', 
    'elec_flip',      
    'elec_twang',     
    'elec_blip',     
    'elec_bloop',     
    'elec_plip',    
    'elec_blip2',    
    'elec_ping',       
    'elec_bell'  
]

api_key = "sk-proj-qtJpGSsbMo4aezh3yMdhT3BlbkFJlgQ8YDLST3mPchDb1o8X"
openai_api_client = openai.OpenAI(api_key=api_key)

# Sonic Pi OSC setup
sonic_pi_ip = "127.0.0.1"
sonic_pi_port = 4560
osc_client = udp_client.SimpleUDPClient(sonic_pi_ip, sonic_pi_port)
setup_instructions = """
Great! Let’s make some music. I'm going to guide you through how to set up your environment in Sonic Pi so you can start creating your own beats and melodies.

Here are the steps we'll follow:
1. Open Sonic Pi: Make sure Sonic Pi is running on your computer. You can download it from the Sonic Pi website if you haven't installed it yet.
2. Check your settings: Once Sonic Pi is open, go to the Preferences and ensure the OSC server is enabled. This will allow us to send commands from this script directly to Sonic Pi.
3. Prepare to receive commands: In the Sonic Pi interface, clear any existing code in the workspace so you have a fresh start.
4. Ready for input: Once everything is set up, we’ll start by sending some test commands to ensure everything is communicating properly.

Feel free to ask any questions as we go along. Let's make some awesome music together!
"""
mode_instructions = """
Great! Let's get started. There are three different modes to this session: Simple (1), Intermediate (2), and Hard (3). 
In the simple mode, I will help you to create a simple and fun melody to give you a taste of Sonic PI. 
In the intermediate mode, I will guide you in constructing your own unique melody through multiple choice options to create a complex and catchy tune. In the hard mode, you will be able to construct your own melody provided your own instructions. At this point, you are a Sonic Pi master! 
"""

send_sonic_pi_instructions = """
Now, copy paste this into you're Sonic Pi and run the program by clicking "run" on the top left corner:
```
data = sync "/osc*/play"
live_loop :osc_listener do
  use_real_time
  sample_name, sleep_time = data[0], data[1].to_f
  sample sample_name.to_sym, amp: 1
  sleep sleep_time
end
```
 Type 'yes' if you have copied this into your code block in Sonic Pi.
"""
intermediate_mode_info = """
will choose one each out of these categories. Once you choose all three, I will generate a fun and complex melody that you can then use for Sonic Pi!
"""

hard_mode_info = """
In hard mode, you have full autonomy over your Sonic Pi creation. Simply provide any instructions you want for your Sonic Pi melody. Based on your instructions, I will generate and refine Sonic Pi code to match your specifications!
"""

def main():
    print("Hi! I’m a musical chatbot for Sonic Pi! I’m here so you can create a fun, cool beat using my help.")
    while True: 
        response = input("Do you want to continue? Type 'yes' or 'no': ").strip().lower()
        if response == 'yes':
            print("Great! Let's get started.")
            run_instructions()
        elif response == 'no':
            print("Okay, feel free to return if you want to make some music later!")
            sys.exit()  
        else:
            print("Sorry, I didn't understand that. Please type 'yes' or 'no'.")
def get_openai_response(prompt):
    try:
        chat_completion = openai_api_client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        # Accessing using dot notation
        response_content = chat_completion.choices[0].message.content
        return response_content
    except Exception as e:
        print("An error occurred:", e)
        return None
def run_instructions():
    print(setup_instructions)
    while True:
        response = input("Do you still want to continue? Type 'yes' or 'no': ").strip().lower() 
        if response == 'yes':
            run_chatbot()
        elif response == 'no':
            print("Okay, feel free to return if you want to make some music later!")
            sys.exit() 
        else:
            print("Sorry, I didn't understand that. Please type 'yes' or 'no'.")
def run_chatbot():
    print("Great! Let’s make some music.")
    print(mode_instructions)
    while True:
        user_input = input("Now provide your choice of mode (1/2/3): ")
        if user_input == '1':
            print("Starting 'simple' mode...")
            time.sleep(1)
            start_simple_mode()
        elif user_input == '2':
            print("Starting 'intermediate' mode...")
            time.sleep(1)
            start_intermediate_mode()
        elif user_input == '3':
            print("Starting 'hard' mode...")
            time.sleep(1)
            start_hard_mode()
        else:
            print("I'm sorry I couldn't understand that. Please write the your mode correctly.")
def start_simple_mode():
    print("Choose a sample from these 16 choices:") 
    for index, sample in enumerate(samples):
        print(f"{index + 1}: {sample}")

    while True:
        sample_input = input("Indicate which sample you'd like to play by inputting the corresponding number: ")
        if sample_input.isdigit() and 1 <= int(sample_input) <= 16:
            break
        print("Please input a number between 1-16.")

    while True:
        sleep_input = input("Now input your number of sleep seconds (0.5 increments, max 5 seconds): ")
        try:
            sleep_val = float(sleep_input)
            if 0 < sleep_val <= 5:
                break
        except ValueError:
            pass
        print("Invalid input. Please follow the guidelines.")
    os.system(f"open -a Sonic\\ Pi ")
    if input(send_sonic_pi_instructions).lower() == 'yes':
        print("Great! Now we are sending this to Sonic Pi.")
        send_sample = samples[int(sample_input)-1]
        send_to_sonic_pi(send_sample, sleep_val)
        user_input = input("Do you want to try a different sample? Write 'yes' if you do. Type 'no' if not: ").lower()
        if user_input =='yes':
            print("Awesome! Make sure you stop your current sample so we can start a new session.")
            time.sleep(3)
            start_simple_mode()
        elif user_input == 'no':
            user_ask_questions()
            print("I hope you had a fun time in 'simple' mode. Feel free to return if you want to make some music later!")
            sys.exit()

def start_intermediate_mode():
    print(intermediate_mode_info)
    print("Here are five different genres: ")
    genre_instru_for_gpt = "Generate randomly five music genres. No explanation needed. "
    print(get_openai_response(genre_instru_for_gpt))
    genre_input  = input("Which genre do you choose? Write the name of the genre: ")
    print("Here are five different moods: ")
    mood_instru_for_gpt = "Generate randomly five moods. No explanation needed. "
    print(get_openai_response(mood_instru_for_gpt))
    mood_input  = input("Which mood do you choose? Write the name of the mood: ")
    print("Here are five different instruments: ")
    instrument_instru_for_gpt = "Generate randomly five simple instruments. No explanation or additional info needed. "
    print(get_openai_response(instrument_instru_for_gpt))
    instrument_input  = input("Which instruments do you choose? Write the name of the instruments: ")
    print("Now I'll generate the Sonic Pi melody...")
    generate_sonic_gpt = f"Generate a sonic pi melody using that represents this specific theme: {genre_input}, {mood_input}, {instrument_input}."
    response = get_openai_response(generate_sonic_gpt)
    print(response)
    print("Additionally, I'll now open Sonic Pi along with the file containing your Sonic Pi code. This was a great music session—I hope you enjoyed coding in Sonic Pi!")
    save_and_open_in_sonic_pi(response)
    user_ask_questions()

def start_hard_mode():
    print(hard_mode_info)
    user_instructions = input("Give me your instructions. One example might me 'recreate the song Billie Jean by Michael Jackson': ")
    print("Generating...")
    response = get_openai_response("Generate a Sonic Pi melody(using existing sonic pi features): " + user_instructions)
    print(response)
    save_and_open_in_sonic_pi(response)

    while True: 
        user_modifications = input("Would you like to modify/change your instruction more? Write 'yes'or 'no': ")
        if user_modifications == 'yes':
            user_more_instructions = input("What is your modification/instruction? ")
            print("Generating...")
            response = get_openai_response("modify this " + response + "with this instruction: " + user_more_instructions)
            print(response)
            save_and_open_in_sonic_pi(response)
        elif user_modifications == 'no':
            user_ask_questions()
        else:
            print("I'm not sure what you said. Please write the correct input value. ")
def save_and_open_in_sonic_pi(response, filename="sonic_pi_code.rb"):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, filename)
    with open(file_path, 'w') as file:
        file.write(response)
    print(f"File saved to: {file_path}")
    os.system(f"open -a Sonic\\ Pi ")
    os.system(f'open "{file_path}"')
def user_ask_questions():
        response = input("Do you have general questions about Sonic Pi? Answer 'yes' or 'no': ")
        if response.lower()=='yes':
            question = input("What's your question? ")
            print(get_openai_response(question))
            while True:
                response = input("Do you have any more questions? (yes/no): ")
                if response.lower() == 'yes':
                    user_input = input("What is your next question? ")
                    print(get_openai_response(user_input))
                elif response.lower() == 'no':
                    print("It was nice chatting with you. Feel free to return if you want to make some music later!")
                    sys.exit()
                else:
                    print("Sorry. What was that again? If you want to exit, type 'no'.")
        elif response.lower()=='no':
                    print("It was nice chatting with you. Feel free to return if you want to make some music later!")
                    sys.exit()

def send_to_sonic_pi(sample_name, sleep_time):
    osc_client.send_message("/play", [sample_name, sleep_time])
if __name__ == "__main__":
    main()
