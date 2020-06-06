from django.shortcuts import render
from django.http import HttpResponse

#Dummy Data to mimic entries in a database to pass into the html.

posts = [
	{
	 'author': 'Aurenhardt',
	 'title': 'Entry 1',
	 'content': 'Description 1',
	 'date_posted': 'June 1, 2020'

	},
	{
         'author': 'Aurelius',
         'title': 'Entry 2',
         'content': 'Description 2',
         'date_posted': 'June 2, 2020'

        }
]


def home(request):
	context = { 
		'posts': posts 
	}

#Dictionary that contains a key 'posts' which is connected to the posts list at the beginning.
 
	return render(request,'overviewpage/overviewpage.html', context)

def about(request):
	return render(request,'overviewpage/about.html')
