from rest_framework.serializers import ModelSerializer
from .models import Vacancy,Booking




class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields =[
            'id',
            'housetitle',
            'roomsvacant',
            'housedescription',
            'picture',

        ]

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields =[
            'id',
            'title',
            'message',
            'email',
            'date',
        ]