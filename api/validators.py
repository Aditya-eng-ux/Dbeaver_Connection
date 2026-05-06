"""
Custom validators for the API
"""
import re
from django.core.exceptions import ValidationError


def validate_email_domain(email):
    """
    Validate that email is from allowed domains
    """
    allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']
    domain = email.split('@')[1] if '@' in email else ''
    
    if domain not in allowed_domains:
        raise ValidationError(f"Email domain '{domain}' is not allowed. Use: {', '.join(allowed_domains)}")


def validate_name_not_empty(name):
    """
    Validate that name is not just whitespace
    """
    if not name or not name.strip():
        raise ValidationError("Name cannot be empty or whitespace only")


def validate_title_length(title):
    """
    Validate that title is at least 3 characters
    """
    if len(title) < 3:
        raise ValidationError("Title must be at least 3 characters long")
