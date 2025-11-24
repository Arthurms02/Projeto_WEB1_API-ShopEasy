from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order, PaymentTransaction
from .services import processar_pagamento, process_webhook_notification


@receiver(pre_save, sender=PaymentTransaction)
def atualizar_estoque(sender, instance, **kwargs):
    print(f"Verificando pagamento para a ordem {instance.order.id} com status {instance.status}")
    if instance.status == 'Pago':
        processar_pagamento(instance)
        process_webhook_notification(instance.order.id, instance.transaction_id, instance.status)
        print(f"Atualizando status da ordem {instance.order.id} para 'Processando'")
        instance.order.status = 'Processando'
        instance.order.save()

    