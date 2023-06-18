from django.db import models
import secrets
from .paystack import PayStack


# Create your models here.
class Payment(models.Model):
    amount = models.PositiveIntegerField()
    email = models.EmailField()
    ref = models.CharField(max_length=250)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created',)

    # create new reference if none exists
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            new_ref = secrets.token_urlsafe(50)
            check_similar_ref = Payment.objects.filter(ref=new_ref)

            if not check_similar_ref:
                self.ref = new_ref
        super().save(*args, **kwargs)
 
    # verify payment
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_paystack_transaction(self.ref, self.amount)

        if status:
            if result['amount'] / 100 == self.amount:
                self.is_verified = True
            self.save()
        if self.is_verified:
            return True
        return False
    
    
    def __str__(self) -> str:
        return f"Payment: {self.amount}"