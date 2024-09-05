from rest_framework.permissions import BasePermission


class IsLoanProvider(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.role == 'UserRole.LOAN_PROVIDER')



class IsLoanCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.role == 'UserRole.LOAN_CUSTOMER')


class IsBankStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.role == 'UserRole.BANK_STAFF')
