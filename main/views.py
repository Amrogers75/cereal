from django.shortcuts import render, render_to_response
from main.models import Cereal, Manufacturer
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import CerealForm2
# Create your views here.


def detail_view(request, pk):
    cereal_object = Cereal.objects.get(pk=pk)

    context = {}

    context['cereal_object'] = cereal_object

    return render_to_response('detail_view.html', context, context_instance=RequestContext(request))


def list_view(request):
    cereal_objects = Cereal.objects.all()

    context = {}

    context['cereal_objects'] = cereal_objects

    return render_to_response('list_view.html', context, context_instance=RequestContext(request))


def create_view1(request):

    context = {}
    form = CerealForm()
    context['form'] = form

    if request.method == 'POST':
        form = CerealForm(request.POST, request.FILES)
        if form.is_valid():
            print form.is_valid()

            form.save()
            return HttpResponseRedirect('/list_view/')
        else:
            context['errors'] = form.errors
    return render_to_response('create_view1.html', context, context_instance=RequestContext(request))


def create_view2(request):

    context = {}

    form = CerealForm2()
    context['form'] = form

    if request.method == 'POST':
        form = CerealForm2(request.POST, request.FILES)

        if form.is_valid():

            print form.cleaned_data

            title = form.cleaned_data['title']
            info = form.cleaned_data['info']
            # image = form.cleaned_data['image']

            new_object = Cereal()

            new_object.title = title
            new_object.info = info
            # new_object.image = image

            new_object.save()

            return HttpResponseRedirect('/list_view/')
        else:
            context['errors'] = form.errors

    return render_to_response('create_view2.html', context, context_instance=RequestContext(request))


def update_view(request, pk):

    context = {}

    cereal_object = Cereal.objects.get(pk=pk)

    context['cereal_object'] = cereal_object

    form = CerealUpdateForm()

    context['form'] = form

    if request.method == 'POST':
        form = CerealUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            cereal_object.title = form.cleaned_data['title']
            cereal_object.info = form.cleaned_data['info']

            if form.cleaned_data['image'] != None:
                cereal_object.image = form.cleaned_data['image']

            cereal_object.save()

            return HttpResponseRedirect('/update_view/%s/' % pk)

        else:
            context['errors'] = form.errors

    return render_to_response('update_view.html', context, context_instance=RequestContext(request))


def delete_view(request, pk):

    Cereal.objects.get(pk=pk).delete()

    return HttpResponseRedirect('/list_view/')


def signup(request):

    context = {}

    form = UserSignUp()
    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            print form.cleaned_data

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = User.objects.create_user(name, email, password)
                context['valid'] = "Thank You For Signing Up!"

                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/list_view/')

            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    if request.method == 'GET':
        context['valid'] = "Please Sign Up!"

    return render_to_response('signup.html', context, context_instance=RequestContext(request))

