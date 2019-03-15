from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Mortgage


def mortgage_home(request):
    context = {
        'mortgages' : Mortgage.objects.all()
    }
    return render(request, 'mortgage/mortgage-home.html', context)

class PostListView(ListView):
    model = Mortgage
    template_name = 'mortgage/mortgage-home.html'
    context_object_name = 'mortgages'
    ordering = ['-date_of_transaction']

class PostDetailView(DetailView):
    model = Mortgage
    template_name = 'mortgage/mortgage_detail.html'


class PostCreateMortgageView(LoginRequiredMixin, CreateView):
    model = Mortgage
    template_name = 'mortgage/mortgage_form.html'
    fields = ['name','address','item','weight','rate','principle','interest','amount']

    def for_valid(self, form):
        return super().form_valid(form)

class PostUpdateMortgageView(LoginRequiredMixin,  UpdateView):
    model = Mortgage
    template_name = 'mortgage/mortgage_form.html'
    fields = ['name','address','item','weight','rate','principle','interest','amount']

    def for_valid(self, form):
        return super().form_valid(form)

class PostDeleteMortgageView(LoginRequiredMixin, DeleteView):
    model = Mortgage
    template_name = 'mortgage/mortgage_confirm_delete.html'
    success_url = '/'

def about(request):
    return render(request, 'mortgage/about.html', {'title': 'Mortgage About'})
