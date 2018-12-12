from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import parsers, renderers

from .models import Admission
from .serializers import AdmissionSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

    permission_classes = (
        IsAuthenticated,
    )

class SanityCheck(APIView):
    """
    List all snippets, or create a new snippet.
    """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    #renderer_classes = (renderers.JSONRenderer,)
    def get(self, request, format=None):
        print('authenticated? {}'.format(request.user.is_authenticated))
        return Response({
            'ping': 'pong',
            'authenticated': request.user.is_authenticated
        })