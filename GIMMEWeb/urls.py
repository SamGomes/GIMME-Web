from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from GIMMEWeb.core.views import Views

urlpatterns = [
    re_path(r'^$', Views.home, name=""),
    re_path(r'^home/$', Views.home, name="home"),
    re_path(r'^logout/$', Views.logout, name="logout"),
    re_path(r'^isLoggedIn/$', Views.isLoggedIn, name="isLoggedIn"),

    re_path(r'^initServer/$', Views.initServer, name="initServer"),

    re_path(r'^dash/$', Views.dash, name="dash"),

    re_path(r'^userRegistration/$', Views.userRegistration, name="userRegistration"),
    re_path(r'^taskRegistration/', Views.taskRegistration, name="taskRegistration"),

    re_path(r'^updateUserRegMode/$', Views.updateUserRegMode, name="updateRegMode"),
    re_path(r'^updateTaskRegMode/$', Views.updateTaskRegMode, name="updateRegMode"),

    re_path(r'^saveUserRegistration/$', Views.saveUserRegistration, name="saveUserRegistration"),
    re_path(r'^removeUserRegistration/$', Views.removeUserRegistration, name="removeUserRegistration"),

    re_path(r'^saveTaskRegistration/$', Views.saveTaskRegistration, name="saveTaskRegistration"),
    re_path(r'^removeTaskRegistration/$', Views.removeTaskRegistration, name="removeTaskRegistration"),

    re_path(r'^addAllUsersSelected/$', Views.addAllUsersSelected, name="addAllUsersSelected"),
    re_path(r'^removeAllUsersSelected/$', Views.removeAllUsersSelected, name="removeAllUsersSelected"),
    re_path(r'^addSelectedUser/$', Views.addSelectedUser, name="addSelectedUser"),
    re_path(r'^removeSelectedUser/$', Views.removeSelectedUser, name="removeSelectedUser"),
    
    re_path(r'^addAllTasksSelected/$', Views.addAllTasksSelected, name="addAllTasksSelected"),
    re_path(r'^removeAllTasksSelected/$', Views.removeAllTasksSelected, name="removeAllTasksSelected"),
    re_path(r'^addSelectedTask/$', Views.addSelectedTask, name="addSelectedTask"),
    re_path(r'^removeSelectedTask/$', Views.removeSelectedTask, name="removeSelectedTask"),

    re_path(r'^loginCheck/$', Views.loginCheck, name="loginCheck"),
    re_path(r'^startAdaptation/', Views.startAdaptation, name="startAdaptation"),
    re_path(r'^configAdaptation/', Views.configAdaptation, name="configAdaptation"),

    re_path(r'^startActivity/', Views.startActivity, name="startActivity"),
    re_path(r'^saveTaskResults/', Views.saveTaskResults, name="saveTaskResults"),

    
    re_path(r'^fetchServerState/', Views.fetchServerState, name="fetchServerState"),
    re_path(r'^fetchSelectedUserStates/', Views.fetchSelectedUserStates, name="fetchSelectedUserStates"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)