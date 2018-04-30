from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me!!!'})
    # return HttpResponse('Hello, from Django!!!')

def about(request):
    return render(request, 'about.html')

# def eggs(request):
#     return HttpResponse('<h1>It is Eggs...how cool is that!!!</h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    # print(fulltext)

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else:
            # add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), "sortedwords": sortedwords } )
