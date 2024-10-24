from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import collections
from datetime import datetime
import pytz

class HomeView(View, LoginRequiredMixin):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return render(request, "home/dickb.html")
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        def to_chars(value):
            """Helper function to convert numbers to characters (or keep it as is)."""
            return chr(65 + (value % 26))  # A simple conversion: 0 -> A, 1 -> B, etc.
        
        colors = [
            '#fb8500', '#ffb703', '#ae2012', '#48cae4', '#0077b6', '#023e8a', '#03045e', '#f72585',
            '#b5179e', '#480ca8', '#0081a7', '#00afb9', '#7b2cbf', '#2b2d42', '#8d99ae', '#ef233c',
            '#5f0f40', '#ffd500', '#99582a', '#432818', '#9381ff', '#7371fc', '#9D34DA', '#DFE0E2',
            '#c9ada7', '#ddbdfc', '#662e9b', '#31263e', '#44355b', '#d62246', '#16697a', '#489fb5',
            '#6a994e', '#bc4749', '#0ead69', '#6f4518'
        ]

        number_of_colors = len(colors)
        number_of_days_per_year = 365

        # Current date
        tz = pytz.timezone('Asia/Nicosia')
        current = datetime.now(tz)
        day = current.day

        # Calculate index for color
        index = round((day * number_of_colors) / number_of_days_per_year)

        # Generate the code
        generated_code = (
            colors[index][:3] + 
            to_chars(current.hour) +
            to_chars(current.day) +
            to_chars(current.month)
        )

        context = collections.defaultdict()

        current_time = datetime.now()
        formatted_time = current_time.strftime("%A, %B %d, %Y")
        
        user = request.user

        context["user"] = user
        context["time"] = formatted_time
        context["current_date"] = current.strftime('%A, %B %d, %Y')
        context["color"] = colors[index]
        context["generated_code"] = generated_code

        return render(request, "home/home.html", context)