import torch
from django.shortcuts import render
from transformers import BartTokenizer, BartForConditionalGeneration
import os

# Load model and tokenizer once at module load
MODEL_PATH = os.path.join(os.path.dirname(__file__), "chatmodel/best_model.pth")
MODEL_NAME = "facebook/bart-base"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

def generate_answer(question):
    inputs = tokenizer(question, return_tensors="pt", max_length=512, truncation=True).to(device)
    output = model.generate(**inputs, max_length=128)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def chatbot_view(request):
    answer = None
    question = ""

    if request.method == "POST":
        question = request.POST.get("question", "")
        if question:
            answer = generate_answer(question)

    return render(request, "t5_model.html", {"question": question, "answer": answer})
