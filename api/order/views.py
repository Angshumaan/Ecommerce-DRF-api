from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# TODO:
# We want to validate whether the user is signed in or not
# Also when user is succesfully signed in and authenticated and he has got something in the cart while making the payment after the payment he is gonna be redirected to the url  which is gonna be add order where he can have all this order being registerd in the admin itself


"""------Checking user is signup /authenticated or not  """
# We will grab request id and token


def validate_user_session(id, token):
    UserModel = get_user_model()
    print(UserModel)
    try:
        # We will grab user model id and token
        user = UserModel.objects.get(pk=id)
        # checking what we got from user model id and request id are equal or not
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False


# Simpply add all the details which user is bringing in  from the front  end and we have to just add that thing into the admin panel
    # in short
# When user hits the certain route we need to execute a method which is responsible for collecting all the data and pushing the data in the admin

@csrf_exempt
def add(request, id, token):
    # from validate_user_session function checking the user is signed up or not
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Please re-login', 'code': '1'})

    # checking what user is entering the value from front end
    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_pro = len(products.split(',')[:-1])
        print(total_pro)

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User does not exist '})
        # grabbing the order from model
        ordr = Order(user=user, product_names=products, total_products=total_pro,
                     transaction_id=transaction_id, total_amount=amount)
        ordr.save()
        return JsonResponse({'succes': True, 'error': False, 'msg': 'Order placed Successfully'})


class OrderViewset(viewsets.ModelViewSet):
    # ----2 steps we need---
    # 1)this is the query what data we need from the database that is model by getting all values
    # 2) And based on the serializer waht we have wrote like fields name etc hat data wiill be  coverted into json that is CategorySerializer class should be included in second step....go through docs Viewsts
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
