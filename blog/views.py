# import plotly.plotly as py
# import plotly.graph_objs as go
import csv
import pdfkit
from django import template
from django.template.loader import get_template
from io import TextIOWrapper, StringIO
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import loader, Context
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def export_csv(request):
    memory_file = StringIO()
    writer = csv.writer(memory_file)
    for post in Post.objects.all():
        row = [post.pk, post.title, post.text]
        writer.writerow(row)
        response = HttpResponse( memory_file.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=db.csv'
        return response

# not work for iframe
def export_pdf(request):
    template = get_template("blog/pdf.html")
    #  context = Context({'data1':value1, 'data2':valu2})
    data = {'data': (
              ('<h2><a>irst row</a></h2>', 'Foo', 'Bar', 'Baz'),
              ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
          ) }
    html = template.render(data)
    options = {
          # 'page-size': 'Letter',
          # 'margin-top': '0.75in',
          # 'margin-right': '0.75in',
          # 'margin-bottom': '0.75in',
          # 'margin-left': '0.75in',
          'encoding': "UTF-8",
          'enable-javascript': 'true',
          'javascript-delay': '10000'
    }
    # pdf = pdfkit.from_string(html, False)
    pdf = pdfkit.from_url("https://plot.ly/~tallidea/7845.embed?showlink=false", False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response

# jquery.xeponline for good static image
def debug_pdf(request):
    template = get_template("blog/pdf.html")
    #  context = Context({'data1':value1, 'data2':valu2})
    data = {'data': (
              ('<a>First row</a>', 'Foo', 'Bar', 'Baz'),
              ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
          ) }
    html = template.render(data)

    # fig = py.get_figure('tallidea', '6312')
    # py.image.save_as(fig,'chris-plot.png')

    response = HttpResponse(html, content_type='text/html')
    return response

# def proxy_plot(request):
#     url = "https://plot.ly/~tallidea/6312.embed?showlink=false"
#     response = urllib.request.urlopen(url).read()
#     return response
