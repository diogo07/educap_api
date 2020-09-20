from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


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