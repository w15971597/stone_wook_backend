from django.conf.urls import patterns

from . import views


urlpatterns = patterns(
	'',
	# (r'login', views.login),
	# (r'home', views.home),
	# (r'message', views.message),
	#
	# (r'card/create', views.create_card),
	# (r'card/update', views.update_card),
	# (r'card/search', views.search_card),
	# (r'card/detail', views.get_card_detail),
	#
	# (r'bill/search', views.search_bill),
	# (r'feedback', views.feedback),
	# (r'operate', views.operate),
	(r'', views.index),
)

