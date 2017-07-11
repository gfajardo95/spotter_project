from rest_framework.routers import DefaultRouter

from .api import WorkoutViewSet, ExerciseViewSet, UserViewSet


router = DefaultRouter()

router.register(r'workouts', WorkoutViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
