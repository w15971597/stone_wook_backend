from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
	return HttpResponse("Hello, world, this is credit card.")


# def create_card(request, data):
#
# 	ret, task_id = manager.create_card_item(
# 		bank=bank,
# 		logo=logo,
# 		card_no=card_no,
# 		delivery_time=delivery_time,
# 		current_station_id=current_station_id
# 	)
# 	if ret:
# 		return response_data(ret)
#
# 	return response_data(RESP_OK, data={"assignment_task_id": task_id})