from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import *
from .models import *
from .form_x import *
from django.contrib.auth import login
import django.contrib.auth.views as log_y
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from django.views.generic.edit import *
from django.urls import *
from .links import *
from .Extra_action1 import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.


class Logging_into(log_y.LoginView):
    template_name='registration/login.html'
    def get_context_data(self, **kwargs):
        context = super(Logging_into, self).get_context_data(**kwargs)
        print("\ncalling Logging_IN class \n")
        return context


class Logging_out(log_y.LogoutView):
    template_name='registration/logout.html'
    def get_context_data(self, **kwargs):
        context = super(Logging_out, self).get_context_data(**kwargs)
        print("\ncalling Logging_OUT class \n")
        return context




class Menu(TemplateView):
    
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        print("MENU AREA")
        mark_list=Mark_model.objects.all()
        context['supported_companys']=Mark_model.objects.filter(Q(cat_type_field=Cat_type[1][1]) | Q(cat_type_field=Cat_type[2][1]) )    
        context['mark_cars']=Mark_model.objects.filter(cat_type_field=Cat_type[0][0])[:9]  
         
        
        print("marks\n"+str(mark_list))
        user_list=User.objects.all()
        print("user\n"+str(user_list))
        if self.request.user.is_authenticated :
            try:
             context['profile_x']=User_model.objects.get(user_of=self.request.user.pk)
             print("\nUser profile model "+str(context['profile_x'])+"\n")
            except User_model.DoesNotExist:
                print("\nUser profile dose not exisit\n")
                #context['profile_x']="NOT EXISIT"
                #return redirect("logout")
            
        else:
            print("No user found")
            #context['profile_x']=None

        return context


class Add_user_page(CreateView):
    
    template_name='registration/add_user.html'
    form_class=Make_user_form
    model=User
    #success_url='new_user/profile_for_<str:user_x>/make_profile'
    def get_context_data(self, **kwargs):
        context = super(Add_user_page, self).get_context_data(**kwargs)
        
        print("ADD USER AREA "+str(self.request.user.username))
        #self.success_url='new_user/profile_for_'+str(self.request.user.username)+'/make_profile'
        #print("\n Model red"+str(self.success_url)+"\n")
        return context
    def get_success_url(self):
        user_of= User.objects.last()
        login(self.request,user_of )
        print("\nnew_user/profile_for_"+str(user_of)+"/make_profile\n")
        return f'new_user/profile_for_'+str(user_of)+'/make_profile'
     
    def is_valid(self):
        valid = super().is_valid()
        if not valid:
            print("\nSOMETHING WRONG.... in user making phase\n")
            return False
        # Custom Logic
        print("\nthe user "+str(self.request.user.username)+"\n")
        return redirect()
    
    
    


class Make_profile_page(CreateView):
    
    template_name='user_profile/make_model.html'
    form_class=Make_profile_form
    model=User_model
    #success_url=str(User_model.get_absolute_url)
    def get_context_data(self, **kwargs):
        context = super(Make_profile_page, self).get_context_data(**kwargs)
        
        context['profile_owner']=self.kwargs['user_x']
        print(f"\nsuccess_url={str(User_model.get_absolute_url)}\n")
        print(f"\nmaking a profile for user "+str(context['profile_owner'])+"\n")
        return context
    
    '''def save(self, *args, **kwargs):
       if self.request.user.is_authenticated:
         user_key=User.objects.get(username=self.request.user.username)
         self.request['user_of']=user_key
       
         return super().post(self.request,*args, **kwargs) # Call the real save() method'''
    
    def form_valid(self, form: Make_profile_form):
        user_x=self.request.user
        form.instance.user_of=user_x if user_x else "NO DATA"
        print("\nLast details on user "+str(user_x)+"\n")
        return super(Make_profile_page,self).form_valid(form)
    
    


    def get_success_url(self):
        user_key= self.kwargs['user_x']
        profile_x=User_model.objects.get(user_of=self.request.user.pk)
        print(f"\nRedirecting to :user{self.request.user.pk}_{self.request.user.username}/name_of/{profile_x.name}\n")
        return reverse("core:view_user_profile",kwargs={'user_x':self.request.user.username,'user_key':self.request.user.pk,'username':self.request.user.username,'profile_name':profile_x.name})
        #return f"user{self.request.user.pk}_{self.request.user.username}/name_of/{profile_x.name}"
        

    
    
    
