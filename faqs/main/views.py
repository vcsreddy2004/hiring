from django.shortcuts import redirect, render
from django.core.cache import cache
from main.forms import FAQForm
from .models import FAQ
def home(request):
    lang = request.GET.get('lang', 'en') 
    cache_key = f"faqs_home_{lang}"
    faqs = cache.get(cache_key)

    if faqs is None:
        faqs = FAQ.objects.all()
        translated_faqs = [faq.get_translation(lang) for faq in faqs]
        cache.set(cache_key, translated_faqs, timeout=300)
    else:
        translated_faqs = faqs
    return render(request, 'index.html', {'faqs': translated_faqs, 'selected_lang': lang})
def adminPage(request):
    lang = request.GET.get("lang", "en")
    faqs = FAQ.objects.all()
    translated_faqs = [faq.get_translation(lang) for faq in faqs]
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/admin-page?lang={lang}")
    else:
        form = FAQForm()
    return render(request, "admin-page.html", {"form": form, "faqs": translated_faqs, "selected_lang": lang})
