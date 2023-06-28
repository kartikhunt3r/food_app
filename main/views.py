from django.shortcuts import render
from .models import Dishz
import json

def search_dishes(request):
    query = request.GET.get('query')
    if query:
        queryset = Dishz.objects.filter(items__icontains=query)
        
        resullt = []
        
        for obj in queryset:
            json_data = obj.items
            if json_data:
                data_dict = json.loads(json_data)
                restaurant_name=obj.name


                # Filter the dictionary based on your criteria
                filtered_items = {k: v for k, v in data_dict.items() if query in k.lower()}
                restaurant_result = {'name': restaurant_name, 'items': filtered_items}

                # Append the filtered items to the result list
                resullt.append(restaurant_result)
                # resullt.append(filtered_items)


    else:
        resullt = []
        
    print(resullt)

    return render(request, 'search/results.html', {'results': resullt})
