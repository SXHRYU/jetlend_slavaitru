@api_view(["POST"])
@transaction.atomic
def api_increase_a(request, investor_id):
    try:
        investor = Investor.objects.select_for_update().filter(pk=investor_id)
    except Investor.DoesNotExist:
        raise Http404
    investor.a += 100
    time.sleep(0.5)
    investor.save()
    return Response({"status": "OK"})

@api_view(["POST"])
@transaction.atomic
def api_increase_a(request, investor_id):
    try:
        investor = Investor.objects.select_for_update().filter(pk=investor_id)
    except Investor.DoesNotExist:
        raise Http404
    investor.b += 100
    time.sleep(0.5)
    investor.save()
    return Response({"status": "OK"})