from django.shortcuts import render
from django.views.generic import View



class PlayersHomeView(View):
    
    def get(self, request):
        return render(request, 'players\players.html')
    
    def post(self,request):
        pass