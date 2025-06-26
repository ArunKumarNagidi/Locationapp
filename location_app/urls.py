from django.urls import path
from .import views


urlpatterns=[
#Locations urls starts here

    path('',views.locationsMainPage,name='locationsMainPage'),
    #person details urls
    path('personRenderData/',views.personRenderData ,name='personRenderData'),
    path('personStatusChange/<int:pk>/',views.personStatusChange ,name='personStatusChange'),
    path('deletePerson/<int:pk>/',views.deletePerson ,name='deletePerson'),
    path('updatePerson/<int:pk>/',views.updatePerson ,name='updatePerson'),
    path('get_areas_by_city/', views.get_areas_by_city, name='get_areas_by_city'),

    path('locationCountryStateCityArea',views.locationCountryStateCityArea,name='locationCountryStateCityArea'),

    #country urls
    path('showCountry/',views.showCountry, name= 'showCountry'),
    path('countryRenderData/',views.countryRenderData, name= 'countryRenderData'),
    path('countryStatusChange/<int:pk>',views.countryStatusChange, name= 'countryStatusChange'),
    path('deleteCountry/<int:pk>',views.deleteCountry, name= 'deleteCountry'),
    path('updateCountry/<int:pk>',views.updateCountry, name= 'updateCountry'),

    #state urls
    path('showState/', views.showState, name='showState'),
    path('stateRenderData/', views.stateRenderData, name='stateRenderData'),
    path('stateStatusChange/<int:pk>', views.stateStatusChange, name='stateStatusChange'),
    path('deleteState/<int:pk>', views.deleteState, name='deleteState'),
    path('updateState/<int:pk>', views.updateState, name='updateState'),

    # City URLs
    path('showCity/', views.showCity, name='showCity'),
    path('cityRenderData/', views.cityRenderData, name='cityRenderData'),
    path('cityStatusChange/<int:pk>', views.cityStatusChange, name='cityStatusChange'),
    path('deleteCity/<int:pk>', views.deleteCity, name='deleteCity'),
    path('updateCity/<int:pk>', views.updateCity, name='updateCity'),
    path('get_states_by_country/', views.get_states_by_country, name='getStatesByCountry'),

    #Area urls
    path('showArea/',views.showArea, name= 'showArea'),

    path('areaRenderData', views.areaRenderData, name='areaRenderData'),
    path('areaStatusChange/<int:pk>/', views.areaStatusChange, name='areaStatusChange'),
    path('deleteArea/<int:pk>/', views.deleteArea, name='deleteArea'),
    path('updateArea/<int:pk>/', views.updateArea, name='updateArea'),
    path('get_cities_by_state', views.get_cities_by_state, name='getCitiesByState'),
    path('get_states_by_country', views.get_states_by_country, name='getStatesByCountry'),

]