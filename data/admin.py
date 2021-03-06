from django.contrib import admin
from data.models import Cause, Project, NGO, Consultant, Audit

#add all the fields of the models you want to see on the django admin panel
#just add the word "Admin" to the model name
class CauseAdmin(admin.ModelAdmin):
    list_display = ('cause_id', 'name', 'total_amount')
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'title', 'start_date', 'end_date', 'total_amount', 'raised_amount', 'cause', 'ngo_id', 'zip', 'person_of_contact', 'summary', 'team_member_id')
class NGOAdmin(admin.ModelAdmin):
    list_display = ('ngo_id', 'name', 'person_of_contact', 'registration_code', 'address', 'website', 'team_member_id')
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('consultant_id', 'name',)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('audit_id', 'date', 'report_id', 'consultant_id', 'project_id')


#mention all the models to be viewed on the django admin panel
admin.site.register(Cause, CauseAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(NGO, NGOAdmin)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(Audit, AuditAdmin)