@login_required
def display_profile(h,user_x,user_key,username,profile_name):
    print("display User profile of"+str(username)+" with a key of "+str(profile_name)+"\n")
    the_x_user=User.objects.get(pk=user_key)
    the_x_profile=User_model.objects.get(user_of=user_key)
    user_sectors=[]
    for x in range(len(User_activity)):
        print(User_activity[x][0])
        user_sectors.insert(x,User_activity[x][0])
    return render(h,"user_profile/display_model.html",{'sectors':user_sectors,'user':the_x_user,'user_profile':the_x_profile})

@login_required
def display_x_profile(h,user_x,user_key,username,profile_name,sec_x,id_profile):
    print("display User profile of"+str(username)+" with a key of "+str(profile_name)+"\n")
    the_x_user=User.objects.get(pk=user_key)
    the_x_profile=User_model.objects.get(pk=id_profile)
    cat_list=[]
    #User_model.profile_activity
    '''users_1=User_model.objects.filter(profile_activity='مركز صيانة')
    items_1=Part_model.objects.filter(owned_by=user_key)
    items_2=Advertise_action.objects.filter(post_by=user_key)
    if the_x_profile.profile_activity == sec_x:
      items_3=Petrol_area.objects.filter(owned_by=the_x_profile.pk)
    items_4=Decorator_model.objects.filter(owned_by=user_key)
    items_5=School_of_drive.objects.filter(owned_by=user_key)'''
    if sec_x =='وقود':
        cat_list=Petrol_area.objects.filter(owned_by=the_x_profile.pk)
    elif sec_x =='محل قطع غيار':
        cat_list=Part_model.objects.filter(owned_by=the_x_profile.pk)
    elif sec_x =='إيجار':
        cat_list=Advertise_action.objects.filter(post_by=the_x_profile.pk)
    elif sec_x =='أكسسوارت':
        cat_list=Decorator_model.objects.filter(owned_by=the_x_profile.pk)
    elif sec_x =='مركز تدريب':
        cat_list=School_of_drive.objects.filter(owned_by=the_x_profile.pk)
    elif sec_x =='مركز صيانة':
        cat_list=User_model.objects.filter(user_of=the_x_profile.pk,profile_activity='مركز صيانة')
    else:
        cat_list=['bb','bb','bb','bb','bb','bb',]

    print("petrols \n"+str(cat_list))
    return render(h,"user_profile/display_x_model.html",{'items_x':cat_list, ''''items_1':items_1,
                                                         'items_2':items_2,
                                                         'items_3':items_3,
                                                         'items_4':items_4,
                                                         'items_5':items_5,'users_fix':users_1,'''
                                                         'user':the_x_user,'sector_of':sec_x,'user_profile':the_x_profile})






def deep_petrol_dit(h,user_x,user_key,username,profile_name,sec_x,id_profile,petrol_id):
    petrol_x=Petrol_area.objects.get(pk=petrol_id)
    
    the_x_profile=User_model.objects.get(pk=id_profile)

    return render(h,"petrol_zone/deep_detail.html",{'petrol_x':petrol_x,'user_profile':the_x_profile})






def all_sec_of_x(h,user_x,user_key,username,profile_name,sec_x):
    all_staff_of_x=User_model.objects.filter(profile_activity=sec_x)
    return render(h,'enduser_sec/sector.html',{'sec_type':sec_x,'sector_users':all_staff_of_x})


@login_required
def user_profile(h,user_key,username,profile_name):
    print("from bottom_menu.html display User profile of"+str(username)+" with a key of "+str(profile_name)+"\n")
    the_x_user=User.objects.get(username=username)
    the_x_profile=User_model.objects.get(user_of=user_key)
    return render(h,"bottom_menu.html",{'user':the_x_user,'user_profile':the_x_profile})


def all_marks(h):
    mark_list=Mark_model.objects.all()
    print("your list is \n"+str(mark_list))
    return render(h,"cars/marks.html",{'marks':mark_list})



