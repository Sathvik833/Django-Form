from django.shortcuts import render,redirect

def index(request):
    return render(request,"index.html")
def results(request):
    print(request.POST)
    request.session['name_1']=request.POST['name']
    request.session['location']=request.POST['Dojo_location']
    request.session['langauge']=request.POST['language']
    request.session['comment']=request.POST['comments']
    return redirect('/view_results')
def view_results(request):
    return render(request,"index_2.html")   

    
