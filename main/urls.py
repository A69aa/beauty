from django.contrib import admin
from django.urls import path
from beauty import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/push/',views.PushNotificationsListAPIView.as_view()),
    path('api/v1/push/<int:id>/',views.PushCreateUpdateDeleteAPIView.as_view()),
    path('api/v1/image/',views.InteriorImageListCreateAPIView.as_view()),
    path('api/v1/image/<int:id>/',views.InteriorImageUpdateDeleteAPIView.as_view()),
    path('api/v1/image2/',views.WorksOfMastersImageListCreateAPIView.as_view()),
    path('api/v1/image2/<int:id>/',views.worksImageUpdateDeleteAPIView.as_view())
]
