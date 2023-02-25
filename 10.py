from django.db.models import Sum


Loan.objects.filter(borrower__created_at__year = 2021).aggregate(Sum("amount"))
Borrower.objects.filter(loans__status=0, loans__created_at__year=2022).distinct().count()
Borrower.objects.filter(loans__status=2).distinct().count()
