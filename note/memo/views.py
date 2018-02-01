from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Memo

from django.forms import ModelForm

# Create your views here.


from django.http import HttpResponse
from pymongo import MongoClient

# db connection
# client = MongoClient()
client = MongoClient("mongodb://nkia:nkia123@ds113000.mlab.com:13000/ahn_test")
# client = MongoClient("localhost", 27017)
# client = MongoClient("mongodb://mongodb0.example.net:27017")

# database 얻어오기
# > db          현재 사용중인 db
# > show dbs    db 리스트 확인
# db = client.test      # local mongodb
db = client.ahn_test    # mLab mongodb

# 컬렉션 가져오기
coll = db.articles

# cursor = coll.find()
# for document in cursor:
#     print(document)
cursor = coll.find_one({"title": "Hello world"})
# print(cursor['title'])

# memo list 를 index로 설정
# def index(request):
#     return render(request, 'memo/index.html', {'cursor': cursor['title']})
#     # return HttpResponse(cursor['title'])#HttpResponse("Hello, world. You're at the memo index.")

def test(request):
    return render(request, 'memo/test.html', {'cursor': cursor['title']})

def postgres(request):
    data = Test.objects.filter(id=1)
    # print(data[0].id)
    return render(request, 'memo/postgres.html', {'data': data[0]})

# CRUD
class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['username', 'title', 'content', 'tags']

def memo_list(request, template_name='memo/memo_list.html'):
    memos = Memo.objects.all()
    data = {}
    data['object_list'] = memos
    return render(request, template_name, data)

def memo_create(request, template_name='memo/memo_form.html'):
    form = MemoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('memo_list')
    return render(request, template_name, {'form':form})

def memo_update(request, pk, template_name='memo/memo_form.html'):
    memo = get_object_or_404(Memo, pk=pk)
    form = MemoForm(request.POST or None, instance=memo)
    if form.is_valid():
        form.save()
        return redirect('memo_list')
    return render(request, template_name, {'form':form})

def memo_delete(request, pk, template_name='memo/memo_confirm_delete.html'):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method=='POST':
        memo.delete()
        return redirect('memo_list')
    return render(request, template_name, {'object':memo})
