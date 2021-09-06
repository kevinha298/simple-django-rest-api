from api.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)

# URL: http://127.0.0.1:8000/api/employee/1
# GET: http://127.0.0.1:8000/api/employee/2
# POST: http://127.0.0.1:8000/api/employee/2
# PUT: http://127.0.0.1:8000/api/employee/2/
# DELETE: 
# List, Retrieve