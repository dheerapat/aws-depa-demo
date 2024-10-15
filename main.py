import gradio as gr
import random
import time

q1 = """
Thailand is a fantastic place to visit, offering beautiful beaches, exciting cities, a rich culture, and friendly people.
As a Bangkok Airways Assistance, I can help you plan your trip to world-famous destinations like Phuket or Chiang Mai.
Where would you like to go?
"""

q2 = """
Phuket is a great choice when traveling to Thailand, with exquisite beach like Pa Tong Beach that always fascinated people around the world.
Seafood that freshly caught out of the sea. I suggest this intersting spot
1. Pa Tong Beach
2. Karon Beach
3. Phuket Old Town
4. Rawai Seafood Market
5. Cape Phromthep
Also, Bangkok Airways offer daily flight from Bangkok to Phuket with great offer, do you want to know the detail of the flight?
"""

q3 = """
I want to access external tools to completed this task, do you want me to continue?
"""

q4 = """
Flight: PG273
Depart: Bangkok
Arrive: Phuket
Boarding Time: 12.30
Arriving Time: 13.55

Flight: PG277
Depart: Bangkok
Arrive: Phuket
Boarding Time: 16.50
Arriving Time: 17.30

Flight: PG279
Depart: Bangkok
Arrive: Phuket
Boarding Time: 19.30
Arriving Time: 20.45

If you want to book any of this flight just provide me with your full name, passport number, date and flight number of your choice.
"""

q5 = """
Please confirm your information before I continue the process
Name: John
Surname: Doe
Passport: US000100001
Flight: PG279 (19.30, BKK-HKT)
Date: 15-Oct-2024
"""

q6 = """
I want to access external tools to completed this task, do you want me to continue?
"""

q7 = """
Due to safety limitations, I cannot directly book your flight yet.
Please continue the process with this [link](https://click.ly/tools/fake-link-generator#).
I already predefined your information for you to continue.
"""

def get_prepared_questions():
    return [
        {"text": q1, "tool_use": False},
        {"text": q2, "tool_use": False},
        {"text": q3, "tool_use": True},
        {"text": q4, "tool_use": False},
        {"text": q5, "tool_use": False},
        {"text": q6, "tool_use": True},
        {"text": q7, "tool_use": False}
    ]

with gr.Blocks(title="✈️ Bangkok Airways's Travel Assistance | depa x AWS GenAI Hackathlon Demo") as demo:
    gr.Markdown("# ✈️ Bangkok Airways's Travel Assistance | depa x AWS GenAI Hackathlon Demo")
    gr.Markdown("If you want to play this demo again just hit F5 on your keyboard or refresh the browser.")
    gr.Markdown("The information provided in this demo is fictional and does not correspond to actual people or organizations. Any resemblance to real entities is purely coincidental.")
    gr.Markdown("""
        #### Use this sample question to test the demo
        ```
        I want to travel to Thailand
        Phuket
        Yes
        Yes
        My name is John Doe, passport number is US000100001 I want to book PG279 on 15 Oct
        Confirmed
        Yes
        Thank you
        ```
        """)

    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()

    questions = gr.State(get_prepared_questions)

    def respond(message, chat_history, questions):
        chat_history.append({"role": "user", "content": message})

        if len(questions) > 0:
            bot_message = questions.pop(0)
        else:
            bot_message = {"text": "End of the demo. Thank you for participating!", "tool_use": False}

        if bot_message["tool_use"]:
            chat_history.append({"role": "assistant", "content": bot_message["text"], "metadata": {"title": "🛠️ External Tools Required"}})
        else:
            chat_history.append({"role": "assistant", "content": bot_message["text"]})

        delay = random.uniform(2, 10)
        time.sleep(delay)

        return "", chat_history

    msg.submit(respond, [msg, chatbot, questions], [msg, chatbot])

demo.launch()
