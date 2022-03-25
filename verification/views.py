from django.shortcuts import render, redirect
from accounts.decorators import unverified_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Verification
from .forms import verificationForm

# Verify Views Here


@login_required
@unverified_user
def verification_view(request):
    form = verificationForm()
    if request.method == 'POST':
        form = verificationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = Verification.objects.get(user=request.user)
            user_code = user.code
            verification_code = form.cleaned_data['code']

            if user_code == verification_code:
                Verification.objects.filter(user=request.user).update(
                    status=True,
                )
                messages.success(request, 'Account Verified')
                return redirect('settings')

            else:
                messages.success(request, 'Wrong verification code')
                form = verificationForm()
    context = {
        'form': form,
    }
    return render(request, 'verification/verify.html', context)
