from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree

# Create your views here.

# Create your views here.
# First step) Importing from braintree
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="cvcstvt95d342m3q",
        public_key="6t573tht8h5hx8dq",
        private_key="7739677869875ddc8c5d2f7ad9199052"
    )
)


# 2)checking whether user is logged in or not

def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


# tep1) from braintree Your front-end requests a client token from your server and initializes the client SDK.
# step 2) Your server generates and sends a client token back to your client using the server SDK.

@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid session, Please login again!'})
# Token will be generated here
    return JsonResponse({'clientToken': gateway.client_token.generate(), 'success': True})




# create a transaction.
@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid session, Please login again!'})

    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]

    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })

    if result.is_success:
        return JsonResponse({
            # NOTE: transaction spelling bug was fixed later
            "success": result.is_success, 'transaction': {'id': result.transaction.id, 'amount': result.transaction.amount}})
    else:
        return JsonResponse({'error': True, 'sucess': False})
