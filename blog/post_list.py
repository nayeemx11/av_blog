from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    
    """
    View function to display a list of posts and handle the creation of new posts.

    Models Used:
    - Post: Represents a blog post. This model is used to retrieve and display all posts,
      as well as to create new posts when the form is submitted.

    Form Used:
    - PostForm: A form linked to the Post model. This form is used to handle user input
      for creating new posts. It includes fields for the post's title and body.

    Working Process:
    1. Retrieve all Post objects from the database using the Post model and display them in a list.
       This is done by querying the Post model with `Post.objects.all()` and storing the result in `post_list`.
       
    2. Initialize a PostForm instance to provide an empty form for creating new posts.
       If the request method is GET, the form will be blank. This form is passed to the template for rendering.
       
    3. If the form is submitted via a POST request, it is re-initialized with the data from the request.
       The form is then validated to ensure the data conforms to the model’s requirements.
       
    4. Upon successful validation, a new Post instance is created from the form data. However, the instance is not
       immediately saved to the database (`commit=False`) to allow for additional modifications—specifically, associating
       the post with the current user (`post.author = request.user`).
       
    5. The new post is saved to the database, and the user is redirected back to the post list view to see the updated list.
       
    6. The context dictionary, which includes `post_list` (the list of all posts) and `post_form` (the form for creating a new post),
       is passed to the `post_list.html` template for rendering.

    Context:
    - post_list: A queryset containing all Post objects to be displayed.
    - post_form: An instance of PostForm, either blank or bound with POST data.

    Template:
    - post_list.html: The template used to render the post list and the form.

    Args:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The rendered post list page with the form, or a redirect to the same page after form submission.
    """
    
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