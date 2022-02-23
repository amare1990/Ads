from django.http import HttpResponse

def hello(request):
    print(request.COOKIES)
    #resp =  HttpResponse("Hello, world. b025330e is the hello index.")
    resp.set_cookie('dj4e_cookie', 'b025330e', max_age=1000)

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    #if num_visits > 4 : del(request.session['num_visits'])
    return HttpResponse('view count='+str(num_visits))

    #return resp
