from rest_framework import permissions

class EhSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser: # so ira deletar se for super usuario --> ir em permissions e marcar status de superusuario (localhost:8000/admin)
                return True
            return False
        return True