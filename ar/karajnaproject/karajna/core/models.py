from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User , Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator , MaxValueValidator
import os
from django.conf import settings
#from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Version(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE )
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Range(models.Model):
    begin_int = models.IntegerField()
    end_int = models.IntegerField()
    
    def __str__(self):
        return self.begin_int

 

class Car(models.Model):

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    COLOR_CHOICES = (('أسود', 'اسود'),('أصفر', 'اصفر'),('رمادى', 'رمادى'),('بنى', 'بنى'),('أبيض', 'ابيض'),('أزرق', 'ازرق'),('أحمر', 'احمر'),('بمبى', 'بمبى'),('بيج', 'بيج'),('فيروزى', 'فيروزى'),('موف', 'موف'),('أخضر', 'اخضر'),('متعدد اﻷلوان', 'متعدد اﻷلوان'),('برتقالى', 'برتقالى'),('ذهبى', 'ذهبى'),)
    MOTION_CHOICES = (('أوتوماتيك', 'اوتوماتيك'),('يدوى', 'يدوى'),)
    CLASS_CHOICES = (('مستعمل', 'مستعمل'),('جديد', 'جديد'),)
    PAYMENT_CHOICES = (('أمامى', 'امامى'),('خلفى', 'خلفى'),)
    BODY_CHOICES = (('ميني', 'ميني'),('هتشباك', 'هتشباك'),('سيدان', 'سيدان'),('استيشن', 'استيشن'),('مترفة', 'مترفة'),('كشف', 'كشف'),(' SUV', 'SUV'),('كوبيه', 'كوبيه'),('فان', 'فان'),('بيك أب', 'بيك أب'),('رياضية', 'رياضية'),)
    FUEL_CHOICES = (('بنزين', 'بنزين'),('مازوت', 'مازوت'),)
    REFILLS_CHOICES = [(i,i) for i in range(1 , 13)]
    DATE_CHOICES = [(i,i) for i in range(1985 , 2020)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #group = models.ForeignKey(Group, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    version = models.ForeignKey(Version, on_delete=models.SET_NULL, null=True )
    price = models.IntegerField(default=0,validators=[ MaxValueValidator(100000000),MinValueValidator(0)])
    distance = models.IntegerField(default=0,validators=[ MaxValueValidator(1000000),MinValueValidator(1)])
    external_color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    internal_color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    production_date = models.IntegerField( choices=DATE_CHOICES)
    basic_title=models.TextField(max_length=25)
    extra_title=models.TextField(max_length=50)
    seats_number=models.IntegerField(default=0,validators=[MaxValueValidator(48), MinValueValidator(0)])
    guaranty=models.TextField(max_length=50)
    motion_movement = models.CharField(max_length=10, choices=MOTION_CHOICES)
    class_car = models.CharField(max_length=10, choices=CLASS_CHOICES)    
    payment_system = models.CharField(max_length=10, choices=PAYMENT_CHOICES)    
    car_body = models.CharField(max_length=10, choices=BODY_CHOICES)
    #technical information 
    fuel_type= models.CharField(max_length=10 , choices=FUEL_CHOICES)
    engine_capacity= models.IntegerField(default=0,validators=[ MaxValueValidator(100000),MinValueValidator(0)])
    cylinders= models.IntegerField(default=0,validators=[ MaxValueValidator(36),MinValueValidator(0)])
    doors_number= models.IntegerField(default=0,validators=[MaxValueValidator(8), MinValueValidator(1)])
    refills_number= models.IntegerField( choices=REFILLS_CHOICES)
    hourses= models.IntegerField(default=0,validators=[MaxValueValidator(10000), MinValueValidator(0)])
    car_weight= models.IntegerField(default=0,validators=[MaxValueValidator(100000), MinValueValidator(0)])
   # comfortable mean
    chrome_wheels= models.BooleanField(default=True)
    third_brake_light= models.BooleanField(default=True)
    airbag= models.BooleanField(default=True)
    side_airbags= models.BooleanField(default=True)
    adjustable_rear_headrests= models.BooleanField(default=True)
    adjustable_front_headrestraints= models.BooleanField(default=True)
    help_braking= models.BooleanField(default=True)
    decorative_side_thresholds= models.BooleanField(default=True)
    adjustable_front_seatbelts= models.BooleanField(default=True)
    safety_belts= models.BooleanField(default=True)
    central_controller= models.BooleanField(default=True)
    enhanced_guidance= models.BooleanField(default=True)
    rear_fog_light= models.BooleanField(default=True)
    daytime_lights= models.BooleanField(default=True)
    isofix_child_seat= models.BooleanField(default=True)
    front_power_windows= models.BooleanField(default=True)
    rear_windows= models.BooleanField(default=True)
    heat_rear_glass= models.BooleanField(default=True)
    external_handles= models.BooleanField(default=True)
    drink_holder= models.BooleanField(default=True)
    radio_antennas_loudspeakers= models.BooleanField(default=True)
    seat_belts = models.BooleanField(default=True)
    door_low_storage = models.BooleanField(default=True)
    dashboard_store= models.BooleanField(default=True)
    exterior_mirrors = models.BooleanField(default=True)
    exterior_mirrors_adjustable= models.BooleanField(default=True)
    tire_repair_kit= models.BooleanField(default=True)
    anti_lock_braking = models.BooleanField(default=True)
    immobilizer_system= models.BooleanField(default=True)
    central_locking= models.BooleanField(default=True)
    glove_box= models.BooleanField(default=True)
    colorful_windows= models.BooleanField(default=True)
    front_central_armrest= models.BooleanField(default=True)
    roof_rails= models.BooleanField(default=True)
    ashtrays_cigarette_lighters= models.BooleanField(default=True)
    anti_slip_chains= models.BooleanField(default=True)
    conditioning= models.BooleanField(default=True)
    back_sensitive= models.BooleanField(default=True)
    seven_pin_ball_bearing_connector= models.BooleanField(default=True)
    trunk_network_separated= models.BooleanField(default=True)
    navigation_system= models.BooleanField(default=True)
    computer= models.BooleanField(default=True)
    radio= models.BooleanField(default=True)
    cd_mp3_player= models.BooleanField(default=True)
    backup_frame= models.BooleanField(default=True)
    front_seat_heating= models.BooleanField(default=True)
    steering_wheel_adjustable= models.BooleanField(default=True)
    abs_brakes= models.BooleanField(default=True)
    sunroof= models.BooleanField(default=True)
    #image upload
    #image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg' , validators=[validate_image])
    image1 = models.ImageField(upload_to='pic_folder/')
    image2 = models.ImageField(upload_to='pic_folder/')
    image3 = models.ImageField(upload_to='pic_folder/')
    image4 = models.ImageField(upload_to='pic_folder/')
    image5 = models.ImageField(upload_to='pic_folder/')
    image6 = models.ImageField(upload_to='pic_folder/')
    image7 = models.ImageField(upload_to='pic_folder/')
    #extra information 
    name = models.CharField(max_length=30)
    business = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.brand.name

    


