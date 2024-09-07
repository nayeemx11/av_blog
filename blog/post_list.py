from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    
    """
    View to display a list of posts and handle post creation, including search functionality.

    Models:
    - Post: Represents a blog post. Used to retrieve and display all posts, as well as create new ones.

    Forms:
    - PostForm: A form tied to the Post model, allowing users to submit a new post.

    Process:
    1. Retrieves all posts from the database using `Post.objects.all()` and displays them in the post list.
    2. Displays a search box that allows users to filter posts by title via a case-insensitive search using the `icontains` lookup.
       If a search query is provided in the GET request (`?q=`), the post list is filtered by that query; otherwise, all posts are shown.
    3. Displays a `PostForm` for users to submit new posts. 
       - If the request method is GET, an empty form is passed to the template.
       - If the method is POST, the form is initialized with the submitted data and files (for handling media uploads).
    4. Upon valid form submission, a new post is created but not immediately saved to allow for associating the post with the current user.
    5. The post is saved to the database, and the user is redirected to the post list view, now updated with the new post.

    Context:
    - post_list: QuerySet of Post objects, filtered based on the search query if provided.
    - post_form: Instance of PostForm, either blank for GET requests or bound with POST data.

    Template:
    - post_list.html: Template used to display the post list and the form for creating a new post.

    Args:
    - request (HttpRequest): The incoming request object, containing GET or POST data.

    Returns:
    - HttpResponse: Rendered post list page, or a redirect back to the post list after successful form submission.
    """

    
    post_list = Post.objects.all()
    post_form = PostForm()
    
    query = request.GET.get('q')
    if query:
        # Search for posts whose title contains the query (case-insensitive)
        post_list = Post.objects.filter(Q(title__icontains=query))
    else:
        # If no query, show all posts
        post_list = Post.objects.all()

    if request.method == "POST":
         post_form = PostForm(request.POST, request.FILES)  # request.FILES uploads the files to form
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