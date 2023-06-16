from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import BuyForm
from .models import Good

# Create your views here.
@login_required
def	index(request):
	if request.POST:
		submit = BuyForm(request.POST)
		if submit.is_valid():
			data = submit.cleaned_data
			wather = Good.objects.get(id=1)
			wather.stock = wather.stock - int(data['wather']) if wather.stock - int(data['wather']) >= 0 else 0
			wather.save()
			rice = Good.objects.get(id=2)
			rice.stock = rice.stock - int(data['rice']) if rice.stock - int(data['rice']) >= 0 else 0
			rice.save()
			banana = Good.objects.get(id=3)
			banana.stock = banana.stock - int(data['banana']) if banana.stock - int(data['banana']) >= 0 else 0
			banana.save()
			bread = Good.objects.get(id=4)
			bread.stock = bread.stock - int(data['bread']) if bread.stock - int(data['bread']) >= 0 else 0
			bread.save()
			milk = Good.objects.get(id=5)
			milk.stock = milk.stock - int(data['milk']) if milk.stock - int(data['milk']) >= 0 else 0
			milk.save()
	all_goods = Good.objects.all()
	form = BuyForm()
	context = {
		'form': form,
		'goods': all_goods
		}
	return render(request, 'app_main/index.html', context)
