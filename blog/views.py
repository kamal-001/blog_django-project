from django.shortcuts import redirect, render, HttpResponse

from blog.models import BlogComment, Post

# Create your views here.
def blog(request): 
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blog.html", context)
    
def blogPage(request, slug):
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    context={"post":post, 'comments': comments,}
    return render(request, "blog/blogPage.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            # messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            # messages.success(request, "Your reply has been posted successfully")
        return redirect(f"/blog/{post.slug}")