from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def ana(request):
    djtext = request.POST.get('text','default')
    rpunc = request.POST.get('rpunc','off')
    fcaps = request.POST.get('fcaps','off')
    nlrem = request.POST.get('nlrem','off')
    esrem = request.POST.get('esrem','off')
    ccoun = request.POST.get('ccoun','off')
    
    if rpunc == 'on' or fcaps == 'on' or nlrem == 'on' or esrem == 'on' :

        if rpunc == 'on':
            analysed = ""
            puntkick='''?…!.,—––:;“‘[]{}()@#$%^&*'''
            for c in djtext:
                if c in puntkick:
                    pass
                else:
                    analysed  = analysed + c
            djtext = analysed*1
            params = {'purpose':'R punc', 'analysed_text': analysed}
    
        if fcaps == 'on':
            analysed = ""
            for c in djtext:
                analysed = analysed + c.upper()
            djtext = analysed*1
            params = {'purpose':'F caps', 'analysed_text': analysed}
    
        if nlrem =='on':
            analysed = ""
            for c in djtext:
                if c != '\n' and c !='\r':
                    analysed = analysed + c
            djtext = analysed*1
            params = {'purpose':'NL remover', 'analysed_text': analysed}
    
        if esrem =='on':
            l = len(djtext)-1
            c = 0 
            d = 1
            analysed = ""            
            while c<=l :
                if not(djtext[c] ==" " and djtext[c+1] ==" "):  
                    analysed = analysed + djtext[c] 
                c += 1
                d += 1
            djtext = analysed*1
            params = {'purpose':'ES remover', 'analysed_text': analysed}

    if (rpunc !="on" and nlrem!="on" and esrem!="on" and fcaps!="on"):
        params = {'purpose':'IDIOT IDIOT ARE YOU AN IDIOT','analysed_text':("plese give atleast one of the functions if you don't want to use then why did you come")}
        
  
    return render(request,'ana.html', params)


#    return HttpResponse("This was my first site with django. It was created on 5 November 2022")

