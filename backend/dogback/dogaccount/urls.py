from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DogProfile, DogDetail, DogViewSet#, DogProfileViewSet#, extraction_vec

from django.conf.urls.static import static # 이미지처리 setting -> static
from django.conf import settings # import settings

router = DefaultRouter()
router.register('nose-print', DogViewSet)
#router.register('up-weight', DogProfileViewSet)

profile_detail = DogViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path('profile/',profile_detail),
    path('profile/<int:nose_vec>',DogProfile.as_view()),
    #path('profile/<int:pk>/',DogDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)