from django.shortcuts import render,redirect
import datetime
from kobita.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from kobita.models import ExtraInfo

def About(request):
    return render(request,'about.html')

def Users(request):
    data = ExtraInfo.objects.all().order_by('-id')
    return render(request,"users.html",{'data':data})

@login_required
def UserProfile(request,name):
        if request.method=="POST":
            bio = request.POST['bio']
            user =User.objects.get(username = name)
            relationship_status = request.POST['rltn_status']
            mobile = request.POST['mobile']
            gender = request.POST['gender']
            bio = request.POST['bio']
            obj = ExtraInfo(user=user,bio=bio,mobile=mobile,relationship_status=relationship_status,gender=gender)
            obj.save()
        return render(request,'profile.html')

@login_required
def view_page(request,slug):

    post = Post.objects.all().get(title=slug)
    comment = Comment.objects.all().filter(post_comment_id=post.id).order_by('-id')
    my_date = datetime.datetime.now()
   
    post.view += 1
    post.save()

    if request.method=='POST':
        comment_take = Comment(request.POST)

        name = request.POST['name']
        body = request.POST['body']
        date = datetime.datetime.now()
        post_id = request.POST['post_id']
        post_slug= request.POST['post_slug']

        object = Comment(name=name,body=body,post_comment_id=post_id,created_at=date)
        object.save()
        messages.success(request,"Comment Successfull")
        return redirect('/post/'+str(post_slug)+'/')
    else:
        comment_take = Comment()


    context ={
        'post':post,
        'comment':comment,
        'my_date': my_date
    }
    return render(request,'view.html',context)


def IP(request):
    get_ip = request.META.get("HTTP_X_FORWARDED_FOR")

    if get_ip is not None:
        ip = get_ip.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def mail_checker(request):

    x = request.split('@')[1]
    array = ['gmail.com', 'email.com', 'hotmail.com', 'yahoo.com', 'iubat.edu.bd']
    msg = False
    for i in range(0, len(array)):
        if x == array[i]:
            msg = True
            break
    return msg

def all_post(request):
    data = Post.objects.all().order_by('-id')
    return render(request,"all-post.html",{'data':data})

def home(request):
    myip = IP(request)
    data = Post.objects.all().order_by('-view')[:3]
    data2 = Post.objects.all().order_by('-id')[:100]
    if request.method=='POST':
        data3 = subscription(request.POST)
        mail = request.POST["email"]
        ip = request.POST["ip"]
        object = subscription(email=mail,ip=ip)
        already_has = subscription.objects.all().filter(email=mail).exists()
        if already_has:
            messages.warning(request,"Sorry, already subscribed")
        else:
            if mail_checker(mail):
                object.save()
                messages.success(request,"Subscription Done")
            else:
                messages.warning(request, "Invalid Mail")
            return redirect('Home')
    else:
        data3 = subscription()

    context = {
        'data':data,
        'data2':data2,
        'myip':myip
    }
    return render(request,'index.html',context)