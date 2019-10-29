from django.shortcuts import render
from django.http import HttpResponse

from credit_card.models import BillTab, CardTab


def create_card_item(**kwargs):
	return CardTab.objects.create(**kwargs)


def get_card_objs(**kwargs):
	return CardTab.objects.filter(**kwargs)


def get_card_obj(**kwargs):
	return CardTab.objects.filter(**kwargs).first()


def update_card_filters(filters, updates):
	return CardTab.objects.filter(**filters).update(**updates)
