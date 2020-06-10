from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#Dummy Data to mimic entries in a database to pass into the html.

def home(request):
	context = { 
		'posts': Post.objects.all(),
                'pageName': 'home',
		'pageTitle': 'CHRISTIAN ',
		'pageTitleHighlight': 'GOMEZ',
		'pageTagline': 'ILLUSTRATOR | WEB DESIGNER | DEVELOPER',
		'pageBottomTitle': 'MY ',
		'pageBottomTitleHighlight': 'LINKS',
		'LINK1': 'LINK1',
		'LINK2': 'LINK2',
		'LINK3': 'LINK3',
		'LINK4': 'LINK4',
		'galleryEnabled': "true"
		

	}

#Dictionary that contains a key 'posts' which is connected to the posts list at the beginning.
 
	return render(request,'overviewpage/overviewpage.html', context)



def about(request):
	context = {
		'pageName': "about",
		'pageTitle': 'ABOUT ',
		'pageTitleHighlight': 'ME',
		'pageTagline': ' ',
		'pageBottomTitle': 'CONTACT ',
		'pageBottomTitleHighlight': 'ME',
		'LINK1': 'LINK5',
		'LINK2': 'LINK6',
		'LINK3': 'LINK7',
		'LINK4': 'LINK8',
		'galleryEnabled': "false"

	}
	return render(request,'overviewpage/about.html', context)

def links(request):
	context = {
		'pageName': 'links',
		'pageTitle': 'IF YOU WOULD LIKE TO KNOW ',
		'pageTitleHighlight': 'MORE',
		'pageBottomTitle': 'CONTACT ',
		'pageBottomTitleHighlight': 'CONTACT ',
		'LINK1': 'LINK9',
		'LINK2': 'LINK1',
		'LINK3': 'LINK2',
		'LINK4': 'LINK3',
		'galleryEnabled': "false"
	}
	return render(request,'overviewpage/links.html',context)

