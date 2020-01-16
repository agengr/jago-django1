from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BerandaView(TemplateView):
    template_name = 'beranda.html'

class TentangKamiView(TemplateView):
    template_name = 'tentangkami.html'
