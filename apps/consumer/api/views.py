# views.py
from django.shortcuts import render, redirect
from .forms import URL_Shortner_Form
import requests
from urllib.parse import urlparse


def fetch_all_data(request):
    base_url = request.build_absolute_uri('/') 
    api_url = base_url + "app1_shortner/v1/create_list/short-url/?format=json"

    context = {'short_urls': []}

    if request.method == 'GET':
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()

                # Sort newest to oldest : higher 'id' means newer
                sorted_data = sorted(data, key=lambda x: x.get('id', 0), reverse=True)
                context['short_urls'] = sorted_data[:8] # Get only first 8
            else:
                print("Failed to fetch short URLs:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("API Request failed:", e)

    return render(request, 'consumer/consumer.html', context)




def preprocess_redirect(request, short_url):
    
    # Example short_url = "http://127.0.0.1:8000/r/1gx"
    parsed_url = urlparse(short_url)
    
    # last part access
    short_code = parsed_url.path.strip("/").split("/")[-1]
    print(short_code)

    # final url to redirect 
    base_url = request.build_absolute_uri('/') 
    api_url = f"{base_url}app1_shortner/v1/redirect/{short_code}/"

    return redirect(api_url)




def post_long_url(request):
    base_url = request.build_absolute_uri('/') 
    api_url = base_url + "app1_shortner/v1/create_list/short-url/"
    
    if request.method == 'POST':
        form = URL_Shortner_Form(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            if long_url:
                try:
                    requests.post(api_url, data={"long_url": long_url})
                except requests.exceptions.RequestException as e:
                    print("API Request failed:", e)

    return redirect('fetch_all_data')



def delete_url(request, id):
    base_url = request.build_absolute_uri('/')  # e.g., http://127.0.0.1:8000/
    api_url = f"{base_url}app1_shortner/v1/delete/{id}/"

    if request.method == 'POST':
        response = requests.delete(api_url)
        print("Response status:", response.status_code)

    return redirect('fetch_all_data')