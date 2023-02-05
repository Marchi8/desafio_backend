# from .serializers import UserSerializer
from rest_framework.views import APIView, Request, Response, status
from .models import DocFile
from .serializers import ParseSerializer

# Create your views here.
class ParseView(APIView):

    queryset = DocFile.objects.all()
    serializer_class = ParseSerializer

    def post(self, request: Request) -> Response:
        """
        o arquivo fica em request.FILES
        """
        cnab = request.FILES["file"]
        data = []
        for fields in cnab:
            data.append(
                {
                    "type": fields[0:1],
                    "date": fields[1:9],
                    "value": float(str(fields[9:19]).lstrip("b'0")[:-1]) / 100,
                    "cpf": fields[19:30],
                    "cardNum": fields[30:42],
                    "hour": fields[42:48],
                    "owner": fields[48:62].decode("utf-8"),
                    "store": fields[62:81].decode("utf-8"),
                }
            )
        return Response(data, status.HTTP_201_CREATED)
