import traceback
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from objects.models import Node
from flowsheet.models import Project
from objects.serializers.EdgeSerializer import EdgeSerializer
from objects.models.Edge import Edge
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes


class CreateEdgeSerializer(serializers.Serializer):
    project = serializers.IntegerField(required=True)
    source = serializers.IntegerField(required=True)
    target = serializers.IntegerField(required=True)


class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer

    def get_queryset(self):
        queryset = self.queryset
        projectID = self.request.query_params.get("projectID")
        if projectID is not None:
            queryset = queryset.filter(project=projectID)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(name="projectID", required=True, type=OpenApiTypes.INT),
        ]
    )
    def list(self, request):
        return super().list(request)

    def error_response(self, e):
        tb_info = traceback.format_exc()
        error_message = str(e)
        response_data = {
            "status": "error",
            "message": error_message,
            "traceback": tb_info,
        }
        return Response(response_data, status=400)

    @extend_schema(request=CreateEdgeSerializer, responses=None)
    def create(self, request):
        """
        Custom CREATE function.
        Validates URL Params and Serializes data.
        """
        try:
            # Extract data from the request
            projectID = request.data.get("project")
            project = Project.objects.get(pk=projectID)

            source = request.data.get("source", None)
            target = request.data.get("target", None)

            if not project or not source or not target:
                raise ValueError("Source and target are required")

            source_obj = Node.objects.get(pk=source)
            target_obj = Node.objects.get(pk=target)

            # Use the ObjectBase.create method
            instance = Edge.objects.create(
                project=project, source=source_obj, target=target_obj
            )
            instance.save()

            # Serialize and return the created object
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=201)

        except Exception as e:
            return self.error_response(e)
