from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from myapp.models import SystemNumber, Agency, County
# Create your views here.
def upload_file_view(request):
    error_message = None
    success_message = None

    form = CsvForm(request.POST or None, request.FILES or None)
    # check whether it's valid:
    if form.is_valid():
        form.save()
        form = CsvForm()


        # obj.activated=True
        # obj.save()

        # try:
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            n = 0
            for row in reader:
                # what we need is a common list element for each row. 
                
                if n == 0:
                    n = 1
                    print(row)
                    continue    # continue here
                elif n == 1:
                    print(row)
                    n = n + 1
                elif n % 90 == 0:
                    print(row)
                    n = n + 1
                else:
                    n = n + 1


                # print(row[0])
                # print(row[1])
                # County.objects.create(
                #     coid = row[0],
                #     name = row[1],
                # )
                # for item in row:
                #     print(type(item) + len(item))

                ag_sys_name = row[0]
                ag_sys_no = row[8]

                # Agency.objects.create(
                #     system_name = ag_sys_name,
                #     county = row[1],
                #     state = row[2],
                #     active = (int(row[3]) == 1),
                #     system_type = row[4],
                #     address = row[5],
                #     city = row[6],
                #     zipcode = row[7],
                # )

                SystemNumber.objects.get_or_create(
                    sys_name= ag_sys_name,
                    system_no= ag_sys_no, 
                )


        obj.activated=True
        obj.save()
        #     success_message = "Uploaded Successful..."
        # except:
        #     error_message = "Oops. something went wrong..."


    context = {'form': form, 'success_message': success_message, 'error_message': error_message,}
    return render(request, 'csvs/upload.html', context)
