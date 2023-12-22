from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the query from the POST data
        query = request.POST.get('query')

        # Make the API request
        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
        headers = {'X-Api-Key': 'tDSkk47a82DvgMurNmreqw==rzRGi2kZRXDsIoAl'}
        response = requests.get(api_url, headers=headers)

        if response.status_code == requests.codes.ok:
            data_list = response.json()

            if data_list:  # Check if the list is not empty
                # Assume the relevant data is in the first item of the list
                data = data_list[0]

                # Extract relevant nutrition data
                protein_data = data.get('protein_g', 0)
                carb_data = data.get('carbohydrates_total_g', 0)
                fat_data = data.get('fat_total_g', 0)
                calories_data = data.get('calories', 0)
                food_name = data.get('name', '')

                # Pass data to the template
                return render(request, 'progress/index.html', {
                    'query': query,
                    'protein_data': protein_data,
                    'carb_data': carb_data,
                    'fat_data': fat_data,
                    'calories_data': calories_data,
                    'food_name': food_name,
                })
            else:
                # Handle the case when the list is empty
                print("Error: Empty response list")
        else:
            print("Error:", response.status_code, response.text)
    
    # Render the template without data if the request method is not POST
    return render(request, 'progress/index.html')
