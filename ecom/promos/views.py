from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import PromoCode
from .forms import PromoCodeApplyForm


@require_POST
def promo_code_apply(request):
    now = timezone.now()
    form = PromoCodeApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            promo_code = PromoCode.objects.get(code__iexact=code,
                                               valid_from__lte=now,
                                               valid_to__gte=now,
                                               active=True)
            request.session['promo_code_id'] = promo_code.id
        except PromoCode.DoesNotExist:
            request.session['promo_code_id'] = None
    return redirect('cart:cart_detail')
