from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.utils import translation

from .forms import SubjectForm, TestForm
from Ponzo.models import Subject, IllusionCase, Answer

# Create your views here.
def index(request):
    return render(request, 'index.html')

'''
# modify a URL for multilingual support
def multilingual_url(request, url):
    if 'en' in request.LANGUAGE_CODE:
        lang_prefix = request.LANGUAGE_CODE[:2]
        url = '/' + lang_prefix + url
    return url
'''

def subject_registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
	    form.save()
            # testsuite = [case.id for case in IllusionCase.objects.filter(group=sub.id)]
            # request.session['testsuite'] = testsuite
            # return redirect(multilingual_url(request, '/ponzo/setup/'))
	    url = '/ponzo/setup/'
            return url

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubjectForm()
        # post_url = multilingual_url(request, "/ponzo/registration/")
	post_url = '/ponzo/registration'
        return render(request, 'registration.html', {'form': form, "post_url": post_url})


