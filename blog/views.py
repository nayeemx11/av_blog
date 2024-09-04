from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post, Comments, Replies
from .forms import PostForm, CommentForm, ReplyForm
from .post_list import post_list


def index(request):
    """
    View function for the home page of the application.
    - Redirects to the `post_list` view, which displays a list of all blog posts and handles post creation.
    
    Improvement: in future index/home view for better way to display

    Redirect:
    - Always redirects to the `post_list` view, regardless of user authentication status.

    Args:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: Redirects to the `post_list` view, showing the list of posts.
    """
    return post_list(request)




def post_detail_view(request, id):
    
    """
    To handle the display and submission of comments and replies for a specific blog post.

    This view displays the details of a single blog post along with its associated comments and replies.
    It also handles form submissions for adding new comments or replies.

    Depending on the request method and form submission, the view performs the following actions:
    - If the request method is POST and a "parent_id" is present in the request, it processes a reply.
      - Validates the reply form.
      - Associates the reply with an existing comment or reply based on the provided "parent_id".
      - Saves the reply and redirects to the same post detail view.
    - If the request method is POST and no "parent_id" is present, it processes a new comment.
      - Validates the comment form.
      - Associates the comment with the current post and the logged-in user.
      - Saves the comment and redirects to the same post detail view.
    - If the request method is not POST, it initializes empty forms for comments and replies.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.
        id (int): The ID of the post whose details are to be displayed.

    Returns:
        HttpResponse: The rendered template for the post detail view with context including:
            - "post": The blog post object.
            - "comments": A queryset of comments associated with the post.
            - "comment_form": An instance of the CommentForm for adding new comments.
            - "reply_form": An instance of the ReplyForm for adding replies to comments.
    """
    
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
