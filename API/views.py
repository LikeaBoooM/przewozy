from django.shortcuts import render, get_object_or_404, redirect
from django.http import request, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import PrzewozSerializer, KartaSerializer
from . models import Przewoz, Karta
from . forms import PrzewozForm, KartaForm
from django.forms import inlineformset_factory, modelformset_factory
# Create your views here.

def manageprzewozy(request):
    template_name = "API/przewoz_update.html"
    PrzewozyFormSet = modelformset_factory(Przewoz, fields='__all__')
    if request.method == "POST":
        formset = PrzewozyFormSet(request.POST)
        if formset.is_valid():
            formset.save()
        return HttpResponse("OK")
    else:
        formset = PrzewozyFormSet()
    context = {'formset': formset}
    return render(request, template_name, context)


def managekarty(request):
    cards = Karta.objects.all()
    KartyFormSet = modelformset_factory(Karta, form=KartaForm)
    template_name = 'API/karty_update.html'
    if request.method == 'POST':
        formset = KartyFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
        return redirect('karty-update')
    else:
        formset = KartyFormSet()
    context = {'formset': formset}
    return render(request, template_name, context)


class DeletePrzewoz(DeleteView):
    model = Przewoz
    template_name = 'API/przewoz_delete.html'
    success_url = '/view/przewozy/'


class KartyID(APIView):
    def get(self, request, id=None):
        card = get_object_or_404(Karta, pk=id)
        serializer = KartaSerializer(card)

        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id=None):
        card = get_object_or_404(Karta, pk=id)
        serializer = KartaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        card = get_object_or_404(Karta, pk=id)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Karty(APIView):
    def get(self, request):
        cards = Karta.objects.all()
        serializer = KartaSerializer(cards, many=True)

        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = KartaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PrzewozyDetailView(DetailView):
    model = Przewoz
    template_name = 'API/przewoz_detail.html'


class PrzewozyUpdateView(UpdateView):
    model = Przewoz
    fields = '__all__'
    template_name = 'API/przewoz_update.html'


class PrzewozyCreateView(CreateView):
    form_class = PrzewozForm
    template_name = 'API/przewoz_create.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('przewozy-view')


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

    def delete(self, request, id=None):
        przewozs = get_object_or_404(Przewoz, pk=id)
        przewozs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
