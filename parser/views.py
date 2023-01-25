# from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from .models import DocFile
from .serializers import ParseSerializer
import ipdb

# Create your views here.
class ParseView(CreateAPIView):

    queryset = DocFile.objects.all()
    serializer_class = ParseSerializer

    def perform_create(self, serializer):
        """
        o arquivo fica em self.request.FILES
        """
        ipdb.set_trace()
        serializer.save()
