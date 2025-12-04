import gradio as gr
import pickle  # if you saved a trained model
import pandas as pd
import numpy as np

# --- Load your model/data from Kaggle notebook ---
# Example if you have a trained model saved as pickle:
try:
    with open("chatbot_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None  # fallback

# --- Define chatbot response function ---
def chatbot_response(message):
    """
    Takes user message and returns a response using your notebook logic
    """
    # Replace this with your notebook code
    if model:
        # Example if your model has predict method
        response = model.predict([message])[0]
    else:
        # fallback placeholder
        response = f"You said: {message}"
    return response

)

# --- Step 4: Launch the app ---
chatbot_interface.launch()
