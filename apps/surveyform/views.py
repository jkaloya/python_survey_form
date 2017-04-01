from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'surveyform/index.html')

def create(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/user')

def user(request):
    print "Go to show results!"
    print request.session
    return render(request, 'surveyform/user.html')
