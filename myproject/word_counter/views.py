from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    sentence=str(request.POST.get("sentence")) # "안녕 안녕"
    sentence_to_list=sentence.split() # [ "안녕", "안녕"]

    dictionary={} # {word1:count1 , word2:count2 ,...}

    for word in sentence_to_list:
        if word in dictionary:
            dictionary[word] += 1
        else: 
            dictionary[word]=1
    
    word_count=list(dictionary.items())
    # [(안녕, 2)]



    return render(request, 'result.html', {'word_count': word_count})

