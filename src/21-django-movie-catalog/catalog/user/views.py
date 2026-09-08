from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
# LEARNER NOTE: render() vs redirect()
# render(request, template) builds an HttpResponse by rendering a
# template and sends it back directly -- the browser's address bar
# doesn't change, and the URL stays whatever the user requested (e.g.
# GET /user/login/ shows the login form in place).
# redirect(name) instead sends back an HTTP redirect response, telling
# the browser "go make a brand-new request to this other URL". The
# argument here is a *URL name* (as defined by name= in urls.py, e.g.
# 'index' or 'login'), which Django resolves to an actual path -- this
# is the same name-based lookup {% url %} does in templates.
# Redirecting after a successful POST (rather than just render()-ing a
# result page) is a deliberate, common pattern called
# "Post/Redirect/Get": it stops the browser's back button or a page
# refresh from re-submitting the same form data a second time.

def login(request):
    # request.method tells you which HTTP verb this request used. Forms
    # in this project (see templates/user/login.html) use
    # method="POST", so the *first* time a visitor opens the login page
    # it's a GET request (falls to the `else` branch, just showing the
    # empty form); once they fill it in and click Submit, the browser
    # re-requests the same URL as a POST carrying the form data, and this
    # `if` branch runs instead.
    if request.method == 'POST':
        # request.POST is a dict-like object holding form data submitted
        # in the POST body. Each key here matches a form field's `name`
        # attribute in the HTML (<input name="username">, <input
        # name="password"> in login.html) -- Django doesn't parse form
        # fields by id or label, only by that `name` attribute.
        username = request.POST['username']
        password  = request.POST['password']

        # auth.authenticate() is django.contrib.auth's credential
        # checker: it looks up a User with this username, hashes the
        # supplied password the same way the stored one was hashed, and
        # compares them. It returns the matching User object if the
        # credentials are correct, or None if the username doesn't exist
        # or the password is wrong -- notice it does NOT log the user in
        # by itself; it only verifies who they claim to be.
        user = auth.authenticate(username= username, password = password)
        if user is not None:
            # auth.login() is the separate step that actually starts the
            # session: it stores the user's id in request.session (via
            # SessionMiddleware) so that on every subsequent request,
            # AuthenticationMiddleware can recognize them and populate
            # request.user automatically -- this is what makes
            # {% if user.is_authenticated %} in the navbar work.
            auth.login(request, user)
            # messages.add_message() queues a one-time notification with
            # a given "level" (here SUCCESS) and text. It's stored on the
            # session so it survives the redirect() below and is
            # rendered exactly once on the very next page, by
            # partials/_alert.html's {% for message in messages %} loop
            # -- after that render, it's gone.
            messages.add_message(request, messages.SUCCESS,'Logged in successfully.')
            return redirect('index')
        else:
            # Wrong credentials: queue an ERROR-level message (which,
            # per MESSAGE_TAGS in settings.py, renders with Bootstrap's
            # "alert-danger" styling) and send the visitor back to the
            # login form to try again.
            messages.add_message(request, messages.ERROR, 'Wrong username or password')
            return redirect('login')
    else:
        # Plain GET request: just show the empty login form, with no
        # context dict needed since the template has nothing dynamic to
        # display yet.
        return render(request, 'user/login.html')

# This view taught me how to use the messages framework to give the user
# feedback after a redirect instead of just rendering an error in place.
def register(request):
    if request.method == 'POST':

        # get form values
        # Same pattern as login() above: read each submitted field out
        # of request.POST by the `name` attribute used in
        # templates/user/register.html.
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        # Manual validation, checked in order, each with its own early
        # return via redirect() back to the same form:
        if password == repassword:
            # Username
            # User.objects.filter(username=username) returns a QuerySet
            # of every User row matching that username (zero or one,
            # since usernames are unique) without raising an error the
            # way .get() would if none matched; .exists() just asks the
            # database "is this QuerySet non-empty?" as an efficient
            # existence check, without fetching the actual rows.
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, 'This username is already taken.')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, 'This email is already taken.')
                    return redirect('register')
                else:
                    # everything checks out
                    # User.objects.create_user(...) is the recommended
                    # way to make a new account: unlike creating a User
                    # instance directly and setting a `password`
                    # attribute, create_user() runs the password through
                    # Django's hashing machinery before storing it, so
                    # the plain-text password submitted in the form is
                    # never itself saved to the database.
                    user = User.objects.create_user(username=username, password= password,email=email)
                    # create_user() already inserts the row into the
                    # database as part of creating it, so this extra
                    # .save() call re-saves the same (unchanged) object --
                    # harmless, just redundant.
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Your account has been created.')
                    return redirect('login')
        else:
            # Passwords didn't match -- note this only prints to the
            # server's console/terminal (visible to whoever's running
            # `manage.py runserver`), not to the visitor; the person
            # filling out the form only sees the page reload with an
            # empty form and no on-page explanation of what went wrong.
            print('passwords do not match')
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    # Like login(), this view only acts on POST -- see
    # templates/partials/_navbar.html, where the "Logout" link submits a
    # hidden form via JavaScript rather than being a plain GET link,
    # specifically so that logging out goes through this POST branch.
    if request.method == 'POST':
        # auth.logout() clears the current session's authentication
        # state (and rotates the session key), so request.user reverts
        # to Django's "anonymous user" on the next request.
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out.')
        return redirect('index')
