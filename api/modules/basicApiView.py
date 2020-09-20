from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny


class IsAutenticatedListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    pass


class IsAutenticatedCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    pass


class IsAutenticatedUpdateAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    pass


class IsAutenticatedGetApiView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    pass


# VIEWS SEM AUTENTICAÇAO

class AllowListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    pass


class AllowCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    pass


class AllowUpdateAPIView(UpdateAPIView):
    permission_classes = (AllowAny,)
    pass


class AllowGetAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    pass
