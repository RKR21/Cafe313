from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from cafe.models import DailySpecial, MenuItem
from datetime import date


def HomePage(request):
    # HOW TO SEE TEMPLATES IN SAME FOLDER
    today = date.today()
    specials = DailySpecial.objects.all()
    items = MenuItem.objects.all()
    context = {}
    for special in specials:

        if (special.date.date() == today):
            context = {'special': special, 'date': today, 'items': items}
    if (len(context) == 0):
        context = {'special': 'None', 'date': 'None', 'items': items}

    return render(request, './index.html', context)


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(reverse('home'))
            return redirect('home')

    context = {'form': form}
    return render(request, './register.html', context)


class MyLoginView(LoginView):
    template_name = './login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
