from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import openai

# Create your views here.

openai_api_key = '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'
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.completions.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n=1,
        stop = None,
        temperature = 0.7,
    )
    print(response)
    # answer = response.choice[0].text.strip()

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
