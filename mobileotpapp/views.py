from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
import requests
class Home(View):
    def get(self, request):
        return render(request, 'input.html')
class Mobileotp(View):
    def get(self, request):
        mobile="+91"+request.GET['t1']
        resp = requests.post('https://textbelt.com/text', {
            'phone': 'mobile',
            'message': 'otp',
            'key': '69f083f5036ad0e78a4e9f76dc7e33f12ab4dc7fzgSHA0Mi5wDej3zTfJs1tzU75',
        })
        print(resp.json())
        return HttpResponse('send otp successfully')