def mark_models(h,k,mark_name):
    target_mark=Mark_model.objects.get(pk=k)
    target_models=Car_model.objects.filter(family_of=target_mark)
    print("\nExploring models of "+str(target_mark)+" and key model\n")
    return render(h,"cars/list_mark_model.html",{'models_of_mark':target_models,'mark':mark_name})


def model_details(h,k,mark_name,model_name,model_num):
    target_car_model=Car_model.objects.get(pk=model_num)
    print("obtaining Car details")
    return render(h,"cars/list_model_dit.html",{'the_car_model':target_car_model,'model':model_name,'mark':mark_name})





#for the fix center page



def has_a_fix_center(h,user_key,username,profile_name):
    return render(h,"user_profile/model_2_fix_center.html")


#for the driving school page

class Add_School_page(CreateView):
    model = School_of_drive
    form_class=Add_School_form
    template_name='learn_center/add_school.html'
    def get_context_data(self, **kwargs):
        context = super(Add_School_page, self).get_context_data(**kwargs)
        get_user=self.kwargs['user_key']
        #get_username=self.kwargs['user_name']
        
        #get_profile=self.kwargs['profile_name']
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\nmakeing a driving school for  user {get_user} profile {get_profile}\n")
        return context
    
    def form_valid(self, form: Add_School_form):
        user_model=self.request.user
        form.instance.owned_by=user_model
        print("\n\nvalidating the user named as "+str(user_model.username))
        return super(Add_School_page,self).form_valid(form)
    
    def get_success_url(self):
        user_model=self.request.user
        user_pg=User_model.objects.get(user_of=user_model.pk)

        redir_url=f"new_user/profile_for_{user_model.username}/user{user_model.pk}_{user_model.username}/name_of/"+str(user_pg)
        return reverse("core:view_user_profile",kwargs={'user_x':user_model.username,'user_key':user_model.pk,'username':user_model.username,'profile_name':user_pg.name})
        #return HttpResponseRedirect(redir_url)


def schools_that_I_owne(h,user_key,user_x,profile_name,username):
    print("\nOWEND SCHOOLS INCLUDED\n")
    #filter is not for one to one model key
    main_user=User_model.objects.get(user_of=u_key)
    school_item=School_of_drive.objects.filter(owned_by=u_key)
    print("\n\nthe school of user "+str(main_user)+" is :\n"+str(school_item)+"\n\n")
    return render(h,"learn_center/list_all.html",{'school_owner':main_user,'schools':school_item,})



def schools_that_I_owne_with_item(h,user_key,user_x,profile_name,username,s_item):
    print("\nOWEND SCHOOLS Item\n")
    #filter is not for one to one model key
    main_user=User_model.objects.get(user_of=u_key)
    school_item=School_of_drive.objects.get(pk=s_item)
    print("\n\nthe school of user "+str(main_user)+" is :\n"+str(school_item)+"\n\n")
    return render(h,"learn_center/school_item.html",{'user_profile':main_user,'the_school_item':school_item,})




#for the obtained marks

def add_marks_that_I_deal_with(h,user_key,username,profile_name):
    marks_list=Mark_model.objects.all()
    dealed_marks=[]
    print(f"making the selected marks list for user {user_name}:{user_key} profile name {profile_name}.....")
    if h.method=='POST':
        print("post action applied")
        for d in range(len(marks_list)):
            dealed_marks.insert(d,marks_list[d])
            print("\n"+str(marks_list[d])+" inserted\n")

        print(f"\nadding to the dealed list\n{dealed_marks}\n")
        #return redirect()
        
        
    else:
        print("No post action applied")
    return render(h,"mark_owner/select_marks.html",{'all_marks':marks_list,'dealed_marks':dealed_marks})


def view_marks_that_I_deal_with(h,user_key,username,profile_name):
    print("\nOWEND MARKS INCLUDED\n")
    return render(h,"user_profile/model_1_mark_owner.html")



#for the obtained parts

