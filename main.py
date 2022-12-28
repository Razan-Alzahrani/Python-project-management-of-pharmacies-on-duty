# من مكتبة tkinter استدعي لي كل الدوال
from tkinter import *
# مكتبه للتعامل مع خريطة قوقل
from tkintermapview import TkinterMapView

# TK كلاس جاهز او نافذه جاهزه داخل مكتبة tkinter
#لمن اسند كلاس داخل متغير هذا مايسمى بالاوبجكت في لغة البايثون 
root = Tk()
# اعدل الان الطول والعرض تبع النافذه عن طريق دالة .geometry( العرضxالطول)
root.geometry('880x450')
# بعدين نعدل على اسم البرنامج عن طريق داله .title()
root.title('Razan[الصيدليات المناوبة]')
# نضيف ايقونه جنب اسم البرنامج بدالة .iconbitmap(اسم ملف الصوره)
root.iconbitmap('images.ico')
# اعدل الخلفيه عن طريقة دالة التحكم بالخصائص .configure()
root.configure(background='white')



# اعمل دالة جديده علشان لمن اضغط على زر صيدليه مركزيه مثلا تطلع لي كل الصيدليات فالمنطقه 
def markazi():
    map = TkinterMapView (root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=40)
    # السطر 25 مايشتغل علشان كذا خليتو تعليق لكن هو المفروض يكون جزء من البرنامج
    # map.set_tile_server("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d475322.6559024308!2d39.49134090897901!3d21.45052894054877!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x15c3d01fb1137e59%3A0xe059579737b118db!2z2KzYr9ip!5e0!3m2!1sar!2ssa!4v1672225917807!5m2!1sar!2ssa",max_zoom=22)
    #  خطوط الطول والعرض نروح لقوقل ماب ونكتب صيديله مركزيه بعدين كلك يمين وننسخ الاحداثيات
    map.set_position(33.52108472669002, 36.296695905181544)
    map.set_zoom(15)
    marker = map.set_marker(33.52108472669002, 36.296695905181544)
    marker.set_text('Razan[صيدليه مركزيه]')

# اعمل دالة جديده علشان لمن اضغط على زر صيدليه مزرعه مثلا تطلع لي كل الصيدليات فالمنطقه بعدين انزل اضيفها ع الزر تحت 
def mazraa():
    map = TkinterMapView (root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=40)
    map.set_tile_server("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d475322.6559024308!2d39.49134090897901!3d21.45052894054877!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x15c3d01fb1137e59%3A0xe059579737b118db!2z2KzYr9ip!5e0!3m2!1sar!2ssa!4v1672225917807!5m2!1sar!2ssa",max_zoom=22)
    #  خطوط الطول والعرض نروح لقوقل ماب ونكتب صيديله مركزيه بعدين كلك يمين وننسخ الاحداثيات
    map.set_position(33.52322419997178, 36.29292321569425)
    map.set_zoom(15)
    marker = map.set_marker(33.52322419997178, 36.29292321569425)
    marker.set_text('Razan[صيدليه المزرعه]')

def dahaan():
    map = TkinterMapView (root,width=500,height=400,corner_radius=0)
    map.place(x=370,y=40)
    map.set_tile_server("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d475322.6559024308!2d39.49134090897901!3d21.45052894054877!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x15c3d01fb1137e59%3A0xe059579737b118db!2z2KzYr9ip!5e0!3m2!1sar!2ssa!4v1672225917807!5m2!1sar!2ssa",max_zoom=22)
    #  خطوط الطول والعرض نروح لقوقل ماب ونكتب صيديله مركزيه بعدين كلك يمين وننسخ الاحداثيات
    map.set_position(33.528644041556326, 36.28987030220258)
    map.set_zoom(15)
    marker = map.set_marker(33.528644041556326, 36.28987030220258)
    marker.set_text('Razan[صيدليه المزرعه]')


