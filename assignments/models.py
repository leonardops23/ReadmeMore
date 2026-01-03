from django.db import models

class About(models.Model):
    """
    Model representing the 'About' section.

    Attributes:
        about_heading (str): The heading of the about section.
        about_description (str): The main description of the about section.
        created_at (datetime): Timestamp when the about section was created.
        updated_at (datetime): Timestamp when the about section was last updated.
    """
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.about_heading


class SocialLink(models.Model):
    """
    Model representing social media links.

    Attributes:
        platform_name (str): The name of the social media platform.
        profile_url (str): The URL to the social media profile.
        created_at (datetime): Timestamp when the social link was created.
        updated_at (datetime): Timestamp when the social link was last updated.
    """
    platform_name = models.CharField(max_length=25)
    profile_url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['platform_name']
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return self.platform_name
