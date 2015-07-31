from django.contrib.auth.decorators import login_required
from datahub.helpers.decorators import provide_profile, require_profile


class ProvideProfileMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return provide_profile(view)


class ProfileRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return require_profile(view)


class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)


class AddUserToFormMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class AddProfileToFormMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.profile = self.request.user.profile
        return super().form_valid(form)
