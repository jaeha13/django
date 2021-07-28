from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def exercise1(request):
    template = loader.get_template("exercise1.html")
    name = request.GET.get('name', '하재연')
    context = {'result': name}
    return HttpResponse(template.render(context, request))


def exercise2(request):
    type = request.GET.get('type')
    if not type:
        context = {'type': None, 'msg': "type = memberlist 또는 type = number 로 쿼리를 전달하세요"}
    else:
        context = {'type': type, 'memberlist': ['김영훈', '박민국', '하재연', '황규상'], 'number': len(['김영훈', '박민국', '하재연', '황규상'])}
    return render(request, 'exercise2.html', context)


def exercise3(request):
    if request.method == 'POST':
        name = request.POST['name']
        contents = request.POST['contents']
        context = {'name': name, 'contents': contents}
    else:
        context = None
    return render(request, 'exercise3.html', context)

