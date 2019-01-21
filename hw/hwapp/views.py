from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'hwapp/home.html')

def about(request):
    return render(request, 'hwapp/about.html')

def count(request):
    global full_text
    full_text=request.GET['fulltext']
    word_list=full_text.split()
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] +=1
        else:
            word_dictionary[word]=1
    return render(request, 'hwapp/count.html', {'fulltext':full_text, 'total':len(word_list), 'dictionary':word_dictionary.items()})


def search(request):
    search=request.GET['search']
    Yn=['yes', 'no']
    if search in full_text:
        return render(request, 'hwapp/search.html', {'result':Yn[0]})
    else:
        return render(request, 'hwapp/search.html', {'result':Yn[1]})