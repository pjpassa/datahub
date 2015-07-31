from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect


def get_request(*args, **kwargs):
    if "request" in kwargs:
        request = kwargs["request"]
    else:
        request = args[0]
    return request


def provide_profile(view):
    def func(*args, **kwargs):
        request = get_request(*args, **kwargs)
        try:
            profile_id = request.user.profile.id
            return view(pk=profile_id, *args, **kwargs)
        except ObjectDoesNotExist:
            return redirect("home")
        except AttributeError:
            return redirect("login")
    return func


def require_profile(view):
    def func(*args, **kwargs):
        request = get_request(*args, **kwargs)
        try:
            test = request.user.profile
        except ObjectDoesNotExist:
            return redirect("home")
        except AttributeError:
            return redirect("login")
        if test:
            return view(*args, **kwargs)
        return redirect("login")
    return func
