import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from sample_app.models import *
# Create your views here.

def hello(request):
    print("hello world")
    return HttpResponse("ok")

def natural(request):
    for i in range(1, 11):
        print(i)
    return HttpResponse("printed")

def evenorodd(request):
    number = 2

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    return HttpResponse("ok")

def large2(request):
    a=2
    b=3
    if a>b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
    return HttpResponse("ok")


def login(request):
    return  render(request,"login.html")

def login_post(request):
    un=request.POST['textfield']
    pas=request.POST['textfield2']
    return HttpResponse("ok")

def register(request):
    return render(request,"register2.html")
def register_post(request):
    nam=request.POST['textfield']
    mail=request.POST['textfield2']
    pw=request.POST['textfield3']
    gender=request.POST['RadioGroup1']
    image=request.FILES['fileField']
    lang=request.POST.getlist('CheckboxGroup1')
    lng=','.join(lang)
    print(nam,mail,pw,gender,image,lang)
    date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    fs.save(r"C:\Users\asus\PycharmProjects\untitled2\sample_app\static\userphoto\\"+date+'.jpg',image)
    path="/static/userphoto/"+date+'.jpg'

    a=register1()
    a.name=nam
    a.mail=mail
    a.password=pw
    a.gender=gender
    a.image=path
    a.language=lng
    a.save()
    return HttpResponse("OK")

def notification(request):
    return render(request,"noti.html")
def notification_post(request):
    notifica=request.POST['textfield']
    date=datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    print(notifica,date)

    b=notifi()
    b.notification=notifica
    b.date=date
    b.save()
    return HttpResponse("ok")

def bookk(request):
    return render(request,"BOOK.html")
def bookk_post(request):
    bookname=request.POST['textfield']
    Author=request.POST['textfield2']
    price=request.POST['textfield3']
    publication=request.POST['textfield4']


    c=book()
    c.bookname = bookname
    c.Author = Author
    c.price = price
    c.publication = publication
    c.save()
    return HttpResponse("ok")


def view_user(request):
    res=register1.objects.all()
    return render(request,"view.html",{'data':res})

def veiw_noti(request):
    res=notifi.objects.all()
    return render(request,"VIEWNOTI.html",{'data':res})

def view_login(request):
    res=login.objects.all()
    return render(request,"login_view.html",{'data':res})

def view_book(request):
    res=book.objects.all()
    return render(request,"book_view.html",{'data':res})


def delete_book(request,bid):
    book.objects.filter(id=bid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_book"</script>')

def delete_noti(request,nid):
    notifi.objects.filter(id=nid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_noti"</script>')

def delete_user(request,uid):
    register1.objects.filter(id=uid).delete()
    return HttpResponse('<script>alert("deleted");window.location="/view_user"</script>')

def world(request):
    print(" world")
    return HttpResponse("ok")

def edit_book(request,id):
    data = book.objects.get(id=id)

    return render(request,"Edit_BOOK.html",{"data":data,"id":id})

def edit_book_post(request,id):
    bn=request.POST['textfield']
    au=request.POST['textfield2']
    pr=request.POST['textfield3']
    pb=request.POST['textfield4']
    book.objects.filter(id=id).update(bookname=bn,Author=au,price=pr,publication=pb)
    return HttpResponse('<script>alert("edited");window.location="/view_book"</script>')


def edit_notifi(request,id):
    data = notifi.objects.get(id=id)
    return render(request,"edit_noti.html",{"data":data,"id":id})
def edit_notifi_post(request,id):
    nt=request.POST['textfield']
    notifi.objects.filter(id=id).update(notification=nt)
    return HttpResponse('<script>alert("edited");window.location="/view_noti"</script>')


