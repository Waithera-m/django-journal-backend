from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/')
    objects = models.Manager()
    active_objects = models.Manager()

    def save_profile(self):
        """
        method saves added profile
        """
        self.save()
    
    def update_profile(self, using=None, fields=None, **kwargs):
        """
        class method updates profile properties
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()

            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
                
        super().refresh_from_db(using, fields, **kwargs)

    def delete_profile(self):
        """
        method deletes saved profile
        """
        self.delete()
    
    def __str__(self):
        return f'{self.user.username}'
           
class JournalEntry(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='entries_tags')
    objects = models.Manager()
    active_objects = models.Manager()

    def save_entry(self):
        """
        method saves added journal entry
        """
        self.save()
    
    def update_entry(self, using=None, fields=None, **kwargs):
        """
        method updates saved journal entry
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()

            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)
    
    def delete_entry(self):
        """
        method deletes saved journal entry
        """
        self.delete()

    @classmethod
    def search_by_title(cls, title):
        """
        class method searches for a journal entry by title
        """
        return cls.objects.filter(title__icontains=title)

    @classmethod
    def search_by_archive_status(cls, status):
        """
        class method searches for a journal entry by archive status
        """
        return cls.objects.filter(is_archived=status)

    @classmethod
    def search_by_tags(cls, tags):
        """
        class method searches for a journal entry by tags
        """
        return cls.objects.filter(tags__name__icontains=tags)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save_tags(self):
        """
        method saves added tag
        """
        self.save()
    
    def update_tags(self, using=None, fields=None, **kwargs):
        """
        class method updates profile properties
        """
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()

            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
                
        super().refresh_from_db(using, fields, **kwargs)

    def delete_tags(self):
        """
        method deletes saved tag
        """
        self.delete()
    
    def __str__(self):
        return f'{self.name}'