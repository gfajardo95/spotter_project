from rest_framework.routers import DefaultRouter

from .api import WorkoutViewSet, ExerciseViewSet


router = DefaultRouter()

router.register(r'workouts', WorkoutViewSet)
router.register(r'exercises', ExerciseViewSet)

urlpatterns = router.urls
