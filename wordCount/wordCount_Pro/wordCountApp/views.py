from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
#index 함수가 요청되었을 때, index.html을 띄워주라는 의미

def wordCount(request):
    return render(request, "wordCount.html")

def result(request):
    return render(request, "result.html")

def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    return render(request, "result.html", {'length': len(word_dictionary), 'alltext': entered_text, 'dictionary': word_dictionary.items()})
