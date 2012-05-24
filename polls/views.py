# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.template import Context, loader
from DjangoPro.polls.models import Poll, Choice
import datetime
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from reportlab.pdfgen import canvas


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    '''t = loader.get_template('index.html')
    c = Context({
    'latest_poll_list': latest_poll_list,
    })'''
    return render_to_response('index.html', {'latest_poll_list':latest_poll_list})

def detail(request, poll_id):

    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'poll': p})

def results(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response("results.html", {'poll': p})


def votes(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('DjangoPro.polls.views.results',args=(p.id,)))

def display_meta(request):
    try:
        values = request.META.items()
    except RuntimeError:
        raise Http404
    return render_to_response("indexin.html", {'values': values})

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    print now
    return render_to_response('index.html', locals())

def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    image = canvas.ImageReader('C:/Documents and Settings/Syno-Frank/PycharmProjects/DjangoPro/643126.tif')


    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    p.drawImage(image, 0, 0)
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def hello_request(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return render_to_response('template_request.html',
            {'message': 'I came from ContentRequest.'}, context_instance=RequestContext(request))