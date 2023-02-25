@transaction.atomic
@api_view(["POST"])
def api_create_invesotr(request):
    investor = Investor.objects.create()
    transaction.on_commit(lambda: investor_task.delay(investor.id))
    time.sleep(0.5)
    return Response({"status": "OK"})


@shared_task
def investor_task(investor_id):
    with transaction.atomic():
        investor = Investor.objects.select_for_update().get(pk=investor_id)
        investor.processed = True
        investor.save()
