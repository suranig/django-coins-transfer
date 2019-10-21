from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Transfer(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='sender',
                               on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='receiver',
                                 on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)

    def clean(self):
        if self.sender.balance < self.amount:
            raise ValidationError(
                'You have not enough coins to send. Try to send less.',
                code='invalid')
        elif self.sender == self.receiver:
            raise ValidationError('You cannot send coins to yourself.',
                                  code='invalid')
        elif self.amount <= 0:
            raise ValidationError('Mininium amount to send is 1.',
                                  code='invalid')

    def save(self, *args, **kwargs):
        self.full_clean()
        self.sender.balance = self.sender.balance - self.amount
        self.sender.save()
        self.receiver.balance = self.receiver.balance + self.amount
        self.receiver.save()
        return super(Transfer, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.sender} sent {self.amount} to {self.receiver}'
