from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Admission
from .serializers import AdmissionSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

    permission_classes = (IsAuthenticated, )