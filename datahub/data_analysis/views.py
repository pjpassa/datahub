from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, DeleteView
from data_analysis.models import Dataset, Project


class DatasetListView(ListView):
    model = Dataset


class DatasetDetailView(DetailView):
    model = Dataset


class DatasetDeleteView(DeleteView):
    model = Dataset


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectDelteView(DeleteView):
    model = Project

