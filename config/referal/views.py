from django.shortcuts import render, redirect
from .forms import AuthForm
    
def auth(request):
    if request.method == 'POST':
        complite_auth_form = AuthForm(request.POST)
        if complite_auth_form.is_valid():
            code = complite_auth_form.cleaned_data['invite_code']
            return redirect('profile/' + code)
    
    else:
        create_auth_from = AuthForm()
        context = {'form': create_auth_from}
        return render(request, 'auth.html', context)
