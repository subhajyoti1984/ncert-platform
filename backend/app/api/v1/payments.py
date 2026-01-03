from fastapi import APIRouter
import stripe, os

router = APIRouter()
stripe.api_key = os.getenv("STRIPE_SECRET")

@router.post("/create-checkout")
def create_checkout():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "inr",
                "product_data": {"name": "NCERT Learning Access"},
                "unit_amount": 9900
            },
            "quantity": 1
        }],
        mode="payment",
        success_url="https://yourapp/success",
        cancel_url="https://yourapp/cancel"
    )
    return {"url": session.url}


