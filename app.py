import gradio as gr
import nbformat
from nbconvert import PythonExporter
import types

# --- Step 1: Load the notebook ---
with open("kaggle.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

# Convert notebook to Python code
exporter = PythonExporter()
source, _ = exporter.from_notebook_node(nb)

# Create a new module to execute notebook code
notebook_module = types.ModuleType("notebook_module")
exec(source, notebook_module.__dict__)

# --- Step 2: Define chatbot function ---
def chatbot_response(message):
    """
    Calls a function defined in the notebook.
    Replace 'get_response' with the actual function name
    in your notebook that takes user input and returns output.
    """
    try:
        # Calls the notebook function dynamically
        response = notebook_module.get_response(message)
    except AttributeError:
        response = f"You said: {message} (no function found in notebook)"
    return response

# --- Step 3: Website description ---
description_html = """
<h1>Welcome to SentiShelter!</h1>
<p>This website showcases our SentiShelter technology from the Kaggle notebook.
Ask the chatbot anything related to the dataset or our analysis!</p>
<hr>
"""

# --- Step 4: Gradio UI ---
with gr.Blocks() as demo:
    gr.HTML(description_html)
    chatbot = gr.Chatbot()
    with gr.Row():
        msg = gr.Textbox(label="Your message")
        btn = gr.Button("Send")

    def respond(message, chat_history):
        reply = chatbot_response(message)
        chat_history.append((message, reply))
        return chat_history, ""

    btn.click(respond, [msg, chatbot], [chatbot, msg])
    msg.submit(respond, [msg, chatbot], [chatbot, msg])

demo.launch()

)

# --- Step 4: Launch the app ---
chatbot_interface.launch()
