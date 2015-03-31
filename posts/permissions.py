from rest_framework import permissions


class IsAuthorOfPost(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.user:
            return post.author == request.user
        return False


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.user:
            return request.user.is_admin
        return False
