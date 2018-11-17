from django.contrib.auth import login
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from karajna.core.forms import SignUpForm
from karajna.core.tokens import account_activation_token
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.views.generic import ListView, CreateView, UpdateView ,DeleteView
from django.urls import reverse_lazy
from .models import Car, Version 
from .forms import CarForm 
from .filters import CarFilter
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse ,HttpResponseForbidden
from django.http import Http404
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, get_object_or_404






#@login_required
#def home(request):
#    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })

            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    
    return render(request, 'account_activation_sent.html')

def activate(request, uidb64, token):
    
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        
    
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):

        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def adsnumber(request):

    ads_number = Car.objects.all().filter(user=request.user.id).count()
    context = {'number': ads_number }
    return render(request, 'base.html , before_sell.html' ,context)

def carlist(request):

    car_data = Car.objects.all().filter(user=request.user.id)
    ads_number = Car.objects.all().filter(user=request.user.id).count()
    context = {'karaj': car_data , 'number': ads_number }
    return render(request, 'core/car_list.html' ,context)

@method_decorator(login_required , name='dispatch')
class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('carlist')
    #field=__all_
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('carlist')

class CarDelete(DeleteView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('carlist')

def load_versions(request):
    brand_id = request.GET.get('brand')
    versions = Version.objects.filter(brand_id=brand_id).order_by('name')
    return render(request, 'core/version_dropdown_list_options.html', {'versions': versions})



def has_group(request):
    group = Group.objects.get(name="dealer")
    users=group.user_set.all()
    return True if group in request.user.groups.all() else False

#def has_group(request):
#    return request.user.groups.filter(name="dealer").exists()
#User.objects.filter(groups__name='dealer')


def home(request):
    f = CarFilter(request.GET, queryset=Car.objects.all())
    return render(request, 'home.html', {'filter': f})

def cardata(request , pk ):
    one_car = Car.objects.get(id=pk)
    context = {'onecar': one_car }
    return render(request, 'core/one_car.html' ,context)

def car_delete(request , pk):
    one_car = get_object_or_404(Car ,id=pk)
    one_car.delete()
    context = {'delete': one_car }

    return render(request, 'core/car_list.html' ,context)

def before_sell(request):
    return render(request, 'before_sell.html')



