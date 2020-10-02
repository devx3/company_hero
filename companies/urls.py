from rest_framework.routers import SimpleRouter
from .views import CompanyViewSet, EmployeeViewSet

router = SimpleRouter()
router.register('companies', CompanyViewSet, basename='companies')
router.register('employees', EmployeeViewSet, basename='employees')
