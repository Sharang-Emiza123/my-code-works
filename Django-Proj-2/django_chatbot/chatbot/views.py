from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import openai

# Create your views here.

openai_api_key = ''
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.chat.completions.create(
        model = "gpt-4",
        temperature=0.7,
        messages = [
            {"role":"system", "content":"You are an helpful assistant."},
            {"role":"user", "content": message}
        ]
    )
    answer = response.choices[0].message.content.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
