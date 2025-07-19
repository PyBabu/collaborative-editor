# from django.contrib.sessions.middleware import SessionMiddleware
# from users.models import UserSession
# from django.utils import timezone

# class ActiveUserMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             session_key = request.session.session_key
#             if session_key:
#                 UserSession.objects.update_or_create(
#                     session_id=session_key,
#                     defaults={
#                         'user': request.user,
#                         'last_activity': timezone.now()
#                     }
#                 )
        
#         response = self.get_response(request)
#         return response