# ======جزء البرمجه لاظهار المدينه اللي يبحث عنها المستخدم=========
def cu(): #تعريف داله اسمها cu()
    country = En.get() # متغير كونتري = اجلب فيه البايانات اللي دخلها اليوزر في متغير سطر 55 
    #  متغير ماب اللي في سطر182 جيب فيه الخريطه من الرابط
    # 22على قيمه للتكبيرmax_zoom
    # map.set_tile_server("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d475322.6559024308!2d39.49134090897901!3d21.45052894054877!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x15c3d01fb1137e59%3A0xe059579737b118db!2z2KzYr9ip!5e0!3m2!1sar!2ssa!4v1672225917807!5m2!1sar!2ssa",max_zoom=22)
    # جيب الموقع اللي كتبه اليوزر وحدده بالدبوس الاحمر
    map.set_address(country,marker=True)


# كتابة نص داخل البرنامج عن طريق تغيير خصائص label (خلفية الخط,نوع الخط وحجمه,اسم البرنامج , النص , لون الخط)
# اسنادها داخل متغير
# لعرض النص نستخدم label
# ==================title =====================
title1 = Label(root,
               text='مشروع الصيدليات المناوبه',
               fg='white', 
               bg='black',
               font=('Tajawal',18),
               )
#  تشغيل ماسبق عن طريق داله .pack(خاصيه لملاء المساحه كامله)
# ولكن هذه الداله تعرض بشكل تسلسلي أي من اعلى الصفحه وبعدين تحت وهكذا  
title1.pack(fill='x')  


# ===================logo======================
#بعدها نضع الصوره تبع الوقو داخل متغير باستدعاء الصوره داخل داله  PhotoImage(اسم الصور
logo = PhotoImage(file=('logo.png'))
# لتغيير خصائص الصورهlable
lab_log = Label(root, image=logo, bd=0,bg='white' )
# .place()داله لعرض ماسبق ولكنها تختلف عن .pack في انها تسمح بتحديد مكان العرض 
lab_log.place(x=30,y=40)

# =========== Label + Entry + button ==========
# كلمة country:
l = Label(root,text='Country:',font=('Tajawal','13'),fg='black',bg='white')
# من اليسار 10 من فوق 260
l.place(x=10,y=260)


# مربع البحث
# Groove شكل البوردر تبع البحث
En = Entry(root, font=('Tajawal',14),width=10,bd=2,relief=GROOVE)
En.place(x=100,y=260)

# ( اسم البرنامج,اللي مكتوب ع الزر,خلفية الزر,لون الخط) زر البحث
b1=Button(root, 
          text='Get country',
          bg='black',
          fg='white',
          bd=2,
          relief=SOLID, #لازم اعرف ايش وظيفتها
          width=10,
          cursor='hand2',#علشان تحول المؤشر من سهم ليد اذا حطيناها ع الزر
          command=cu #20اضفنا الداله اللي تطلع الخريطه وتحدد المكان سطر
          )
b1.place(x=220,y=260)

# ================pharmacy Buttons===============
b = Button(
    root, text='صيدلية مركزيه',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12,
    # يعني اذا ضغطت ع الزر نفذ دالة markazi
    command=markazi
)
b.place(x=10,y=300) 

b1 = Button(
    root, text='صيدلية المزرعه',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12,
    command=mazraa
)
b1.place(x=130,y=300)

b2 = Button(
    root, text='صيدلية الطحان',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12,
    command=dahaan
)
b2.place(x=250,y=300)

b3 = Button(
    root, text='صيدليه جباصيني',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12
)
b3.place(x=10,y=340)

b4 = Button(
    root, text='صيدليه المجتهد',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12
)
b4.place(x=130,y=340)

b5 = Button(
    root, text='صيدليه الغزالي',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12
)
b5.place(x=250,y=340)

b6 = Button(
    root, text='صيدليه الملقي',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12
)
b6.place(x=10,y=380)

b7 = Button(
    root, text='صيدليه الحفار',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12
)
b7.place(x=130,y=380)

b8 = Button(
    root, text='صيدليه الشهبندر',
    cursor='hand2',
    bg='white',
    fg='black',
    bd=1,
    relief=SOLID, # شكل بوردر الزر
    font=('Tajawal','13'),
    width=12
)
b8.place(x=250,y=380)

# ==============map================
# (الحواف 0 مالها حواف و الارتفاع والعرض و اسم البرنامج)
map = TkinterMapView(root, width=500,height=400,corner_radius=0)
map.place(x=370,y=45)


# كل ماكتبت root معناها.
# دالة .mainloop() تشغل البرنامج.
root.mainloop()


