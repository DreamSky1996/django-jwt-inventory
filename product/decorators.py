from rest_framework.response import Response
from rest_framework.views import status

def validate_request_data(fn):
    def decorated(*args, **kwargs):
        product_data = args[0].request.data.get("data", "")
        if not product_data:
            return Response(
                data={
                    "message": "Data is required to add a product"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)

    return 