from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import LxyClass
from .models import LxyOffice
from . import models
from django.shortcuts import redirect

from .models import LxyVehicle
from .models import LxyCustomer



def index(request):
    return render(request,'cars/welcome.html')

def list_class(request):
    lxy_class_list=LxyClass.objects.order_by('class_over_m_fee')
    context={'lxy_class_list':lxy_class_list}
    return render(request,'cars/listclass.html',context)

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        verify=request.POST.get('verify')
        # if verify=='yes' or verify=='YES':
        #     person=models.LxyAdmin.objects.get(cust_email=email)
        #     if password==person.cust_password:
        #         return HttpResponse('login successful')# this should redirect to the admin platform
        #     else:
        #         return HttpResponse('login failed')
        # else:
        person=models.LxyCustomer.objects.filter(cust_email=email)
        if not person.exists():
            return HttpResponse("user doesn't exist")
        person=models.LxyCustomer.objects.get(cust_email=email)
        if password==person.cust_password:
            #return HttpResponse('login successful')
            return redirect('/cars/userplatform')  # this should redirect to the user platform
        else:
            return HttpResponse('login failed')
    return render(request,'login/login.html')
# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         verify=request.POST.get('verify')
#         if verify=='yes' or verify=='YES':
#             person=models.LxyAdmin.objects.get(email=email)
#             if password==person.password:
#                 return HttpResponse('login successful')# this should redirect to the admin platform
#             else:
#                 return HttpResponse('login failed')
#         else:
#             person=models.LxyCustomer.objects.get(cust_email=email)
#             if password==person.password:
#                 #return HttpResponse('login successful')
#                 return redirect('/cars/userplatform')  # this should redirect to the user platform
#             else:
#                 return HttpResponse('login failed')
#     return render(request,'login/login.html')

def register(request):
    if request.method=='POST':
        cid=request.POST.get('id')
        name=request.POST.get('username')
        password=request.POST.get('password')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        #type=request.POST.get('customertype')
        #verify=request.POST.get('verify')
        # if verify=='yes'or verify=='YES':
        #     models.LxyAdmin.objects.create(
        #         adminname=name,
        #         email=email,
        #         password=password,
        #     )
        # else:
        models.LxyCustomer.objects.create(
            cust_id=cid,
            cust_username=name,
            cust_password=password,
            cust_street = street,
            cust_city = city,
            cust_state = state,
            cust_zip = zip,
            cust_email = email,
            cust_phone = phone,
            #cust_type = type,
        )
            
        return redirect('register/regisuccess')
    return render(request,'register/register.html')

def regisuccess(request):
    return render(request,'register/regisuccess.html')

def vcrud(request):
    vehicle_list=models.LxyVehicle.objects.all()
    context={'vehicle_list':vehicle_list}
    return render(request,'vehicle_crud/vcrud.html',context)
    

def addvehicle(request):
    if request.method=='POST':
        vlice=request.POST.get('vehi_lice')#primarykey
        vvin=request.POST.get('vehi_vin')
        vmake=request.POST.get('vehi_make')
        vmodel=request.POST.get('vehi_model')
        vyear=request.POST.get('vehi_year')
        vclass=request.POST.get('class_id')
        voffi=request.POST.get('office_id')
        
        models.LxyVehicle.objects.create(
            vehi_lice=vlice,
            vehi_vin = vvin,
            vehi_make = vmake,
            vehi_model = vmodel,
            vehi_year = vyear,
            class_field=LxyClass.objects.get(pk=vclass),
            offi_id=LxyOffice.objects.get(pk=voffi).pk
        )
        
        return redirect('/cars/crud')
    return render(request,'vehicle_crud/addvehicle.html')

# def searchvehicle(request):
#     if request.method=='POST':
#         vmodel=request.POST.get('vehi_model')
#         print(vmodel)
#         vehicle_list=models.LxyVehicle.objects.filter(vehi_model=vmodel)
#         context={'vehicle_list':vehicle_list}
#         print('success')
#         return render(request,'userplatform/search.html',context)
#     else:
#         return HttpResponse('search failed')
#     #return render(request,'userplatform/searchresult.html',context)

def searchvehicle(request):
    vmodel=request.GET.get('vehi_model')
    print(vmodel)
    vehicle_list=models.LxyVehicle.objects.filter(vehi_model=vmodel)
    context={'vehicle_list':vehicle_list}
    return render(request,'userplatform/searchresult.html',context)
def checkout(request):
    expenses=0
    if request.method=='POST':
        orderlist=models.LxyRentServ.objects.first()
        drop_id=request.POST.get('drop_offi')
        do=models.LxyOffice.objects.get(offi_id=drop_id)
        dd=request.POST.get('drop_date')
        eod=request.POST.get('eodom')

        orderlist.drop_offi=do
        orderlist.drop_date=dd 
        orderlist.eodom=eod 
        orderlist.save()
        #默认距离：1000,超出租车天数就要与之比较
        standard=1000

        vid=orderlist.vehi_lice.vehi_lice
        vc=models.LxyVehicle.objects.get(pk=vid).class_field
        daily_rate=vc.class_dailyrate
        over_fee=vc.class_over_m_fee
        start_date=orderlist.pick_date
        end_date=orderlist.drop_date
        print(str(start_date)[8:10])
        print(str(end_date)[8:10])
        days=int(str(end_date)[8:10])-int(str(start_date)[8:10])
        basecost=days*daily_rate
        overfee=(int(orderlist.eodom)-int(orderlist.sodom)-standard)*over_fee
        if orderlist.unlimi=='yes':
            orderlist.payment=basecost
            overfee=0
            orderlist.save()
            return render(request,'userplatform/checkout.html',{'orderlist':orderlist,'base':basecost,'overfee':overfee,'daily_rate':daily_rate,'over_fee':over_fee})
        if days<orderlist.dail_limi:
            orderlist.payment=basecost
        else:
            orderlist.payment=basecost+overfee
        orderlist.unlimi='no'
        orderlist.save()
        #print('the expense result is:')
        #print(days)
        return render(request,'userplatform/checkout.html',{'orderlist':orderlist,'base':basecost,'overfee':overfee,'daily_rate':daily_rate,'over_fee':over_fee})
    return render(request,'userplatform/checkout.html')


