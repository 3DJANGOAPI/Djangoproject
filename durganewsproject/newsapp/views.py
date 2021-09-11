from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')
def moviesinfo(request):
    head_msg='Latest movies Information'
    msg1='Radhe movie is relese today'
    msg2='POTC is the best movie in the world'
    msg3='Johnny Deep is going to marry again'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
def sportsinfo(request):
    head_msg='Latest Sports Information'
    msg1='IPL cancel due to covid pandemic '
    msg2='India going to play football match in FIFA'
    msg3='Saina win the single chaimpionship'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
def politicsinfo(request):
    head_msg='Latest Politics Information'
    msg1='IPL cancel due to covid pandemic '
    msg2='India going to play football match in FIFA'
    msg3='Saina win the single chaimpionship'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
