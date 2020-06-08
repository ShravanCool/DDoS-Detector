from django.shortcuts import render
from .forms import TestForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from .models import Test
from .serializers import TestSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd



# Create your views here.
def index(request):
	return render(request, 'index.html')

def dataset(request):
	return render(request, 'dataset.html')

class TestView(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializers


# @api_view(["POST"])
def Test_detect(unit):
	try:
		mdl = joblib.load('/home/shravan/Projects/Software/DDoS/DDoS/detector/tree_model.pkl')
		mydata = unit
		# print(mydata)
		# print(list(mydata.values()))
		# unit = np.ndarray(list(mydata.values()))
		X = unit.iloc[:,1:].values.reshape(1,-1)
		y_pred = mdl.predict(X)
		newdf = pd.DataFrame(y_pred, columns=['Status'])
		# return JsonResponse('The status is {}'.format(newdf), safe=False)
		return newdf.values[0][0]
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def call_model(request):
	if request.method=='POST':
		form = TestForm(request.POST)
		if form.is_valid():
			myDict = (request.POST).dict()
			df = pd.DataFrame(myDict, index=[0])
			# print(Test_detect(df))
			print(df)
			answer = Test_detect(df)
			messages.success(request, 'Traffic belongs to {}'.format(answer))

	form = TestForm()

	return render(request, 'testing.html', {'form': form})



