from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, Department, Designation



class AccountAdmin(UserAdmin):
	list_display = (
     'email','username','date_joined','dt_ob', 
     'last_login', 'is_admin','is_staff',
     'Department', 'Designation',
     'highest_quali','pan_no',
     'gender','quali_year',
     'tot_experience',     
     )
	search_fields = ('email','username',)
	readonly_fields=('id', 'last_login','date_joined')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Department)
admin.site.register(Designation)