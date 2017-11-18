#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Permissions for APIStar, Classes with has_permission() that returns bool."""


from apistar.interfaces import Auth


class IsGuestUser():  # A Guest.
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return bool(auth.user.is_guest)


class IsFreeUser():  # A Free tier user.
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return bool(auth.user.is_free)


class IsPremiumUser():  # A Premium tier user.
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return bool(auth.user.is_premium)


class IsCompanyUser():  # A Company account.
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return bool(auth.user.is_company)


class IsAdminUser():  # An Admin.
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return bool(auth.user.is_admin)


class IsTesterUser():  # A QA Tester user.
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return bool(auth.user.is_tester)


class IsStaffUser():  # An Staff Admin.
    def has_permission(self, auth: Auth):
        if not auth.is_authenticated():
            return False
        return bool(auth.user.is_staff)
