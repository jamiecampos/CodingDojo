from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    # 1. Last_name Rodriguez.
    users = models.Users.objects.filter(last_name='Rodriguez')

    # 2. Everyone except last_name Rodriguez.
    # users = models.Users.objects.exclude(last_name='Rodriguez')

    # 3. Last_name Rodriguez OR first_name Daniel.
    # users = models.Users.objects.filter(last_name='Rodriguez') | models.Users.objects.filter(first_name='Daniel')

    # 4. All last_name Rodriguezes except Madison.
    # users = models.Users.objects.filter(last_name='Rodriguez').exclude(first_name='Madison')

    # 5. Everyone except Daniel and Michael.
    # users = models.Users.objects.exclude(first_name='Daniel').exclude(first_name='Michael')

    # 6. Use .get() to have the first_name and last_name of user_id=1 print on index.html.
    # users = models.Users.objects.get(id=1)

    # 7. Use .get() to print users with last_name Rodriguez.
    # This errors out as "MultipleObjectsReturned at /"
    # users = models.Users.objects.get(last_name="Rodriguez")

    # 8. Use .get to have the first_name and last_name of user_id=1000 print on index.html.
    # This errors out as "DoesNotExist at /"
    # users = models.Users.objects.get(id=1000)

    # 9. Order users by first_name
    # users = models.Users.objects.all().order_by("first_name")

    #10. Order users by reverse last_name
    # users = models.Users.objects.all().order_by("-last_name")

    #11. Print all the Friendship objects in your terminal.
    # friendships = models.Friendships.objects.all()

    #12. Retrieve the Friendships where the User at id 4 is the user in the friendships table!
    # friendships = models.Friendships.objects.filter(user=4)

    # 13. Retrieve the Friendships where the User at id 4 is the friend.
    # friendships = models.Friendships.objects.filter(friend=4)

    # 14. Retrieve the Friendships where the user isnt user 4, 5, or 6.
    # friendships = models.Friendships.objects.exclude(friend=4).exclude(friend=5).exclude(friend=6)

    # comment out below line for get methods
    print users.query
    # comment out below line for users methods
    # print friendships.query
    # print users
    context = {
                'users':users,
                # 'friendships':friendships
    }
    return render(req, "friendapp/index.html",context)
