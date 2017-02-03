from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    # 1. Show all of the users and friends first and last names on your index.html page.
    friendships = models.Friendships.objects.all()

    # 2. Print all of the friends' first and last names associated with user__first_name = Michael on your index.html page.
    # friendships = models.Friendships.objects.filter(user__first_name='Michael')

    # 3. Print all of the friends' first names who Daniel is not friends with on your index.html page.
    # friendships = models.Friendships.objects.exclude(user__first_name='Daniel').exclude(friend__first_name='Daniel')

    # 4. Print all of the friends who are friends with both User with the id of 1 and with Users with the last name Hernandez.
    # friendships = models.Friendships.objects.filter(friend__id=1) | models.Friendships.objects.filter(friend__last_name="Hernandez")

    # 5. Order these by friend first_name and print them on your index.html page.
    # (Note the double output of Daniel Moore!). Try adding .distinct(), and make
    # sure to still print the query on your terminal. Which column is distinct?
    # friendships = models.Friendships.objects.filter(friend__id=1) | models.Friendships.objects.filter(friend__last_name="Hernandez").order_by("user__first_name")
    # PER DJANGO DOCUMENTATION Any fields used in an order_by() call are
    # included in the SQL SELECT columns. This can sometimes lead to unexpected
    # results when used in conjunction with distinct(). If you order by fields
    # from a related model, those fields will be added to the selected columns
    # and they may make otherwise duplicate rows appear to be distinct. Since
    # the extra columns dont appear in the returned results (they are only
    # there to support ordering), it sometimes looks like non-distinct results
    # are being returned.

    # 6. In your views.py, try the following query:
    # users = models.Users.objects.filter(usersfriend__friend__id=2)
    # print (users.query)
    # don't forget to pass users in to the context dictionary!
    # users = models.Users.objects.filter(usersfriend__friend__id=2)

    # 7. Check out the SQL query that the ORM builds! Related_name allows us to
    # go backward!!! Given this query, on your HTML page, try to print out the
    # first and last name of Users with the id 2. (Note: this is tricky, take it
    # once piece at a time!) When things get too tricky like this, it's probably
    # better to just add another DB query. e.g. number2 = models.Users.get(id=2)
    # and pass that to the context dictionary!
    # users = models.Users.objects.filter(usersfriend__friend__id=2)

    # 8. Now that we can use related names to filter, lets go back and try to
    # get #4 but start with the Users!
    # users = models.Users.objects.filter(usersfriend__friend__id=1) | models.Users.objects.filter(usersfriend__friend__last_name="Hernandez")


    # Use below line for questions 1-5
    print friendships.query
    # Use line below for questions 6-8
    # print users.query
    # print users
    context = {
                # ***Use 'friendships' below for questions 1-5***
                'friendships':friendships,
                # ***Use 'users' below for questions 6-8***
                # 'users':users,
                }
    return render(req, "friendapp/index.html",context)
