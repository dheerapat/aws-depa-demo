from fastapi import FastAPI
import gradio as gr
from chatbot import demo

CUSTOM_PATH = "/gradio"

app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "This is your main app"}

io = demo
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
