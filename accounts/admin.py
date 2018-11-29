from django.contrib import admin
from .models import Customers, Material, Account
from django.forms import DateInput, NumberInput
from django.db import models
from django.forms.models import BaseInlineFormSet


class MaterialInlineFormset(BaseInlineFormSet):
    def clean(self):
        total = 0
        if len(self.forms) > 0:
            for f in self.forms:
                if not f.cleaned_data['DELETE']:
                    total += f.cleaned_data['quantity'] * f.cleaned_data['material_name'].price


class MaterialInline(admin.TabularInline):
    model = Account
    formset = MaterialInlineFormset
    ordering = ['date']
    exclude = (
        'Remark',
    )
    extra = 0
    formfield_overrides = {
        models.DateField: {'widget': DateInput(attrs={'size': '20em'})},
    }


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_circle</i>'

    list_display = ('material_name', 'price')
    list_filter = ('material_name', 'price')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_circle</i>'

    list_display = ('customer_name',)

    readonly_fields = ('total',)


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_circle</i>'

    list_display = ('name', 'address', 'contact_no')
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = [MaterialInline]
