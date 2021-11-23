from django.shortcuts import render, get_object_or_404
from django.http import request, HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import PrzewozSerializer
from . models import Przewoz
from . forms import PrzewozForm
# Create your views here.


def przewozyUpdate(request):

    przewozys = get_object_or_404(Przewoz)
    template_name = "API/przewoz_update.html"
    form = PrzewozForm(instance=przewozys)
    if request.method == 'POST':
        form = PrzewozForm(request.POST, instance=przewozys)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
    context = {'przewozys': przewozys, 'form': form}
    return render(request,  template_name, context)


class PrzewozyDetailView(DetailView):
    model = Przewoz
    template_name = 'API/przewoz_detail.html'

class PrzewozyCreateView(CreateView):
    form_class = PrzewozForm
    template_name = 'API/przewoz_create.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PrzewozyView(ListView):
    model = Przewoz
    template_name = 'API/przewoz_list.html'


class PrzewozID(APIView):

    def get(self, request, id=None):
        przewoz = get_object_or_404(Przewoz, pk=id)
        serializerPrzewoz = PrzewozSerializer(przewoz)

        if id:
            return Response(serializerPrzewoz.data, status=status.HTTP_200_OK)
        return Response(serializerPrzewoz.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id=None):
        przewoz = get_object_or_404(Przewoz, pk=id)
        serializerPrzewoz = PrzewozSerializer(data=request.data)

        if serializerPrzewoz.is_valid():
            serializerPrzewoz.save()
            return Response(serializerPrzewoz.data, status=status.HTTP_200_OK)
        return Response(serializerPrzewoz.errors, status=status.HTTP_404_NOT_FOUND)


class Przewozy(APIView):

    def get(self, request):

        przewozy = Przewoz.objects.all()
        serializer = PrzewozSerializer(przewozy, many=True)

        if serializer :
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):

        serializer = PrzewozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
