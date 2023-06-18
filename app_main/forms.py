from django import forms

class BuyForm(forms.Form):
    wather = forms.CharField(max_length=10, required=False, label="นำ้เปล่า")
    rice = forms.CharField(max_length=10, required=False, label="ข้าวสวย")
    banana = forms.CharField(max_length=10, required=False, label="กล้วย")
    bread = forms.CharField(max_length=10, required=False, label="ขนมปัง")
    milk = forms.CharField(max_length=10, required=False, label="นม")
