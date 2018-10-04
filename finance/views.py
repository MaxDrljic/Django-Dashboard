from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
# rest_framework imports are referring to djangorestframework
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company
from .as_dash import dispatcher


def company_article_list(request):
    return render(request, "finance/plotly.html", {})

# Chart API to integrate and display charts in /companies url


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        articles = dict()
        for company in Company.objects.all():
            if company.articles > 0:
                articles[company.name] = company.articles

        articles = sorted(articles.items(), key=lambda x: x[1])
        articles = dict(articles)

        # These two strings refer to the articleChart function on the front-end
        # Also, it is a Plotly function called after a successful AJAX request
        data = {
            "article_labels": articles.keys(),
            "article_data": articles.values()
        }

        return Response(data)


# Implementing Dash by Plotly
# Dash is a great solution for displaying stock dickers,
# metal and oil chart implementation, etc...

# **kwargs parameter enables to add as many parameters in function call as we want / need
def dash(request, **kwargs):
    return HttpResponse(dispatcher(request))

# This decorator marks a view as being exempt from the protection ensured by the middleware


@csrf_exempt
def dash_ajax(request):
    return HttpResponse(dispatcher(request), content_type='application/json')
