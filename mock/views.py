#from .models import Dialogue
#from .forms import DialogueForm
import pdfkit
from django import template
from django.template.loader import get_template
from io import TextIOWrapper, StringIO
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

#def dialogue_detail(request, pk):
#    dialogue = get_object_or_404(Dialogue, pk=pk)
#    return render(request, 'dialogue/dialogue_detail.html', {'dialogue': dialogue})

#def dialogue_new(request):
    # if request.method == "POST":
    #     form = DialogueForm(request.POST)
    #     if form.is_valid():
    #         dialogue = form.save(commit=False)
    #         dialogue.author = request.user
    #         dialogue.save()
    #         return redirect(dialogue_detail, pk=dialogue.pk)
    # else:
    #     form = DialogueForm()
    #     return render(request, 'dialogue/dialogue_detail.html', {'dialogue': dialogue})
    #
def mock_main(request):
  return render(request, 'mock/mock_main.html',
                {'a_fig': [
                            ['Mentions', 7107],
                            # ['Positive Sentiment', 7101],
                            # ['Negative Sentiment', 7103],
                            # ['Average Ratings', 7099],
                            ['Trending Features', 7013],
                            ['Trending Words', 7059],

                            ['NETGEAR Nighthawk AC1750 Smart Dual Band WiFi Router (R6700)Trending Words', 0],
                            ['Average Star Rating', 6312],
                            ['Review Count (Rolling Sum)', 6282],
                            ['Low Star Review Count (Rolling Sum)', 6200],
                          ] } )

def export_pdf(request):
    template = get_template("mock/mock_main.html")
    data = {'a_fig': [
                            ['Mentions', 7107],
                            # ['Positive Sentiment', 7101],
                            # ['Negative Sentiment', 7103],
                            # ['Average Ratings', 7099],
                            ['Trending Features', 7013],
                            ['Trending Words', 7059],

                            ['NETGEAR Nighthawk AC1750 Smart Dual Band WiFi Router (R6700)Trending Words', 0],
                            ['Average Star Rating', 6312],
                            ['Review Count (Rolling Sum)', 6282],
                            ['Low Star Review Count (Rolling Sum)', 6200],
                          ]}

    html = template.render( data )
    options = {
          'encoding': "UTF-8",
          # 'enable-javascript': 'true',
          'load-error-handling': 'ignore'
          # 'javascript-delay': '10000'
    }
    pdf = pdfkit.from_string(html, False, options)
    # pdf = pdfkit.from_url("https://plot.ly/~tallidea/7845.embed?showlink=false", False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response

