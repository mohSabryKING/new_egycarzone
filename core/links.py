from django.urls import *
from .views import *
from .models import *
from django.contrib.auth import views as log_x

app_name='core'
#url = reverse("core:marks")
urlpatterns = [
      path('login',log_x.LoginView.as_view(template_name='registration/login.html'),name='login'),
      path('logout/',log_x.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
      
      path('',Menu.as_view(),name='home'),
      #path('confirmed',,name=),
      path('new_user',Add_user_page.as_view(),name='add_user'),
      path('new_user/profile_for_<str:user_x>/make_profile',Make_profile_page.as_view(),name='make_user_profile'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>',display_profile,name='view_user_profile'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/browse_<str:sec_x>/more_about_user_<int:id_profile>',display_x_profile,name='view_x_profile'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/browse_<str:sec_x>/more_about_user_<int:id_profile>/pertol_<int:petrol_id>',deep_petrol_dit,name='petrol_x_data'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/browse_<str:sec_x>',all_sec_of_x,name='sector_x'), 






      #----------------TEST--------------\
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/add_petrol',Add_Petrol_zone_page.as_view(),name='user_add_petrol'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/',petrol_owned,name='user_has_petrols'),
      #----------------------------------/
      #----------------TEST--------------\
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/add_car_decore_part',Add_Decore_Parts_page.as_view(),name='user_add_car_decore'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/view_owner_decores',decore_i_have,name='user_has_car_decore'),
      #----------------------------------/
      #----------------TEST--------------\
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/add_your_car_parts',Add_Obtained_Parts_page.as_view(),name='user_add_car_part'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/view_owner_car_parts',parts_that_i_have,name='user_has_car_part'),
      #path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/view_owner_car_parts',parts_that_i_have,name='user_has_car_part'),
      #----------------------------------/
      
      #----------------TEST--------------\
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/add_marks_that_u_manage',add_marks_that_I_deal_with,name='user_add_managed_marks'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/view_managed_marks',view_marks_that_I_deal_with,name='user_has_managed_marks'),
      #----------------------------------/
      #user{self.request.user.pk}_{self.request.user.username}/name_of/{get_profile.user_of}_petrol_zone
      # path("user<int:user_key>_<str:username>/name_of/<str:profile_name>",has_a_fix_center,name='user_has_fix_center'),
      #------------------------------
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/add_school',Add_School_page.as_view(),name='user_add_school'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/my_schools',schools_that_I_owne,name='user_displays_school'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/my_schools/<int:s_item>school',schools_that_I_owne_with_item,name='school_item'),


      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/all_marks',list_marks,name='list_marks'),
      
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/all_marks/add_an_adv_for_mark_<int:m_num>_<str:m_name>',Add_adv_model.as_view(),name='user_add_car_adv'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/all_marks/view_adv_for_mark_<int:m_num>_<str:m_name>',view_user_adv,name='user_view_car_adv'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/all_marks/view_adv_for_mark_<int:m_num>_<str:m_name>/update',Update_adv_model.as_view(),name='user_change_car_adv'),
      
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/all_marks/add_a_Car_<int:m_num>_<str:m_name>',Add_a_car_model.as_view(),name='user_add_car'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/all_marks/view_Car_<int:m_num>_<str:m_name>',view_user_cars,name='user_view_car'),

      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/all_marks/view_Car_<int:m_num>_<str:m_name>/update_<int:model_num>_',Update_a_car_model.as_view(),name='user_change_car'),

      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/view_my_ads',adv_owned,name='user_has_car_adv'),
      path('new_user/profile_for_<str:user_x>/user<int:user_key>_<str:username>/name_of/<str:profile_name>/view_my_ads/adv_num_<int:a_item>',adv_owned_item,name='adv_item'),

























      path('Marks',all_marks,name='marks'),
      path('Marks_of_<int:k>-<str:mark_name>',mark_models,name='mark_item'),
      path('Marks_of_<int:k>-<str:mark_name>/model_name_<str:model_name>:<int:model_num>',model_details,name='dit_item'),
    
]