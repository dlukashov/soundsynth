from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def home(request):
    """
    The synth home view.
    """
    context = RequestContext(request, {
        'foo': 'bar',
    })
    return render_to_response('home.html', context)