def ordervehicle(request):
    if request.method=='POST':
        vid=request.POST.get('vehicle_licence')
        sn=request.POST.get('serv_numb')
        #po=request.POST.get('pick_offi')
        po=models.LxyVehicle.objects.get(vehi_lice=vid).offi.offi_id
        #do=request.POST.get('drop_offi')
        do=models.LxyVehicle.objects.get(vehi_lice=vid).offi.offi_id
        pd=request.POST.get('pick_date')
        #dd=request.POST.get('drop_date')
        sod=request.POST.get('sodom')
        #eod=request.POST.get('eodom')
        #dl=request.POST.get('dail_limi')

        #vl=request.POST.get('vehi_lice')
        vl=vid
        c=request.POST.get('cust')
        models.LxyRentServ.objects.create(
            serv_numb = sn,
            pick_offi = LxyOffice.objects.get(pk=po),
            drop_offi = LxyOffice.objects.get(pk=do),
            pick_date = pd,
            #drop_date = dd,
            sodom = sod,
            #eodom = eod,
            #dail_limi = dl,
            #unlimi = ul,
            vehi_lice = LxyVehicle.objects.get(pk=vl),
            cust = LxyCustomer.objects.get(pk=c),
        )
        orderlist=models.LxyRentServ.objects.get(vehi_lice=vid)
        vc=models.LxyVehicle.objects.get(pk=vid).class_field
        #daily_rate=models.LxyClass.objects.get(pk=vc).class_dailyrate
        daily_rate=vc.class_dailyrate
        #over_fee=models.LxyClass.objects.get(pk=vc).class_over_m_fee
        over_fee=vc.class_over_m_fee
        print(vc)
        print(daily_rate)
        print(over_fee)
        context={'orderlist':orderlist,'daily_rate':daily_rate,'over_fee':over_fee}
        #return redirect('cars/userplatform/myorder')
        return render(request,'userplatform/order.html',context)
    return render(request,'userplatform/order.html')

def myorder(request):
    orderlist=models.LxyRentServ.objects.first()
    if orderlist==None:
        return HttpResponse("you don't have order!")
    vid=orderlist.vehi_lice.vehi_lice
    print(vid)
    vc=models.LxyVehicle.objects.get(pk=vid).class_field
    daily_rate=vc.class_dailyrate
    over_fee=vc.class_over_m_fee
    print(daily_rate)
    context={'orderlist':orderlist,'daily_rate':daily_rate,'over_fee':over_fee}
    return render(request,'userplatform/myorder.html',context)
    


# def ordervehicle(request):
#     vid=request.GET.get('id')
    
#     vehicle=models.LxyVehicle.objects.get(pk=vid)
#     claid=vehicle.class_field.class_id
#     vclass=models.LxyClass.objects.get(pk=claid)
#     print('primary key is: '+str(vid))
#     print('vclass is:'+str(vclass.class_name))
#     #add the car to the rent_serv table
#     vm=vehicle.vehi_model
#     vy=vehicle.vehi_year
#     c=vehicle.class_field
#     of=vehicle.offi
#     dailyrate=vclass.class_dailyrate
#     overfee=vclass.class_over_m_fee
#     expenses=0

#     poi=request.GET.get('pick_offi_id')
#     pd=request.GET.get('pick_date')
#     sdm=request.GET.get('sodom')
#     customer_id=request.GET.get('customer_id')

#     # models.LxyRentServ.objects.create(
#     #     pick_offi=poi,
#     #     drop_offi=poi,
#     #     pick_date=pd,
#     #     drop_date=0,#default
#     #     sodom=sdm,
#     #     eodom=0,#default
#     #     dail_limi=0,#default
#     #     unlimi='no',#default
#     #     vehi_lice=LxyVehicle.objects.get(pk=pk),
#     #     cust=LxyCustomer.objects.get(customer_id),
#     # )

#     context={
#         'vehicle':vehicle,'vehicle_class':vclass,'expenses':expenses,
#         'pick_of_id':poi,'pick_date':pd,'sodom':sdm}
#     return render(request,'userplatform/completeorder.html',context)
def payment(request):
    if request.method=='POST':
        orderlist=models.LxyRentServ.objects.first()
        if orderlist==None:
            return HttpResponse("you don't have orders")
        payment=orderlist.payment
        context={'orderlist':orderlist}
        orderlist.delete()
        return redirect('/cars/userplatform/paysuccess')
    return render(request,'userplatform/pay.html')
    

def paysuccess(request):
    return render(request,'userplatform/paysuccess.html')

def delvehicle(request):
    pk=request.GET.get('id')
    obj=models.LxyVehicle.objects.filter(pk=pk)
    obj.delete()
    return redirect('/cars/crud')

def userplatform(request):
    return render(request,'userplatform/userplatform.html')
