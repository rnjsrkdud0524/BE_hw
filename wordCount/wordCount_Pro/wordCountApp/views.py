from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def hello(request):
    texts = request.GET['text']
    return render(request, 'hello.html', {'name':texts})

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

    characters = len(entered_text)
    withoutSpaces_characters = len(entered_text.replace(" ", ""))
    
    return render(request, "result.html", {'length': len(word_list), 'alltext': entered_text, 'dictionary': word_dictionary.items(), 'characters': characters, 'withoutSpaces_characters': withoutSpaces_characters})