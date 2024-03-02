"""
Middleware to set user metadata and request metadata in the MetadataManager
"""

from django_auditor_logs.metadata import MetadataManager


class MetadataMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_metadata = {
            "ip": request.META.get("REMOTE_ADDR"),
            "user_agent": request.META.get("HTTP_USER_AGENT"),
            "method": request.META.get("REQUEST_METHOD"),
            "path": request.META.get("PATH_INFO"),
            "query_string": request.META.get("QUERY_STRING"),
            "content_type": request.META.get("CONTENT_TYPE"),
            "content_length": request.META.get("CONTENT_LENGTH"),
            "referer": request.META.get("HTTP_REFERER"),
        }
        MetadataManager.set_request_metadata(request_metadata)
        if "Authorization" in request.headers:
            try:
                import jwt

                token = request.headers["Authorization"].replace("Bearer ", "")
                user_metadata = jwt.decode(token, verify=False)
            except:
                try:
                    import jwt

                    token = request.headers["Authorization"].replace("Bearer ", "")
                    user_metadata = jwt.decode(
                        token, options={"verify_signature": False}
                    )
                except:
                    user_metadata = {
                        "Authorization": request.headers["Authorization"],
                    }
            MetadataManager.set_user_metadata(user_metadata)
        elif hasattr(request, "user") and request.user.is_authenticated:
            user_metadata = {
                "username": request.user.username,
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
            }
            MetadataManager.set_user_metadata(user_metadata)
        response = self.get_response(request)
        MetadataManager.clear_user_metadata()
        MetadataManager.clear_request_metadata()
        return response
