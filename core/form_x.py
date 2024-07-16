from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Make_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')
        widgets={}

class Make_profile_form(forms.ModelForm):
    class Meta:
        model = User_model
        #'user_of','has_mark','has_model','has_part','has_school','Position_found','name','profile_activity','user_phone','location_branch','rate_lvl'
     
        fields = ('user_of',
                  
                  'user_img',
                  'name',
                  'profile_activity',
                  'user_phone',
                  'location_branch',
                  'address')
        widgets={
            
        '''    'has_mark':forms.HiddenInput(),
            'has_model':forms.HiddenInput(),
            'has_part':forms.HiddenInput(),
            'has_deco':forms.HiddenInput(),
            'has_petrol':forms.HiddenInput(),
            'has_school':forms.HiddenInput(),
            '''
#has_school,has_petrol

        }
        exclude = ['user_of']



#User.is_authenticated

class Add_School_form(forms.ModelForm):
    class Meta:
        model = School_of_drive
        fields = ('owned_by','name','bio')
        widgets={
            'owned_by':forms.HiddenInput(),
        }


class Add_part_item_form(forms.ModelForm):
    #NOTE:قطع غيار اساسية ولا أكسسوارت
    class Meta:
        model = Part_model
        fields = ('owned_by','belong_to_mark','belong_to_model','name','part_img','price','bio')
        widgets={'owned_by':forms.HiddenInput()}


class Add_decore_item_form(forms.ModelForm):
    #NOTE:قطع غيار اساسية ولا أكسسوارت
    class Meta:
        model = Decorator_model
        fields = ('owned_by','name','type','part_img','price','bio',)
        widgets={'owned_by':forms.HiddenInput(),}



class Add_Petrol_form(forms.ModelForm):
    #NOTE:قطع غيار اساسية ولا أكسسوارت
    class Meta:
        model = Petrol_area
        fields = ('owned_by','name','address','location_branch','f95_cost','f95','f92_cost','f92','f90_cost','f90','f80_cost','f80')
        widgets={'owned_by':forms.HiddenInput(),}




class Add_adv_form(forms.ModelForm):
    class Meta:
        model = Advertise_action
        fields = ('post_by','adv_poster','name','bio')
        widgets={'post_by':forms.HiddenInput()}



class Add_Car_form(forms.ModelForm):
    class Meta:
        model = Car_model
        fields = ('owned_by','family_of','name','date_of_made','m_img','speed_km','engine_capacity','weight','price','bio')
        
        widgets={'owned_by':forms.HiddenInput(),}




class Add_Fixing_information_form(forms.ModelForm):
    class Meta:
        model = Fix_action
        fields = ('owned_by','bio')
        
        widgets={'owned_by':forms.HiddenInput(),}