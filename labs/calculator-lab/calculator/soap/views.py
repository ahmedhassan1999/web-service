import re
from django.shortcuts import render
import requests
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup

# Create your views here.

def index(request):

    if request.method == "POST":
        url="http://www.dneonline.com/calculator.asmx"
        headers = {
            'content-type': 'text/xml; charset=utf-8',
            'SOAPAction': f'http://tempuri.org/{request.POST["proc"]}'
            }
        body = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <{request.POST["proc"]} xmlns="http://tempuri.org/">
                    <intA>{request.POST["num1"]}</intA>
                    <intB>{request.POST["num2"]}</intB>
                    </{request.POST["proc"]}>
                </soap:Body>
                </soap:Envelope>"""

        response = requests.post(url,data=body,headers=headers)
        res = BeautifulSoup(response.content, features="xml")

        result  = res.select(f'{request.POST["proc"]}Result')
        return render(request, 'index.html', {'data': result[0].contents[0]})

    return render(request, 'index.html')