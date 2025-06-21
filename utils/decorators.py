from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def role_required(*allowed_roles, redirect_to="hardware:hardware_list"):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user_role = getattr(request.user, "role", None)

            if not user_role or user_role.name not in allowed_roles:
                messages.error(
                    request, "You don't have permission to access this site."
                )
                return redirect(reverse(redirect_to))

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
