import gradio as gr
import pandas as pd  # if your notebook uses it

# Example chatbot function
def chatbot_response(message):
    # TODO: Replace this with your Kaggle notebook logic
    return f"You said: {message}"

# Gradio UI
chatbot = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="SentiShelter Chatbot"
)

chatbot.launch()