class Add_Obtained_Parts_page(CreateView):
    model = Part_model
    form_class=Add_part_item_form
    template_name='car_parts/add_part.html'
    def get_context_data(self, **kwargs):
        context = super(Add_Obtained_Parts_page, self).get_context_data(**kwargs)
        get_user=self.kwargs['user_key']
        get_username=self.kwargs['user_name']
        get_profile=self.kwargs['profile_name']
        context['user_p']=self.kwargs['profile_name']
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\nmakeing an obtained parts for  user {get_user} profile {get_profile}\n")
        return context
    
    def form_valid(self, form: Add_part_item_form):
        user_x=self.request.user
        form.instance.owned_by=user_x
        return super(Add_Obtained_Parts_page,self).form_valid(form)


    def get_success_url(self):
        u_key=self.request.user.pk
        u_name=self.request.user.username
        get_profile=User_model.objects.get(user_of=u_key)
        print(f"\na driving school was created for {u_name} profile {get_profile}\n")
        return reverse("core:user_has_car_part",kwargs={'user_x':u_name,'user_key':user_key,'user_name':u_name,'profile_name':get_profile.name})
        #return f"user{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}"

def parts_that_i_have(h,user_x,user_key,username,profile_name):
    print("\nCAR PARTS INCLUDED\n")
    my_car_parts=Part_model.objects.filter(owned_by=user_key)
    profile_name_1=User_model.objects.get(user_of=user_key)
    return render(h,"car_parts/list.html",{'user_profile':profile_name_1,'my_parts':my_car_parts})




#for the Decore parts


class Add_Decore_Parts_page(CreateView):
    model = Decorator_model
    form_class=Add_decore_item_form
    template_name='decore/add_decore.html'
    success_url="?done_adding_decore_part"
    def get_context_data(self, **kwargs):
        context = super(Add_Decore_Parts_page, self).get_context_data(**kwargs)
        get_user=self.kwargs['user_key']
        #get_username=self.kwargs['user_name']
        #get_profile=self.kwargs['profile_name']
        print("USERS:"+str(User.objects.all()))
        get_profile=User_model.objects.get(user_of=get_user)
        print(f"\nmakeing a Decore parts for  user {get_user} profile {get_profile}\n")
        return context
    
    def form_valid(self, form:Add_part_item_form) -> HttpResponse:
        user_k=self.request.user
        form.instance.owned_by=user_k

        return super(Add_Decore_Parts_page,self).form_valid(form)
    
    


    def get_success_url(self):
        
        u_name=self.request.user.username
        u_key=self.request.user.pk
        get_profile=User_model.objects.get(user_of=u_key)
        return f'/'


def decore_i_have(h,user_x,user_key,username,profile_name):
    print("\nDECORE CARS displayer\n")
    owned_decores=Decorator_model.objects.filter(owned_by=user_key)
    return render(h,"decore/list.html",{'user_profile':profile_name,'owned_decores':owned_decores})

#for the petrol zones


class Add_Petrol_zone_page(CreateView):
    model = Petrol_area
    form_class=Add_Petrol_form
    template_name='petrol_zone/add_item.html'
    success_url='?done_add_petrol'
    def form_valid(self, form: Add_Petrol_form) -> HttpResponse:
        user_xp=self.request.user
        form.instance.owned_by=user_xp if user_xp else "Undefined"
        return super(Add_Petrol_zone_page,self).form_valid(form)
   
    
    
        #return f"new_user/profile_for_{self.request.user.username}/user{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}
    def get_success_url(self):
        x_ps=self.request.user.pk
        x_un=self.request.user.username
        profile_x=User_model.objects.get(user_of=x_ps)
        return f"/"

def petrol_owned(h,user_x,user_key,username,profile_name):
    print("\npetrol stations of "+str(username)+"\n")
    #re_petrols=request.user
    the_user=User_model.objects.get(user_of=user_key)
    all_petrols_of_x=User_model.objects.filter(name=profile_name,profile_activity='وقود')
    print(f"\nplay:{str(the_user.name)}\n")
    all_petrols=Petrol_area.objects.filter(owned_by=user_key)
    
    return render(h,"petrol_zone/list.html",{'profile_x_petrols':all_petrols_of_x,'petrols':all_petrols,'user_profile':the_user})



#for the Advetizer


