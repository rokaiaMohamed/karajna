from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Car, Version 
from django.utils.safestring import mark_safe


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='الاسم', error_messages={'min_length' : 'اقل قيمة للاسم اربع حروف','required' : 'هذه الخانة مطلوبة'}  ,min_length=4, max_length=150 ,widget=forms.TextInput(attrs={'class': "text form-control"}))
    email = forms.EmailField(label='البريد الالكترونى' , error_messages={'invalid' : 'قم بادخال بريد صالح' ,'required' : 'هذه الخانة مطلوبة'}  , widget=forms.TextInput(attrs={'class': "text email form-control"}))
    password1 = forms.CharField(label='الرقم السرى',min_length=8, error_messages={'min_length' : 'اقل قيمة للرقم السرى 8 احرف','required' : 'الرقم السرى مطلوب'},widget=forms.PasswordInput(attrs={'class': "text form-control"}))
    password2 = forms.CharField(label='تأكيد الرقم السرى' , error_messages={'required' : 'تأكيد الرقم السرى مطلوب'}, widget=forms.PasswordInput(attrs={'class': "text form-control"}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("الاسم موجود بالفعل")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("الايميل موجود بالفعل")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("الرقم السرى غير متطابق")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user 



class CarForm(forms.ModelForm):
   # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': 4}))
    class Meta:
        model = Car
        fields = ('brand' , 'version' , 'price' , 'distance' , 'external_color' , 'internal_color' , 'production_date' , 'basic_title' , 'extra_title' , 'seats_number' , 'guaranty' , 'motion_movement' , 'class_car' , 'payment_system' , 'car_body' , 'fuel_type' , 'engine_capacity' , 'cylinders' , 'doors_number' , 'refills_number' , 'hourses' , 'car_weight' , 'chrome_wheels','third_brake_light','airbag', 'side_airbags' ,'adjustable_rear_headrests' ,'adjustable_front_headrestraints' ,'help_braking','decorative_side_thresholds','adjustable_front_seatbelts','safety_belts',  'central_controller','enhanced_guidance','rear_fog_light','daytime_lights','isofix_child_seat','front_power_windows','rear_windows','heat_rear_glass','external_handles','drink_holder','radio_antennas_loudspeakers','seat_belts' ,'door_low_storage' , 'dashboard_store','exterior_mirrors' ,'exterior_mirrors_adjustable'  ,  'tire_repair_kit' , 'anti_lock_braking'  , 'immobilizer_system' ,  'central_locking','glove_box' , 'colorful_windows' ,'front_central_armrest' ,'roof_rails' , 'ashtrays_cigarette_lighters'  ,  'anti_slip_chains','conditioning' ,'back_sensitive' ,'seven_pin_ball_bearing_connector', 'trunk_network_separated','navigation_system' ,'computer','radio' ,'cd_mp3_player', 'backup_frame', 'front_seat_heating','steering_wheel_adjustable','abs_brakes' ,'sunroof' , 'image1', 'image2','image3','image4','image5','image6','image7', 'name' , 'business' , 'country' ,'phone_number' )
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].label =' الماركة * '
        self.fields['brand'].error_messages['required'] = 'هذه الخانة مطلوبة'

        self.fields['version'].label ='الموديل'
        self.fields['version'].required = False

        self.fields['price'].label ='السعر *'
        self.fields['price'].error_messages['required'] = 'هذه الخانة مطلوبة'
        self.fields['price'].error_messages['min_value'] = 'تأكد ان السعر اكبر من 0'
        self.fields['price'].error_messages['max_value'] = 'تأكد ان السعر اقل من 100000000 '

        self.fields['distance'].label ='عداد المسافة *'
        self.fields['distance'].error_messages['required'] = 'هذه الخانة مطلوبة'
        self.fields['distance'].error_messages['min_value'] = 'تأكد ان المسافة اكبر من 1'
        self.fields['distance'].error_messages['max_value'] = 'تأكد ان المسافة اقل من 1000000 '

        self.fields['external_color'].label ='اللون الخارجى *'
        self.fields['external_color'].error_messages['required'] = 'هذه الخانة مطلوبة'

        self.fields['internal_color'].label ='اللون الداخلى'
        self.fields['internal_color'].required = False

        self.fields['production_date'].label ='تاريخ الانتاج *'
        self.fields['production_date'].error_messages['required'] = 'هذه الخانة مطلوبة'

        self.fields['basic_title'].label ='العنوان الاساسى *'
        self.fields['basic_title'].error_messages['required'] = 'هذه الخانة مطلوبة'

        self.fields['extra_title'].label ='العنوان الاضافى'
        self.fields['extra_title'].required = False

        self.fields['seats_number'].label ='عدد المقاعد'
        self.fields['seats_number'].error_messages['min_value'] = 'تأكد ان المقاعد اكبر من 0 '
        self.fields['seats_number'].error_messages['max_value'] = 'تأكد ان المقاعد اقل من 48 '
        self.fields['seats_number'].required = False

        self.fields['guaranty'].label ='الكفالة '
        self.fields['guaranty'].required = False

        self.fields['motion_movement'].label ='ناقل الحركة'
        self.fields['motion_movement'].required = False

        self.fields['class_car'].label ='فئة السيارة *'
        self.fields['class_car'].error_messages['required'] = 'هذه الخانة مطلوبة'

        self.fields['payment_system'].label ='نظام الدفع'
        self.fields['payment_system'].required = False

        self.fields['car_body'].label ='بدن السيارة *'
        self.fields['car_body'].error_messages['required'] = 'هذه الخانة مطلوبة'

        self.fields['fuel_type'].label ='نوع الوقود'
        self.fields['fuel_type'].required = False

        self.fields['engine_capacity'].label ='سعة المحرك(cm3)'
        self.fields['engine_capacity'].required = False 
        self.fields['engine_capacity'].error_messages['min_value'] = 'تأكد ان سعة المحرك اكبر من 0'
        self.fields['engine_capacity'].error_messages['max_value'] = 'تأكد ان سعة المحرك اقل من 100000 '


        self.fields['cylinders'].label ='الاسطوانات'
        self.fields['cylinders'].required = False
        self.fields['cylinders'].error_messages['min_value'] = 'تأكد ان الاسطوانات اكبر من 0'
        self.fields['cylinders'].error_messages['max_value'] = 'تأكد ان الاسطوانات اقل من 36 '


        self.fields['doors_number'].label ='عدد الابواب' 
        self.fields['doors_number'].required = False
        self.fields['doors_number'].error_messages['min_value'] = 'تأكد ان عدد الابواب اكبر من 1'
        self.fields['doors_number'].error_messages['max_value'] = 'تأكد ان عدد الابواب اقل من 8 '


        self.fields['refills_number'].label ='عدد الغيارات'
        self.fields['refills_number'].required = False
        

        self.fields['hourses'].label ='الاحصنة'
        self.fields['hourses'].required = False
        self.fields['hourses'].error_messages['min_value'] = 'تأكد ان الاحصنة اكبر من 0'
        self.fields['hourses'].error_messages['max_value'] = 'تأكد ان الاحصنة اقل من 10000 '



        self.fields['car_weight'].label ='وزن السيارة فارغة(كجم)'
        self.fields['car_weight'].required = False
        self.fields['car_weight'].error_messages['min_value'] = 'تأكد ان وزن السيارة فارغة اكبر من 0'
        self.fields['car_weight'].error_messages['max_value'] = 'تأكد ان وزن السيارة فارغة اقل من 100000 '


        self.fields['chrome_wheels'].label ='عجلات كروم'
        self.fields['third_brake_light'].label =' ضوء الفرامل الثالث'
        self.fields['airbag'].label =' وسادة هوائية للسائق والراكب'
        self.fields['side_airbags'].label =' أكياس هواء جانبية للسائق والراكب'
        self.fields['adjustable_rear_headrests'].label =' مساند رأس خلفية قابلة للتعديل'
        self.fields['adjustable_front_headrestraints'].label =' مساند رأس أمامية قابلة للتعديل'
        self.fields['help_braking'].label =' مساعدة الكبح'
        self.fields['decorative_side_thresholds'].label =' العتبات الجانبية الزخرفية السوداء'
        self.fields['adjustable_front_seatbelts'].label ='  أحزمة امان امامية قابلة للتعديل في الارتفاع'
        self.fields['safety_belts'].label =' أحزمة أمان ثلاثية النقاط في جميع الأماكن'
        self.fields['central_controller'].label =' وحدة تحكم المركزية'
        self.fields['enhanced_guidance'].label =' التوجيه المعزز'
        self.fields['rear_fog_light'].label =' ضوء الضباب الخلفي'
        self.fields['daytime_lights'].label =' أضواء النهار'
        self.fields['isofix_child_seat'].label =' مرفق ISOFIX لمقعد الطفل'
        self.fields['front_power_windows'].label =' نوافذ كهربائية امامية'
        self.fields['rear_windows'].label =' نوافذ كهربائية خلفية'
        self.fields['heat_rear_glass'].label =' الزجاج الخلفية مسخن'
        self.fields['external_handles'].label ='  مقابض خارجية باللون الأسود'
        self.fields['drink_holder'].label =' حامل الشراب امامية'
        self.fields['radio_antennas_loudspeakers'].label =' معدات مسبقة للإذاعة والهوائي ومكبرات الصوت'
        self.fields['seat_belts'].label =' شدادات حزام الأمان'
        self.fields['door_low_storage'].label ='تخزين منخفض للباب'
        self.fields['dashboard_store'].label =' تخزين لوحة البيانات'
        self.fields['exterior_mirrors'].label =' المرايا الخارجية باللون الأسود'
        self.fields['exterior_mirrors_adjustable'].label =' مرايا خارجية قابلة للتعديل من الداخل'
        self.fields['tire_repair_kit'].label ='مجموعة إصلاح الإطارات (تناسب الإطارات)'
        self.fields['anti_lock_braking'].label =' نظام المكابح المانعة للانغلاق (ABS)'
        self.fields['immobilizer_system'].label =' نظام منع الحركة'
        self.fields['central_locking'].label ='قفل مركزي مع جهاز التحكم عن بعد'
        self.fields['glove_box'].label =' علبة القفازات'
        self.fields['colorful_windows'].label ='نوافذ ملون فيمه'
        self.fields['front_central_armrest'].label ='مسند الذراع المركزي الامامي'
        self.fields['roof_rails'].label =' قضبان السقف'
        self.fields['ashtrays_cigarette_lighters'].label =' مطافئ السجائر ولاعات السجائر '
        self.fields['anti_slip_chains'].label ='سلاسل مضادة للانزلاق' 
        self.fields['conditioning'].label ='تكييف'
        self.fields['back_sensitive'].label =' حساس رجوع'
        self.fields['seven_pin_ball_bearing_connector'].label ='أداة توصيل مع رأس كروي ثابت ذو 7 أقطاب'
        self.fields['trunk_network_separated'].label ='شبكة فصل في الجذع '
        self.fields['navigation_system'].label =' نظام الملاحة'
        self.fields['computer'].label ='كمبيوتر' 
        self.fields['radio'].label ='راديو'
        self.fields['cd_mp3_player'].label =' مشغل سي دي و MP3'
        self.fields['backup_frame'].label =' الإطار الاحتياطي '
        self.fields['front_seat_heating'].label =' تسخين المقاعد الأمامية'
        self.fields['steering_wheel_adjustable'].label =' عجلة قيادة قابلة للضبط'
        self.fields['abs_brakes'].label =' فرامل ABS'
        self.fields['sunroof'].label =' فتحة السقف'

        self.fields['image1'].label ='الصورة الاولى'
        self.fields['image1'].error_messages['required'] = 'هذه الخانة مطلوبة'
        self.fields['image1'].error_messages['invalid_image'] = 'قم بتحميل صورة صالحة'

        self.fields['image2'].label =' الصورة الثانية'
        self.fields['image2'].required = False
        self.fields['image2'].error_messages['invalid_image'] = 'قم بتحميل صورة صالحة'

        self.fields['image3'].label ='الصورة الثالثة'
        self.fields['image3'].required = False
        self.fields['image3'].error_messages['invalid_image'] = 'قم بتحميل صورة صالحة'

        self.fields['image4'].label ='الصورة الرابعة'
        self.fields['image4'].required = False
        self.fields['image4'].error_messages['invalid_image'] = 'قم بتحميل صورة صالحة'

        self.fields['image5'].label ='الصورة الخامسة'
        self.fields['image5'].required = False
        self.fields['image5'].error_messages['invalid_image'] = 'قم بتحميل صورة صالحة'

        self.fields['image6'].label ='الصورة السادسة'
        self.fields['image6'].required = False
        self.fields['image6'].error_messages['invalid_image'] = 'قم بتحميل صورة صالحة'

        self.fields['image7'].label ='الصورة السابعة'
        self.fields['image7'].required = False
        self.fields['image7'].error_messages['invalid_image'] = 'قم بتحميل صورة صالحة'

        self.fields['name'].label =' الاسم '
        self.fields['name'].error_messages['required'] = 'هذه الخانة مطلوبة'
        self.fields['business'].label ='مجال العمل '
        self.fields['business'].error_messages['required'] = 'هذه الخانة مطلوبة'
        self.fields['country'].label =' الدولة'
        self.fields['country'].error_messages['required'] = 'هذه الخانة مطلوبة'
        self.fields['phone_number'].label =' رقم التليفون'
        self.fields['phone_number'].error_messages['required'] = 'هذه الخانة مطلوبة'

        self.fields['version'].queryset = Version.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['version'].queryset = Version.objects.filter(brand_id=brand_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['version'].queryset = self.instance.brand.version_set.order_by('name')


         

   
                                                                                                               
                                                                                                                                                
