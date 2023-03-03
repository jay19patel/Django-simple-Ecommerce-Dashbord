# Django-simple-Ecommerce-Dashbord my Nots
This is a simple e commerce dashbord using django 


steps For Django Setup:


1:
-create virtual Environment (venv)
-activate venv
-install django and moduls

2:
-make django project 
-make django app
-connect project with app
-set url in main project setting file 
-set view and urls in apps file
- strat project


3:
http response : txt print in page
(django.http)
render : html page render 
(djago.shortcuts)


4: 
URLS: urls are mange the urls and use to render this urls which view connet with them
VIEWS: view are a file ,they contain logics of whole projects and render html files 

5:
templates:
-templates is a container of all htmls file
-set templates in main project file in setting in TEMPLATES =[] => ['templates'] 
same as which made in project file 
- if ours html file in  subdirectory then make sure the subfile in template filr and when we 
render thet file then take same paths as where html file have 

6:
context={}
context contail all perameters of file 
means contaxt have exchange data from html to view or database 

7:
templates inharitance :
-dont repeat yourself
-create one main html file and inherarite in all child html file
-create bloks in main html for all block add here
(jyare call thay koy html file ne to e main file na block part ma add they jay and pachi diplay thay)
- so we create :
	{% block content%}
 	content 
	{% endblock %}
-child file :
	{% extends 'accounts/main.html' %}
	{% block content%}
 	content 
	{% endblock %}
-if you some add html tag outside of block they not print


8: 
navbar andf footer :
create row file for nav and footer 
include thet file in main html file  using include
	{% include 'accounts/navbar.html' %}

include is very use full when some content are repeted multiple time 

9: 
adding Bootstraps
- add bootstrap CDN in main file
-all row contain are set in child classes

10:
statics files:
-creat static file in project main file where also template file create (note: only name is : static)
- create child file like Css & javascript photo videos 
-link files:
	-go main setting 
	-STATICFILES_DIRS = [ BASE_DIR, 'static']

-when setting is change then, we use static file using {% load statics %} as a import and 
file as as{% static 'img.jpg'%}
- also add MEDIA_URL =['imamges/']

-----------------------Data Base------------------------

-MYSQL
-POSTGRE MYSQL

11:
models.py
-create table usigng classes 
-makemigrations (conating changes but not change in DB)
-migrate(change with dataabase )
-need to return some name or id then return :
	def __str__(self):
	    return self.name

--database realationships:
one to many
many to many
table structure 

12:
When create model go to admin.py and add your class in the pannel
-import models
-admin.site.register(Customer)

13:
add some data to test ,check thet uis work or not 
 

14:
database Model Queries:
 queryset = customer.objcets.all()
	.get()
	.filter()
	.exclude()

-menualy collecting data use:   python manage.py shall


15:
data render in templates:
use all logics in views.py
import models in view.py file

use -forloop

	{% for i in products %}
	content
	{% endfor%}

use if else:


save in variable and get all objcet using:
	products= Products.objcects.all()

what we need to pass add in context={'data':getdatanamevariable} and return it 
 in html page  in fore loop add data in {{data.name}}


if we have values then only acces using {{data}}
-check all spelings and make to easy to ready and debuging syntext


16:
one template in manny id (products details page)

add primery key in View.py also url.py 
-need to id as a primery key so we fetch id (view.py) :
	customer.objcet.get(id=pk)
-need to custom url (urls.py)
	'customer/<str:pk>/' as a url


str -> string
int -> integer
slug

here we fetch only id but we need all data of  thair id :
	order_set.all() 
	its convert the all data 
-check all the string where we change the primery key 
means ke jya jya apde use karelu hase url ne tya tya primery key pan add karva padse jem ke nav bar etc 

add url as a : {% url 'customer' customer.id %}

-URL are use name of urls



17:
Django Model Form :
 import  model which we need 
and then form import in view

from django.forms import ModelForm
from .models import Order


class Orderform(ModelForm):
    class Meta:
        model= Order
        fields = '__all__'


-whenerver we need some data uplod in backend we need csrf_token
- if request have POST method then they contain all data with request:
		form = Orderform(request.POST)
		if form.is_valid()
		form.save() # save this form in DB

- redirect :
this isa redirect page  using moduls 
when some proble are have then redirect the page 


18 :
update and delete:
use form model to update 

19:
inline Formsets:

from djago.forms import inlineformset_factory
 this use all  form in one form set

set: 
	all = inlineformset_factory(Customer,order,fields=()




baki : pt 12 dennis lvy
