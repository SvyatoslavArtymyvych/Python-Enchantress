from django.contrib.auth import login, logout

# Create your views here.
from django.db.models import F
from rest_framework import generics

from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework import viewsets

from apps.api.serializers.auth import APIAuthSerializer
from apps.api.serializers.car import CarAPISerializer
from apps.api.serializers.order import OrderAPISerializer
from apps.api.serializers.dealer_car import DealerCarAPISerializer
from apps.api.serializers.dealer_car import CarPublishSerializer

from apps.cars.models import Car
from apps.cars.models import Order

from src.apps.api.serializers.dealer_car import CarStatisticsSerializer


class LoginAPIView(APIView):

    def post(self, request):
        serializer = APIAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request=request, user=user)
        token, created = Token.objects.get_or_create(user=user)
        content = {
            'token': token.key,
        }

        return Response(content)

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            token = Token.objects.get(user=request.user)
            return Response({'token': token.key})
        # except TypeError:
        return Response({'message': 'Please send username and password'})


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        if request.user.is_authenticated:
            token = Token.objects.filter(user=request.user).delete()
            logout(request)
            return Response({'message': 'logged out'})
        return Response({'message': 'you not logged in'})


class OrderAPIView(CreateAPIView):
    serializer_class = OrderAPISerializer
    queryset = Order.objects.all()


class CarsAPIView(ListAPIView):
    serializer_class = CarAPISerializer
    queryset = Car.objects.filter(publish=True)
    filter_backends = [SearchFilter]

    search_fields = ['brand__title', 'model__name']


class CarAPIView(ListAPIView):
    serializer_class = CarAPISerializer
    filter_backends = [SearchFilter]

    def get_queryset(self):
        car_id = self.kwargs['pk']

        Car.objects.filter(id=car_id).update(views=F('views') + 1)
        return Car.objects.filter(id=car_id, publish=True)


class DealerCarsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DealerCarAPISerializer

    def get_queryset(self):
        return Car.objects.filter(dealer=self.request.user)


class CarCreateApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DealerCarAPISerializer
    queryset = Car.objects.all()


class CarUpdateApi(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DealerCarAPISerializer

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return Car.objects.filter(id=car_id, dealer=self.request.user)


class CarDeleteApi(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = DealerCarAPISerializer

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return Car.objects.filter(id=car_id, dealer=self.request.user)


class CarPublishAPI(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return Car.objects.filter(id=car_id, dealer=self.request.user)

    @action(methods=['post'], detail=True)
    def publish(self, request, *args, **kwargs):
        serializer = CarPublishSerializer

        car_id = self.kwargs['pk']

        Car.objects.filter(id=car_id).update(publish=True)

        return Response({'message': 'published'})

    @action(methods=['post'], detail=True)
    def unpublish(self, request, *args, **kwargs):
        serializer = CarPublishSerializer

        car_id = self.kwargs['pk']

        Car.objects.filter(id=car_id).update(publish=False)

        return Response({'message': 'unpublish'})


class CarStatisticsApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CarStatisticsSerializer

    def get_queryset(self):
        user = self.request.user
        return Car.objects.filter(dealer=self.request.user)
