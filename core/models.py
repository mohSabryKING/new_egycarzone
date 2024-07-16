from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField,Country
from django_countries import countries
import datetime
from django.utils.html import format_html
from django.urls import reverse

# Create your models here.
User_activity=[
      ('وكيل ماركة','وكيل ماركة'),
      ('مركز صيانة','مركز صيانة'),
      ('محل قطع غيار','محل قطع غيار'),
      
      ('إيجار','إيجار'),
      ('وقود','وقود'),
      ('بيع-إيجار-شراء','بيع-إيجار-شراء'),
      ('أكسسوارت','أكسسوارت'),
      ('مركز تدريب','مركز تدريب'),
      ('عميل','عميل'),
]

Rate=[
      ('STAR1','STAR1'),
      ('STAR2','STAR2'),
      ('STAR3','STAR3'),
      ('STAR4','STAR4'),
      ('STAR5','STAR5'),
      
      ]

Part_type=[('داخلية','داخلية'),
           ('خارجية','خارجية'),
           ('اكسسوار','اكسسوار')
           ]

Cat_type=[('ماركة سيارات','ماركة سيارات'),
           ('قطع غيار','قطع غيار'),
           ('اكسسوار','اكسسوار')
           ]


topic='''
Provident nihil minus qui consequatur non omnis maiores. Eos accusantium minus dolores iure perferendis tempore et consequatur.
                   
'''


Locat_x='https://maps.app.goo.gl/Ba5yubWZUc811PVg7'


#LAST ITEM TO BE USED
class User_model(models.Model):
      #'user_of','has_mark','has_model','has_part','has_school','Position_found','name','profile_activity','user_phone','location_branch','rate_lvl'
      user_of = models.OneToOneField(User,related_name='r_has_profile_x',verbose_name='for user', on_delete=models.CASCADE)
      ''' has_mark = models.ForeignKey(Mark_model, related_name='r_has_car', on_delete=models.CASCADE, blank=True, null=True)
      has_model = models.ForeignKey(Car_model, related_name='r_has_model', on_delete=models.CASCADE, blank=True, null=True)
      has_part = models.ForeignKey(Part_model, related_name='r_has_part', on_delete=models.CASCADE, blank=True, null=True)
      has_deco = models.ForeignKey(Decorator_model, related_name='r_has_decor', on_delete=models.CASCADE, blank=True, null=True)
      has_school = models.ForeignKey(School_of_drive, related_name='r_has_school', on_delete=models.CASCADE, blank=True, null=True)
      has_petrol = models.ForeignKey(Petrol_area, related_name='r_has_petrol', on_delete=models.CASCADE, blank=True, null=True)
      '''
      has_what=''
      
      name = models.CharField(max_length=40, blank=True, null=True,default="Eltyyar Cars",verbose_name="اسم المحل")
      address= models.CharField(max_length=40, blank=True, null=True,default="م33محل الغربالي",verbose_name="العنوان")
      user_img = models.ImageField(upload_to="user_named", height_field=None, width_field=None, max_length=100,default='car_part2.png')
      profile_activity = models.CharField(max_length=23,verbose_name='نوع النشاط',choices=User_activity,default=User_activity[6])
      user_phone=PhoneNumberField(blank=False)
      location_branch = models.URLField(max_length = 200,default=Locat_x)
      #rate_lvl = models.CharField(max_length = 6,verbose_name='التقييم',choices=Rate,default=Rate[4])
      
      #User.is_authenticated
      

      def __str__(self):
            return self.name
      def img_view(self):
           return format_html(f"<div style='width: 20%;height: 20%;display: grid;justify-self: center;'><img src='{self.user_img.url}' alt='' style='border: 3px solid red;border-radius: 50%;' class='user_model'></div>")
      def Position_found(self):
            
            if self.profile_activity==User_activity[0]:
                 self.has_what='وكيل ماركة'
            elif self.profile_activity==User_activity[1]:self.has_what='مركز صيانة'
            elif self.profile_activity==User_activity[2]:self.has_what='محل قطع غيار'
            elif self.profile_activity==User_activity[3]:self.has_what='إيجار'
            elif self.profile_activity==User_activity[4]:self.has_what='وقود'
            elif self.profile_activity==User_activity[5]:self.has_what='شراء'
            elif self.profile_activity==User_activity[6]:self.has_what='أكسسوارت'
            elif self.profile_activity==User_activity[7]:self.has_what='بيع-إيجار-شراء'
            else:self.has_what='مركز تدريب'
            return self.has_what
      
      def location_as_live(self):
            return format_html(f"<iframe src='{self.location_branch}' width='600px' height='450px' style='border:0px;' allowfullscreen='yes' loading='lazy' referrerpolicy='no-referrer-when-downgrade'></iframe>")
      
      '''def get_absolute_url(self):
        return reverse("core:make_user_profile",kwargs={'user_x':self.user_of})'''
      

      def get_absolute_url(self):pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'User_model'
            verbose_name_plural = 'User_model'





