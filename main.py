from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import stripe

stripe.api_key="sk_test_51HwUlaA67jZ6i4HK3X9Ddp6QtOMIVGzGEtMu4DjYMQN5W6dBWZo4ig8PhyLzr4fYMBPWDNoGSsjzgFHXQ8KD88EB00Du50yLoA"

app = FastAPI()

class DigitalPayments(BaseModel):
    application_amount_fee: float

@app.post("/card_pay", status_code=status.HTTP_200_OK)
def card_pay(digital_payment: DigitalPayments):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(digital_payment.application_amount_fee * 100),  # Convert to cents
            currency="eur",  # Change currency as needed
            payment_method_types=["card"],  # Collect card details directly
            description=f"Payment for table {digital_payment.table_no}",
            transfer_data={"destination": "acct_1L4LUOPGTC9ra4FK"}  # Replace with your connected account ID
        )
        return {"client_secret": payment_intent.client_secret}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post("/apple_pay", status_code=status.HTTP_200_OK)
def apple_pay(digital_payment: DigitalPayments):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(digital_payment.amount * 100),  # Amount in cents
            currency="eur",  # Change currency as needed
            payment_method_types=["card_present"],
            application_fee_amount=int(digital_payment.application_amount_fee * 100),  # Convert to cents
            transfer_data={"destination": "acct_1L4LUOPGTC9ra4FK"}, #account id is fake
        )
        return {"payment_intent_id": payment_intent.id}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@app.post("/google_pay", status_code=status.HTTP_200_OK)
def google_pay(digital_payment: DigitalPayments):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(digital_payment.amount * 100),  # Amount in cents
            currency="eur",  # Change currency as needed
            payment_method_types=["card_present"],
            application_fee_amount=int(digital_payment.application_amount_fee * 100),  # Convert to cents
            transfer_data={"destination": "acct_1L4LUOPGTC9ra4FK"}, #account id is fake
        )
        return {"payment_intent_id": payment_intent.id}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
