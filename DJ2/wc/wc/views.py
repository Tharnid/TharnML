from django.http import HttpResponse
from django.shortcuts import render 
import operator

def homepage(request):
    # url request object
    # return HttpResponse('Hello, from Django!!!')
    return render(request, 'home.html')

# def oatmeal(request):
#     return HttpResponse('I love Oatmeal!!!')

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