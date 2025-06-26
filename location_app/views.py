
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from django.http import HttpResponse, JsonResponse

from .models import *

# Create your views here.


def locationCountryStateCityArea(request):
    return render(request,'location_country_state_area_city.html')

def showCountry(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.method == 'POST':
            country = request.POST.get('country')
            if Country.objects.filter(country_name=country).exists():
                messages.error(request,'Country already exists.',extra_tags='danger')
            else:
                Country.objects.create(

                    country_name=country
                )
                messages.error(request,'Country created successfully.',extra_tags='success')
            return redirect('showCountry')
    except Exception as e:
        print(f"error:{str(e)}")
        messages.error(request, f"An error occured {str(e)}", extra_tags='danger')
        return redirect('showCountry')

    return render(request,'locations/country/country.html')


def countryRenderData(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.headers.get('HX-Request'):
            edit_id = request.GET.get('editid')
            if edit_id:
                country_details = get_object_or_404(Country, id=edit_id)
                context ={
                    'c':country_details
                }
                return render(request,'locations/country/country_components/country_edit_form.html',context)
            query = request.GET.get('query')
            query_name = Q()
            if query:
                query_name &=Q(

                    Q(country_name__icontains = query)
                )
            country_details = Country.objects.filter(query_name).order_by('-id')
            page_number = request.GET.get('page')
            paginator= Paginator(country_details,10)
            page_obj = paginator.get_page(page_number)
            context = {
                'country_records':page_obj
            }
            return render(request,'locations/country/country_components/country_list_data.html',context)
    except Exception as e:
        print(f"error:{str(e)}")
        messages.error(request, f'Error occured {str(e)}', extra_tags='danger')
        return redirect('showCountry')



def countryStatusChange(request,pk):
    try:
        country_details = get_object_or_404(Country,id=pk)
        if request.headers.get('HX-Request'):
            country_details.country_status = not country_details.country_status
            country_details.save()
            return render(request,'locations/country/country_components/country_status_change.html', {'country':country_details,'status_page':'country_page'})
    except Exception as e:
        print(str(e)," Error")
        messages.error(request, f"An error Occured {str(e)}",extra_tags='danger')
        return redirect('countryRenderData')


def deleteCountry(request,pk):
    try:
        country_delete= get_object_or_404(Country,id=pk)
        country_delete.delete()
        messages.error(request, "Country deleted successfully.",extra_tags='success')
        return redirect('showCountry')
    except Exception as e:
        print(str(e),"Error")
        messages.error(request,f"an Error Occured {str(e)}",extra_tags='danger')
        return redirect('showCountry')


def updateCountry(request,pk):
    try:
        admin_regid = request.session.get('master_id')
        country_details = get_object_or_404(Country, id=pk)
        if request.method == 'POST':
            country = request.POST.get('ucountry')
            if Country.objects.exclude(id=pk).filter(country_name=country).exists():
                messages.error(request,'Country already exists.',extra_tags='danger')
            else:

                country_details.country_name = country
                country_details.save()
                messages.error(request,'Country Updated successfully.',extra_tags='success')
            return redirect('showCountry')
    except Exception as e:
        print(str(e), "Error")
        messages.error(request, f"an error occured {str(e)}", extra_tags='danger')
        return redirect('showCountry')

#state starts here

def showState(request):
    try:

        admin_regid = request.session.get('master_id')
        if request.method == 'POST':
            state = request.POST.get('state')
            country_id = request.POST.get('country')
            country = Country.objects.get(id=country_id,country_status=True)

            if State.objects.filter(country_ref=country,state_name=state).exists():
                messages.error(request,'State already exists.',extra_tags='danger')
            else:
                State.objects.create(
                    country_ref = country,
                    state_name=state
                )
                messages.error(request,'state created successfully.',extra_tags='success')
            return redirect('showState')
    except Exception as e:
        print(f"error:{str(e)}")
        messages.error(request, f"An error occured {str(e)}", extra_tags='danger')
        return redirect('showState')
    context={
        'country':Country.objects.filter(country_status=True)
    }

    return render(request,'locations/state/state.html',context)


def stateRenderData(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.headers.get('HX-Request'):
            edit_id = request.GET.get('editid')
            if edit_id:
                state_details = get_object_or_404(State, id=edit_id)
                context ={
                    's':state_details,
                    'country': Country.objects.filter(country_status=True)
                }
                return render(request,'locations/state/state_components/state_edit_form.html',context)
            query = request.GET.get('query')
            query_name = Q()
            if query:
                query_name &=Q(
                    Q(state_name__icontains = query)
                )
            state_details = State.objects.filter(query_name).order_by('-id')
            page_number = request.GET.get('page')
            paginator= Paginator(state_details,10)
            page_obj = paginator.get_page(page_number)
            context = {
                'state_records':page_obj
            }
            return render(request,'locations/state/state_components/state_components_list_data.html',context)
    except Exception as e:
        print(f"error:{str(e)}")
        messages.error(request, f'Error occured {str(e)}', extra_tags='danger')
        return redirect('showState')


def stateStatusChange(request,pk):
    try:
        state_details = get_object_or_404(State,id=pk)
        if request.headers.get('HX-Request'):
            state_details.state_status = not state_details.state_status
            state_details.save()
            return render(request,'locations/state/state_components/state_components_status_change.html', {'state':state_details,'status_page':'state_page'})
    except Exception as e:
        print(str(e)," Error")
        messages.error(request, f"An error Occured {str(e)}",extra_tags='danger')
        return redirect('stateRenderData')

def deleteState(request,pk):
    try:
        state_delete = get_object_or_404(State, id=pk)
        state_delete.delete()
        messages.error(request,"State deleted successfully.",extra_tags='success')
        return redirect('showState')
    except Exception as e:
        print(str(e),"Error")
        messages.error(request,f"an Error Occured {str(e)}",extra_tags='danger')
        return redirect('showState')

def updateState(request,pk):
    try:
        admin_regid = request.session.get('master_id')
        state_details = get_object_or_404(State,id=pk)
        if request.method == 'POST':
            country_id = request.POST.get('ucountry')
            state = request.POST.get('ustate')
            country = get_object_or_404(Country, id=country_id)
            if State.objects.exclude(id=pk).filter(country_ref=country,state_name=state).exists():
                messages.error(request, 'State already exists.',extra_tags='danger')
            else:
                state_details.country_ref=country
                state_details.state_name=state

                state_details.save()
                messages.error(request,'State updated successfully.',extra_tags='success')
            return redirect('showState')
    except Exception as e:
        print(str(e),"Error")
        messages.error(request,f"an error occured {str(e)}", extra_tags='danger')
        return redirect('showState')
#State ends here



#state ends here

#city starts here


def showCity(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.method == 'POST':
            city = request.POST.get('city')
            country_id = request.POST.get('country')
            state_id = request.POST.get('state')
            country = Country.objects.get( id=country_id, country_status=True)
            state = State.objects.get(id=state_id, state_status=True,
                                      country_ref=country)

            if City.objects.filter(country_ref=country, state_ref=state,
                                   city_name=city).exists():
                messages.error(request, 'City already exists.', extra_tags='danger')
            else:
                City.objects.create(
                    country_ref=country,
                    state_ref=state,
                    city_name=city
                )
                messages.error(request, 'City created successfully.', extra_tags='success')
            return redirect('showCity')
    except Exception as e:
        print(f"error: {str(e)}")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('showCity')

    context = {
        'country': Country.objects.filter(country_status=True),
        'state': State.objects.filter(state_status=True)
    }
    return render(request, 'locations/city/city.html', context)



def cityRenderData(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.headers.get('HX-Request'):
            edit_id = request.GET.get('editid')
            if edit_id:
                city_details = get_object_or_404(City, id=edit_id)
                context = {
                    's': city_details,
                    'country': Country.objects.filter(country_status=True),
                    'state': State.objects.filter(state_status=True,
                                                  country_ref=city_details.country_ref)
                }
                return render(request, 'locations/city/city_components/city_components_edit_form.html',context)

            query = request.GET.get('query')
            query_name = Q()
            if query:
                query_name &= Q(
                    Q(city_name__icontains=query)|
                    Q(state_ref__state_name__icontains=query)|
                    Q(country_ref__country_name__icontains=query)
                )
            city_details = City.objects.filter(query_name).order_by('-id')
            page_number = request.GET.get('page')
            paginator = Paginator(city_details, 10)
            page_obj = paginator.get_page(page_number)
            context = {
                'city_records': page_obj
            }
            return render(request, 'locations/city/city_components/city_components_list_data.html',
                          context)
    except Exception as e:
        print(f"error: {str(e)}")
        messages.error(request, f'Error occurred {str(e)}', extra_tags='danger')
        return redirect('showCity')


def cityStatusChange(request, pk):
    try:
        city_details = get_object_or_404(City, id=pk)
        if request.headers.get('HX-Request'):
            city_details.city_status = not city_details.city_status
            city_details.save()
            return render(request, 'locations/city/city_components/city_components_status_change.html',
                          {'city': city_details, 'status_page': 'city_page'})
    except Exception as e:
        print(str(e), " Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('cityRenderData')



def deleteCity(request, pk):
    try:
        city_delete = get_object_or_404(City, id=pk)
        city_delete.delete()
        messages.error(request, "City deleted successfully.", extra_tags='success')
        return redirect('showCity')
    except Exception as e:
        print(str(e), "Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('showCity')



def updateCity(request, pk):
    try:
        admin_regid = request.session.get('master_id')
        city_details = get_object_or_404(City, id=pk)
        if request.method == 'POST':
            country_id = request.POST.get('ucountry')
            state_id = request.POST.get('ustate')
            city = request.POST.get('ucity')
            country = get_object_or_404(Country, id=country_id)
            state = get_object_or_404(State, id=state_id, country_ref=country)

            if City.objects.exclude(id=pk).filter(country_ref=country,
                                                  state_ref=state, city_name=city).exists():
                messages.error(request, 'City already exists.', extra_tags='danger')
            else:
                city_details.country_ref = country
                city_details.state_ref = state
                city_details.city_name = city
                city_details.save()
                messages.error(request, 'City updated successfully.', extra_tags='success')
            return redirect('showCity')
    except Exception as e:
        print(str(e), "Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('showCity')

#get states accordig to country in city

def get_states_by_country(request):
    try:
        country_id = request.GET.get('country_id')
        states = State.objects.filter(country_ref_id=country_id, state_status=True).values('id', 'state_name')
        return JsonResponse({'states': list(states)})
    except Exception as e:
        print(f"error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
#City ends here


#Area starts here

def showArea(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.method == 'POST':
            area = request.POST.get('area')
            country_id = request.POST.get('country')
            state_id = request.POST.get('state')
            city_id = request.POST.get('city')
            country = Country.objects.get(id=country_id, country_status=True)
            state = State.objects.get(id=state_id, state_status=True, country_ref=country)
            city = City.objects.get(id=city_id, city_status=True, state_ref=state, country_ref=country)

            if Area.objects.filter(country_ref=country, state_ref=state, city_ref=city, area_name=area).exists():
                messages.error(request, 'Area already exists.', extra_tags='danger')
            else:
                Area.objects.create(
                    country_ref=country,
                    state_ref=state,
                    city_ref=city,
                    area_name=area
                )
                messages.error(request, 'Area created successfully.', extra_tags='success')
            return redirect('showArea')
    except Exception as e:
        print(f"error: {str(e)}")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('showArea')

    context = {
        'country': Country.objects.filter(country_status=True),
        'state': State.objects.filter(state_status=True),
        'city': City.objects.filter(city_status=True)
    }
    return render(request, 'locations/area/area.html', context)


def areaRenderData(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.headers.get('HX-Request'):
            edit_id = request.GET.get('editid')
            if edit_id:
                area_details = get_object_or_404(Area, id=edit_id)
                context = {
                    's': area_details,
                    'country': Country.objects.filter(country_status=True),
                    'state': State.objects.filter(state_status=True, country_ref=area_details.country_ref),
                    'city': City.objects.filter(city_status=True, state_ref=area_details.state_ref)
                }
                return render(request, 'locations/area/area_components/area_components_edit_form.html', context)

            query = request.GET.get('query')
            query_name = Q()
            if query:
                query_name &= Q(
                    Q(area_name__icontains=query)|
                    Q(city_ref__city_name__icontains=query)|
                    Q(state_ref__state_name__icontains=query)|
                    Q(country_ref__country_name__icontains = query)
                )
            area_details = Area.objects.filter(query_name).order_by('-id')
            page_number = request.GET.get('page')
            paginator = Paginator(area_details, 10)
            page_obj = paginator.get_page(page_number)
            context = {
                'area_records': page_obj
            }
            return render(request, 'locations/area/area_components/area_components_list_data.html', context)
    except Exception as e:
        print(f"error: {str(e)}")
        messages.error(request, f'Error occurred {str(e)}', extra_tags='danger')
        return redirect('showArea')


def areaStatusChange(request, pk):
    try:
        area_details = get_object_or_404(Area, id=pk)
        if request.headers.get('HX-Request'):
            area_details.area_status = not area_details.area_status
            area_details.save()
            return render(request, 'locations/area/area_components/area_components_status_change.html',
                          {'area': area_details, 'status_page': 'area_page'})
    except Exception as e:
        print(str(e), " Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('areaRenderData')


def deleteArea(request, pk):
    try:
        area_delete = get_object_or_404(Area, id=pk)
        area_delete.delete()
        messages.error(request, "Area deleted successfully.", extra_tags='success')
        return redirect('showArea')
    except Exception as e:
        print(str(e), "Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('showArea')


def updateArea(request, pk):
    try:
        admin_regid = request.session.get('master_id')
        area_details = get_object_or_404(Area, id=pk)
        if request.method == 'POST':
            country_id = request.POST.get('ucountry')
            state_id = request.POST.get('ustate')
            city_id = request.POST.get('ucity')
            area = request.POST.get('uarea')
            country = get_object_or_404(Country, id=country_id)
            state = get_object_or_404(State, id=state_id, country_ref=country)
            city = get_object_or_404(City, id=city_id, state_ref=state, country_ref=country)

            if Area.objects.exclude(id=pk).filter( country_ref=country, state_ref=state, city_ref=city, area_name=area).exists():
                messages.error(request, 'Area already exists.', extra_tags='danger')
            else:
                area_details.country_ref = country
                area_details.state_ref = state
                area_details.city_ref = city
                area_details.area_name = area
                area_details.save()
                messages.error(request, 'Area updated successfully.', extra_tags='success')
            return redirect('showArea')
    except Exception as e:
        print(str(e), "Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('showArea')

def get_cities_by_state(request):
    try:
        state_id = request.GET.get('state_id')
        cities = City.objects.filter(state_ref_id=state_id, city_status=True).values('id', 'city_name')
        return JsonResponse({'cities': list(cities)})
    except Exception as e:
        print(f"error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


def get_areas_by_city(request):
    try:
        city_id = request.GET.get('city_id')
        areas = Area.objects.filter(city_ref_id=city_id, area_status=True).values('id', 'area_name')
        return JsonResponse({'areas': list(areas)})
    except Exception as e:
        print(f"error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)



# person details
def locationsMainPage(request):

    try:
        admin_regid = request.session.get('master_id')
        if request.method == 'POST':
            person_name = request.POST.get('person_name')
            gender = request.POST.get('gender')
            country_id = request.POST.get('country')
            state_id = request.POST.get('state')
            city_id = request.POST.get('city')
            area_id = request.POST.get('area')
            country = get_object_or_404(Country, id=country_id, country_status=True)
            state = get_object_or_404(State, id=state_id, state_status=True, country_ref=country)
            city = get_object_or_404(City, id=city_id, city_status=True, state_ref=state, country_ref=country)
            area = get_object_or_404(Area, id=area_id, area_status=True, city_ref=city, state_ref=state, country_ref=country)


            Person.objects.create(
                person_name=person_name,
                gender=gender,
                country_ref=country,
                state_ref=state,
                city_ref=city,
                area_ref=area
            )
            messages.error(request, 'Person created successfully.', extra_tags='success')
            return redirect('locationsMainPage')
    except Exception as e:
        print(f"error: {str(e)}")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('locationsMainPage')

    context = {
        'country': Country.objects.filter(country_status=True),
        'state': State.objects.filter(state_status=True),
        'city': City.objects.filter(city_status=True),
        'area': Area.objects.filter(area_status=True)
    }
    return render(request, 'person_details/locations_main_page.html', context)

def personRenderData(request):
    try:
        admin_regid = request.session.get('master_id')
        if request.headers.get('HX-Request'):
            edit_id = request.GET.get('editid')
            if edit_id:
                person_details = get_object_or_404(Person, id=edit_id)
                context = {
                    'p': person_details,
                    'country': Country.objects.filter(country_status=True),
                    'state': State.objects.filter(state_status=True, country_ref=person_details.country_ref),
                    'city': City.objects.filter(city_status=True, state_ref=person_details.state_ref),
                    'area': Area.objects.filter(area_status=True, city_ref=person_details.city_ref)
                }
                return render(request, 'person_details/person_details_components/person_details_components_edit_form.html', context)

            query = request.GET.get('query')
            query_name = Q()
            if query:
                query_name &= Q(
                    Q(person_name__icontains=query) |
                    Q(gender__icontains=query) |
                    Q(country_ref__country_name__icontains=query) |
                    Q(state_ref__state_name__icontains=query) |
                    Q(city_ref__city_name__icontains=query) |
                    Q(area_ref__area_name__icontains=query)
                )
            person_details = Person.objects.filter(query_name).order_by('-id')
            page_number = request.GET.get('page')
            paginator = Paginator(person_details, 10)
            page_obj = paginator.get_page(page_number)
            context = {
                'person_records': page_obj
            }
            return render(request, 'person_details/person_details_components/person_details_omponents_list_data.html', context)
    except Exception as e:
        print(f"error: {str(e)}")
        messages.error(request, f'Error occurred {str(e)}', extra_tags='danger')
        return redirect('locationsMainPage')

def personStatusChange(request, pk):
    try:
        person_details = get_object_or_404(Person, id=pk)
        if request.headers.get('HX-Request'):
            person_details.person_status = not person_details.person_status
            person_details.save()
            return render(request, 'person_details/person_details_components/person_details_components_status_change.html', {
                'person': person_details,
                'status_page': 'person_page'
            })
    except Exception as e:
        print(str(e), " Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('personRenderData')

def deletePerson(request, pk):
    try:
        person_delete = get_object_or_404(Person, id=pk)
        person_delete.delete()
        messages.error(request, "Person deleted successfully.", extra_tags='success')
        return redirect('locationsMainPage')
    except Exception as e:
        print(str(e), "Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('locationsMainPage')

def updatePerson(request, pk):
    try:
        admin_regid = request.session.get('master_id')
        person_details = get_object_or_404(Person, id=pk)
        if request.method == 'POST':
            person_name = request.POST.get('uperson_name')
            gender = request.POST.get('ugender')
            country_id = request.POST.get('ucountry')
            state_id = request.POST.get('ustate')
            city_id = request.POST.get('ucity')
            area_id = request.POST.get('uarea')
            country = get_object_or_404(Country, id=country_id)
            state = get_object_or_404(State, id=state_id, country_ref=country)
            city = get_object_or_404(City, id=city_id, state_ref=state, country_ref=country)
            area = get_object_or_404(Area, id=area_id, city_ref=city, state_ref=state, country_ref=country)

            # if Person.objects.exclude(id=pk).filter(
            #     country_ref=country,
            #     state_ref=state,
            #     city_ref=city,
            #     area_ref=area,
            #     person_name=person_name,
            #     gender=gender
            # ).exists():
            #     messages.error(request, 'Person already exists.', extra_tags='danger')
        # else:
            person_details.person_name = person_name
            person_details.gender = gender
            person_details.country_ref = country
            person_details.state_ref = state
            person_details.city_ref = city
            person_details.area_ref = area
            person_details.save()
            messages.error(request, 'Person updated successfully.', extra_tags='success')
            return redirect('locationsMainPage')
    except Exception as e:
        print(str(e), "Error")
        messages.error(request, f"An error occurred {str(e)}", extra_tags='danger')
        return redirect('locationsMainPage')

#Area ends here