class Advertise_action(models.Model):
      #'post_by','adv_poster','name','bio'
      post_by= models.ForeignKey(User,null=True,blank=True, related_name='user_posts_adv_x', on_delete=models.CASCADE)
      adv_poster = models.ImageField(upload_to="صوره الاعلان", height_field=None, width_field=None, max_length=100,default='hire_1.jpg')
      name = models.CharField(max_length=55,default="BYD",verbose_name="العنوان")
      adv_cost= models.DecimalField(verbose_name='سعر الأعلان\الإيجار',max_digits=10, decimal_places=2,default=1250)
      location_branch = models.URLField(max_length = 200,default=Locat_x,verbose_name='رابط الأعلان',null=True,blank=True)
      bio = models.TextField(default=topic,null=True,blank=True,verbose_name="details",max_length=150)
      posted_in = models.DateTimeField(auto_now=True)
      

      

      def __str__(self):return "Advertise Num "+str(self.pk)

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Advertise_action'
            verbose_name_plural = 'Advertise_action'




class Mark_model(models.Model):
      #'name','m_logo','country_made','bio'
      name = models.CharField(max_length=15,default="BYD",verbose_name="mark name")
      m_logo = models.ImageField(upload_to="marks", height_field=None, width_field=None, max_length=100,default='byd.jpg')
      cat_type_field = models.CharField(max_length=15,verbose_name='نوع الماركة',default=Cat_type[0],null=True,blank=True,choices=Cat_type)
      country_made=  models.CharField(max_length=50,  null=True, choices=CountryField().choices + [(CountryField().name, 'Select Country')])
      #country_made=CountryField(verbose_name="made from")
      bio = models.TextField(default=topic,null=True,blank=True,verbose_name="details")
      
      

      def __str__(self):
            return str(self.name)
      
      def get_absolute_url(self):
        return f"/Marks_of_{self.pk}-{self.name}"
      
      def country_made_name(self):
           
           return str(Country(code=self.country_made).name)
      
      def print_model_1(self):
           output_model=f''' 
<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-app" style="width:100% !important;">
                            <img src="{self.m_logo.url}" class="img-fluid" width="256px" height="128px" style='width:90%;height:256px;margin:0% 1%;' alt="">
                            <div class="portfolio-info">
                                <h4>{self.name}</h4>
                                <a href="{self.m_logo.url}" title="App 1" data-gallery="portfolio-gallery-app" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
                                <a href="portfolio-details.html" title="More Details" class="details-link"><i class="bi bi-link-45deg"></i></a>
                            </div>
                        </div>
                        
 '''
           return format_html(output_model)
      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Mark_model'
            verbose_name_plural = 'Mark_models'



