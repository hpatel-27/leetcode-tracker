from rest_framework.routers import DefaultRouter
from .views import ProblemViewSet, SolutionViewSet, TagViewSet

router = DefaultRouter()
router.register(r"problems", ProblemViewSet, basename="problems")
router.register(r"solutions", SolutionViewSet, basename="solutions")
router.register(r"tags", TagViewSet, basename="tags")

urlpatterns = router.urls