class Add_adv_model(CreateView):
    model = Advertise_action
    template_name='hire_a_driver/add_item.html'
    form_class=Add_adv_form
    def get_context_data(self, **kwargs):
        context = super(Add_adv_model, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form: Add_adv_form):
        user_call=self.request.user
        form.instance.post_by=user_call
        return super(Add_adv_model,self).form_valid(form)



    def get_success_url(self):
        
        u_key=self.request.user.pk
        u_name=self.request.user.username
        get_profile=User_model.objects.get(user_of=u_key)
        return reverse("core:view_user_profile",kwargs={'user_x':u_name,'user_key':u_key,'username':u_name,'profile_name':get_profile.name})

def view_user_adv(h,user_x,user_key,username,profile_name,m_num,m_name):
    return render(h,'cars/view_car_adv_model.html')



class Update_adv_model(UpdateView):
    model = Advertise_action
    form_class=Add_adv_form
    template_name='hire_a_driver/update_item.html'

    def get_context_data(self, **kwargs):
        context = super(Update_adv_model, self).get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        u_key=self.request.user.pk
        u_name=self.request.user.username
        get_profile=User_model.objects.get(user_of=u_key)
        return reverse("core:view_user_profile",kwargs={'user_x':u_name,'user_key':u_key,'username':u_name,'profile_name':get_profile.name})






def adv_owned(h,user_x,user_key,username,profile_name):
    print("\nadv posters of "+str(profile_name)+":"+str(username)+"\n")
    #re_petrols=request.user
    all_posts=Advertise_action.objects.filter(post_by=user_key)
    profile_x=User_model.objects.get(user_of=user_key)
    return render(h,"hire_a_driver/list.html",{'user_profile':profile_x,'advs':all_posts})


def adv_owned_item(h,user_x,user_key,username,profile_name,a_item):
    print("\nan adv poster of "+str(username)+"\n")
    profile_x=User_model.objects.get(user_of=user_key)
    adv_item=Advertise_action.objects.get(pk=a_item)
    return render(h,"hire_a_driver/list_item.html",{'user_profile':profile_x,'adv_item':adv_item})


#ADD CAR MODEL
def list_marks(h,user_x,user_key,username,profile_name):
    user_f=User_model.objects.get(user_of=user_key)
    marks=Mark_model.objects.all()
    return render(h,"cars/list_marks.html",{'user_profile':user_f,'all_marks':marks})

class Add_a_car_model(CreateView):
    model = Car_model
    form_class=Add_Car_form
    template_name='add_a_car.html'
    def get_context_data(self, **kwargs):
        context = super(Add_a_car_model, self).get_context_data(**kwargs)
        return context
    def get_success_url(self):
        u_key=self.request.user.pk
        u_name=self.request.user.username
        get_profile=User_model.objects.get(user_of=u_key)
        return reverse("core:view_user_profile",kwargs={'user_x':u_name,'user_key':u_key,'username':u_name,'profile_name':get_profile.name})

def view_user_cars(h,user_x,user_key,username,profile_name,m_num,m_name):
    the_user=User_model.objects.get(user_of=user_key)
    the_cars=Car_model.objects.filter(family_of=m_num)
    print("\n\nuser "+str(user_key)+" who has the cars\n"+str(the_cars)+"\n\n")
    return render(h,'cars/view_car_models.html',{'user_profile':the_user,'user_cars':the_cars})

class Update_a_car_model(UpdateView):
    model = Car_model
    form_class=Add_Car_form
    template_name='add_a_car.html'
    pk_url_kwarg ='model_num'
    def get_success_url(self):
        u_key=self.request.user.pk
        u_name=self.request.user.username
        get_profile=User_model.objects.get(user_of=u_key)
        return reverse("core:view_user_profile",kwargs={'user_x':u_name,'user_key':u_key,'username':u_name,'profile_name':get_profile.name})


    



def E500(h):return render(h,"ex_list/e500.html")
def E400(h,ex):return render(h,"ex_list/e400.html")
def E404(h,ex):return render(h,"ex_list/e404.html",{'ex_list':ex})
def E403(h,ex):return render(h,"ex_list/e403.html",{'ex_list':ex})
def E405(h,ex):return render(h,"ex_list/e405.html",{'ex_list':ex})