class Car_model(models.Model):
      owned_by = models.ForeignKey(Mark_model, on_delete=models.CASCADE,null=True,blank=True,verbose_name='من فئة',related_name='belongs_to')
      
      family_of = models.ForeignKey(Mark_model, related_name='family_of', on_delete=models.CASCADE,null=True,blank=True,)
      name = models.CharField(max_length=15,default="Zekolns_1",verbose_name="mark name")
      date_of_made = models.DateField(auto_now=False, auto_now_add=False,verbose_name='date of Model',default=datetime.date(2022, 1,5))
      m_img = models.ImageField(upload_to="marks_models/", height_field=None, width_field=None, max_length=100,default='car_11.jpg')
      
      speed_km = models.PositiveIntegerField(verbose_name="speed with (KM)",default=120)
      engine_capacity  = models.DecimalField(verbose_name='engine capacity (CC)',max_digits=3, decimal_places=2,default=3.5)
      weight = models.DecimalField(verbose_name='car weight(TON)',max_digits=3, decimal_places=2,default=5.5)
      price  = models.DecimalField(verbose_name='price(EGP)',max_digits=10, decimal_places=2,default=250000)
      bio = models.TextField(default=topic,null=True,blank=True,verbose_name="details")

      
      
      def weight_kg(self):return str(self.weight*1000)+" Kg"
      def price_model(self):return str(self.price/1000)+"K EGP"

      def model_of_year(self):return str(self.date_of_made.year)
      def get_absolute_url(self):
        play= "Marks_of_<int:k>-<str:name>/model_num<int:model_num>"
        return f"/Marks_of_{self.family_of.pk}-{self.family_of.name}/model_name_{self.name}:{self.pk}"

      def __str__(self):
            return self.name
      def print_model_1(self):
           output_model=f'''
                    <div class="col-lg-4 col-md-6" data-aos="fade-up" data-aos-delay="100">
                        <img src="{self.m_img.url}" class="img-fluid"  style='width:90%;height:50%;margin:0% 1%;' alt="">
                            <div class="portfolio-info">
                                <h4>Model name:{self.name}</h4>
                                <li>Weight in Kg:{self.weight_kg}</li>
                                <li>Price in EGP:{self.price} EGP</li>
                                <li><a href='{self.get_absolute_url}' class='read-more'>Explor more</a></li>
                                <a href="{self.m_img.url}" title="App 1" data-gallery="portfolio-gallery-app" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
                                <a href="portfolio-details.html" title="More Details" class="details-link"><i class="bi bi-link-45deg"></i></a>
                            </div>
                    </div>
'''
           return format_html(output_model)

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Car_model'
            verbose_name_plural = 'Car_model'



class Part_model(models.Model):
      #'owned_by','belong_to_mark','belong_to_model','name','type','part_img','price','bio'
      owned_by= models.ForeignKey(User, related_name='user_has_part_x', on_delete=models.CASCADE,null=True,blank=True)
      belong_to_mark = models.ForeignKey(Mark_model, related_name='a_part_from_mark_x',null=True,blank=True, on_delete=models.CASCADE)
      belong_to_model = models.ForeignKey(Car_model, related_name='a_part_from_model_y',null=True,blank=True, on_delete=models.CASCADE)
      name = models.CharField(max_length=15,default="Cylinder",verbose_name="mark name")
      #type = models.CharField(max_length=13,verbose_name='النوع',choices=Part_type,default=Part_type[2])
     
      part_img = models.ImageField(upload_to="marks", height_field=None, width_field=None, max_length=100,default='car_part3.png')
      price  = models.DecimalField(verbose_name='price(EGP)',max_digits=10, decimal_places=2,default=1250)
      bio = models.TextField(default=topic,null=True,blank=True,verbose_name="details")
      added_in = models.DateTimeField(auto_now_add=True)


      def get_absolute_url(self):
        if self.belong_to_mark and self.belong_to_model:
             return f"/{self.belong_to_mark}/{self.belong_to_model}/{self.name}/"
        else:return f"/{self.name}/"
      

      def __str__(self):return self.name

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Part_model'
            verbose_name_plural = 'Part_model'




class Fix_action(models.Model):
      owned_by= models.OneToOneField(User,null=True,blank=True, related_name='user_fix_x', on_delete=models.CASCADE)
      bio = models.TextField(default=topic,null=True,blank=True,verbose_name="details")
      

      def __str__(self):
            pass

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Fix_action'
            verbose_name_plural = 'Fix_actions'






