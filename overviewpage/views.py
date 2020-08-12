from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Project

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
		'LINK1': 'LINKEDIN',
		'LINK2': 'INSTAGRAM',
		'LINK3': 'GITHUB',
		'LINK4': 'FIVERR',
	}
#Dictionary that contains a key 'posts' which is connected to the posts list at the beginning.
 
	return render(request,'overviewpage/homepage.html', context)

def gallery(request):
	context = {
                'posts': Post.objects.all(),
                'pageName': 'gallery',
                'pageTitle': 'MY ',
                'pageTitleHighlight': 'GALLERY',
                'pageTagline': 'A COLLECTION OF MY VARIOUS VISUAL WORKS',
                'pageBottomTitle': 'MY ',
                'pageBottomTitleHighlight': 'LINKS',
                'LINK1': 'LINKEDIN',
                'LINK2': 'INSTAGRAM',
                'LINK3': 'GITHUB',
                'LINK4': 'FIVERR',

	}

	return render(request,'overviewpage/gallery.html', context)

def about(request):
	context = {
		'pageName': "about",
		'pageTitle': 'ABOUT ',
		'pageTitleHighlight': 'ME',
		'pageTagline': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
		'pageBottomTitle': 'CONTACT ',
		'pageBottomTitleHighlight': 'ME',
		'LINK1': 'LINKEDIN',
		'LINK2': 'INSTAGRAM',
		'LINK3': 'GITHUB',
		'LINK4': 'FIVERR',
	}
	return render(request,'overviewpage/aboutpage.html', context)

def links(request):
	context = {
		'pageName': 'links',
		'pageTitle': 'IF YOU WOULD LIKE TO KNOW ',
		'pageTitleHighlight': 'MORE',
		'pageBottomTitle': 'IF YOU WOULD LIKE TO SEE ',
		'pageBottomTitleHighlight': 'MORE ',
		'LINK1': 'LINKEDIN',
		'LINK2': 'INSTAGRAM',
		'LINK3': 'GITHUB',
		'LINK4': 'FIVERR',
	}
	return render(request,'overviewpage/linkspage.html',context)

def projects(request):
        context = { 
		'projects': Project.objects.all(),
		'pageName': 'projects',
		'pageTitle': 'MY  ',
		'pageTitleHighlight': 'PROJECTS',
		'pageTagline': 'A COLLECTION OF ALL MAJOR CODING PROJECTS I HAVE DONE COMPLETE WITH DOCUMENTATION AND COMMENTARY',
		'pageBottomTitle': 'EXTERNAL ',
		'proj-desc':'DESC PASSED THROUGH VIEW',
		'pageBottomTitleHighlight': ' LINKS',
		'LINK1': 'DEMONSTRATION',
		'LINK2': 'DOCUMENTATION',
		'LINK3': 'GITHUB REPO  ',
		'LINK4': 'STORYBOARDS  ',
        }
        return render(request,'overviewpage/projectpage.html',context)


