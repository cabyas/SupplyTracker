from decimal import Decimal
from email.policy import default

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from tracker.utils.db import unique_slug_generator


class Network(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    rpc_url = models.URLField(null=False, blank=False)
    chain_id = models.PositiveIntegerField()
    currency_symbol = models.CharField(max_length=20, null=True, blank=True)
    block_explorer = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Token(models.Model):
    network = models.ForeignKey(Network, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=10)
    contract_address = models.CharField(max_length=100)
    decimals = models.IntegerField(default=18)

    def img_logo_path(instance, filename):
        return f'tokens/{instance.contract_address}/{filename}'
    logo = models.ImageField(upload_to=img_logo_path, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def data(self):
        dates = []
        supply = []
        for s in self.supply_data.all():
            dates.append(s.created_at.strftime('%m/%d/%Y %H:%M'))
            supply.append(s.supply * Decimal(10 ** -self.decimals))

        return {
            'dates': dates,
            'supply': supply
        }

    def create_supply_snapshot(self):
        from tracker.utils.supply_checker import check_supply_for
        current_supply = check_supply_for(self)
        SupplySnapshot.objects.create(
            token=self,
            supply=current_supply
        )
        return current_supply


class SupplySnapshot(models.Model):
    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name='supply_data')
    created_at = models.DateTimeField(auto_now_add=True)
    supply = models.DecimalField(decimal_places=4, max_digits=32)

    def __str__(self) -> str:
        return f'{self.token.name} > {self.supply}'


@receiver(pre_save, sender=Network)
def generate_network_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, 'name')
