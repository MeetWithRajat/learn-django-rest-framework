from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from learning_api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    serializers_class = serializers.HelloSerializer

    @staticmethod
    def get(request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives the most control over the application logic',
            'Is mapped manually to URL'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
