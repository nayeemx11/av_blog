from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comments, Replies
from .forms import PostForm, CommentForm, ReplyForm


def index(request):
    count = None
    if request.user.is_authenticated:
        count = User.objects.count()
    # return render(request, 'index.html', {"count": count})
    return post_list(request)


def post_list(request):
    post_list = Post.objects.all()
    post_form = PostForm()

    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')

    context = {
        "post_list": post_list,
        "post_form": post_form,
    }
    return render(request, "post_list.html", context)


def post_detail_view(request, id):
    post_detail = get_object_or_404(Post, id=id)
    comments = post_detail.comments_on.all()

    if request.method == "POST":
        if "parent_id" in request.POST:
            # Handle reply
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                parent_id = request.POST["parent_id"]
                if Comments.objects.filter(id=parent_id).exists():
                    reply.comment = get_object_or_404(Comments, id=parent_id)
                else:
                    reply.comment = None
                    reply.parent_reply = get_object_or_404(Replies, id=parent_id)

                reply.author = request.user
                reply.save()
                return HttpResponseRedirect(f"/post_detail_view/{post_detail.id}/")
        else:
            # Handle comment
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post_detail
                comment.author = request.user
                comment.save()
                return HttpResponseRedirect(f"/post_detail_view/{post_detail.id}/")
    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()

    context = {
        "post": post_detail,
        "comments": comments,
        "comment_form": comment_form,
        "reply_form": reply_form,
    }

    return render(request, "post_detail.html", context)
