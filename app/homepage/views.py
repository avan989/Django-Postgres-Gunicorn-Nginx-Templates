from django.shortcuts import render
from rest_framework import viewsets
from .models import ApprenticeshipDevelop
from .serializers import DeveloperSerializer


# Create your views here.
def homepage(request):

    queryset = ApprenticeshipDevelop.objects.all()
    context = {'developer_list_all': queryset}
    return render(request, "apprenticeshipDeveloper.html", context)


# apprenticeDeveloper - viewsets handle post and get request
class DeveloperView(viewsets.ModelViewSet):

    # get all the data
    queryset = ApprenticeshipDevelop.objects.all()
    serializer_class = DeveloperSerializer
