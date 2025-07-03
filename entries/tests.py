from django.test import TestCase
from .models import Profile, JournalEntry, Tag
from django.contrib.auth.models import User

# Create your tests here.
class ProfileClassTests(TestCase):
    '''
    class tests the Profile class model
    '''
    def tearDown(self):
        """
        method deletes all objects created during the tests
        """
        Profile.objects.all().delete()
        User.objects.all().delete()

    def setUp(self):
        self.user = User(email='test@gmail.com', username='test', password='test', first_name='test', last_name='test')
        self.user.save()
        self.profile = Profile(user=self.user, bio='test bio', profile_pic='test.jpg')

    def test_instance(self):
        """
        method checks if a profile object is initialized properly
        """
        self.assertIsInstance(self.profile, Profile)

    def test_save_profile(self):
        """
        method checks if a profile object is saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_profile_update(self):
        """
        method checks if a profile object is updated
        """
        profile = Profile.objects.create(user=self.user, bio='test bio 1', profile_pic='test.jpg')
        Profile.objects.filter(pk=profile.pk).update(bio='test bio 2')
        profile.update_profile()
        self.assertEqual(profile.bio, 'test bio 2')
    
    def test_delete_profile(self):
        """
        method checks if a profile object is deleted
        """
        profile = Profile.objects.create(user=self.user, bio='test bio to delete', profile_pic='test.jpg')
        Profile.objects.filter(pk=profile.pk).delete()
        profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
        
class TagClassTests(TestCase):

    '''
    class tests the Tag class model
    '''

    def tearDown(self):
        """
        method deletes all objects created during the tests
        """
        Tag.objects.all().delete()

    def setUp(self):
        self.tag = Tag(name='test tag')
        
    def test_instance(self):
        """
        methods checks if tag model is initialized properly
        """
        self.assertIsInstance(self.tag, Tag)

    def test_save_tag(self):
        """
        methods checks if tag model is saved
        """
        self.tag.save_tags()
        tags = Tag.objects.all()
        self.assertTrue(len(tags) > 0)
    
    def test_update_tag(self):
        """
        methods checks if tag model is updated
        """
        tag = Tag.objects.create(name='test tag to update')
        Tag.objects.filter(pk=tag.pk).update(name='test tag updated')
        tag.update_tags()
        self.assertEqual(tag.name, 'test tag updated')
    
    def test_delete_tag(self):
        """
        methods checks if tag model is deleted
        """
        tag = Tag.objects.create(name='test tag to delete')
        Tag.objects.filter(pk=tag.pk).delete()
        tag.delete_tags()
        tags = Tag.objects.all()
        self.assertTrue(len(tags) == 0)

class JournalEntryClassTests(TestCase):
    """
    class tests the JournalEntry class model
    """

    def tearDown(self):
        """
        method deletes all objects created during the tests
        """
        Profile.objects.all().delete()
        Tag.objects.all().delete()
        JournalEntry.objects.all().delete()

    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com", username= "Doeish", password= "test", first_name= "John", last_name= "Doe")
        self.profile = Profile.objects.create(user=self.user, bio="test bio", profile_pic="test.jpg")
        self.tag = Tag.objects.create(name="test tag")
        self.entry = JournalEntry.objects.create(author=self.profile, title="test title", body="test body", is_archived=False)
        self.entry.tags.add(self.tag)
    
    def test_instance(self):
        """
        method checks if a journal entry object is initialized properly
        """
        self.assertIsInstance(self.entry, JournalEntry)
    
    def test_save_entry(self):
        """
        method checks if a journal entry object is saved
        """
        self.entry.save_entry()
        entries = JournalEntry.objects.all()
        self.assertTrue(len(entries) > 0)
    
    def test_update_entry(self):
        """
        method checks if a journal entry object is updated
        """
        entry = JournalEntry.objects.create(author=self.profile, title="test title", body="test body", is_archived=False)
        JournalEntry.objects.filter(pk=entry.pk).update(title="test title updated")
        entry.update_entry()
        self.assertEqual(entry.title, "test title updated")
    
    def test_delete_entry(self):
        """
        method checks if a journal entry object is deleted
        """
        self.entry.save_entry()
        self.entry.delete_entry()
        entries = JournalEntry.objects.all()
        print(entries)
        self.assertTrue(len(entries) == 0)
    
    def test_search_by_title(self):
        """
        method checks if a journal entry object is searched by title
        """
        entry = JournalEntry.objects.create(author=self.profile, title="test title to search", body="test body", is_archived=False)
        search = entry.search_by_title("test title to search")
        initial_project = JournalEntry.objects.filter(pk=entry.pk)
        self.assertQuerySetEqual(search, initial_project, transform=lambda x:x)
    
    def test_search_by_archive_status(self):
        """
        method checks if a journal entry object is searched by archive status
        """
        entry = JournalEntry.objects.create(author=self.profile, title="test title to search", body="test body", is_archived=False)
        search = entry.search_by_archive_status(False)
        
        self.assertTrue(len(search) > 0)
    
    def test_search_by_tags(self):
        """
        method checks if a journal entry object is searched by tags
        """
        entry = JournalEntry.objects.create(author=self.profile, title="test title to search", body="test body", is_archived=False)
        search = entry.search_by_tags("test tag")
        
        self.assertTrue(len(search) > 0)