class Decorator_model(models.Model):
      owned_by= models.ForeignKey(User, related_name='user_has_deco_part_x', on_delete=models.CASCADE,null=True,blank=True)
      
      name = models.CharField(max_length=15,default="bulb funy",verbose_name="deco name")
      type = models.CharField(max_length=13,verbose_name='النوع',choices=Part_type,default=Part_type[2])
     
      part_img = models.ImageField(upload_to="decorators", height_field=None, width_field=None,max_length=100,null=True,blank=True,default="decorators/car_decorations_5.jpg")
      price  = models.DecimalField(verbose_name='price(EGP)',max_digits=10, decimal_places=2,default=250)
      bio = models.TextField(default=topic,null=True,blank=True,verbose_name="details")
      added_in = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name
      
      def view_decore_model(self):
           if self.part_img:
             return format_html(f"<figure style='width: 100%;display:block;justify-self:center;'><img src='{self.part_img.url}' width='250px'' height='250px' alt='{self.part_img.url}' /></figure>")
           else:
                return format_html(f"<h1>No image to display</h1>")
      
      def view_decore_model_1(self):
            try:
             pass_x=format_html(f"<figure style='width: 100%;'><img src='{self.part_img.url}' width='100%'' height='250px' alt='{self.part_img.url}' /></figure>")
            except:
             pass_x=format_html(f"<h1>No image to display ERR</h1>")
            return pass_x
      
      def view_decore_model_2(self):
           if self.part_img:
                return self.part_img.url
           else:
                return 'Image in Media FALL'
      
      
      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Decorator_model'
            verbose_name_plural = 'Decorator_model'



#Added by SUPERUSER
class Drive_News(models.Model):
      name = models.CharField(max_length=30, blank=True, null=True,verbose_name="school name",default="El-nomrous")
      user_img = models.ImageField(upload_to='news_area/', height_field=None, width_field=None, max_length=100)
      
      added_in = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            pass

      def get_absolute_url(self):
        return f"/{self.name}/"

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Drive_News'
            verbose_name_plural = 'Drive_News'


'''
كنابة تقرير لحظي لعملية الاستهلاك
'''

class Petrol_area(models.Model):
      owned_by= models.ForeignKey(User, blank=True, null=True, related_name='user_has_petrol_x',on_delete=models.CASCADE)
      location_branch = models.URLField(max_length = 200,default=Locat_x)
      address= models.CharField(max_length=40, blank=True, null=True,default="م33محل الغربالي",verbose_name="العنوان")
      
      name = models.CharField(max_length=30, blank=True, null=True,verbose_name="petrol name",default="Petrojet EGY")
      f95  = models.DecimalField(verbose_name='f95 obtained(LE):',max_digits=10, decimal_places=2,default=100.51)
      f95_cost  = models.DecimalField(verbose_name='f95 price(EGP)',max_digits=10, decimal_places=2,default=250)
      f92  = models.DecimalField(verbose_name='f92 obtained(LE):',max_digits=10, decimal_places=2,default=25.20)
      f92_cost  = models.DecimalField(verbose_name='f92 price(EGP)',max_digits=10, decimal_places=2,default=250)
      f90  = models.DecimalField(verbose_name='f90 obtained(LE):',max_digits=10, decimal_places=2,default=300.5)
      f90_cost  = models.DecimalField(verbose_name='f90 price(EGP)',max_digits=10, decimal_places=2,default=250)
      f80  = models.DecimalField(verbose_name='f80 obtained(LE):',max_digits=10, decimal_places=2,default=50.6)
      f80_cost  = models.DecimalField(verbose_name='f80 price(EGP)',max_digits=10, decimal_places=2,default=250)
      
      

      def __str__(self):
            return str(self.owned_by.pk)
      
      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'Petrol_area'
            verbose_name_plural = 'Petrol_area'







class School_of_drive(models.Model):
      owned_by= models.ForeignKey(User, related_name='user_has_school_x', blank=True, null=True, on_delete=models.CASCADE)
      
      name = models.CharField(max_length=30, blank=True, null=True,verbose_name="school name",default="El-nomrous Driving")
      
      bio = models.TextField(default=topic,null=True,blank=True,verbose_name="details")
      added_in = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.name

      class Meta:
            db_table = ''
            managed = True
            verbose_name = 'School of drive'
            verbose_name_plural = 'School of drive'
      