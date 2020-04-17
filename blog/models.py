from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date= models.DateTimeField()
    body= models.TextField(null=True)
    blog_image= models.ImageField(upload_to='images/', null=True)
    blog_image2= models.ImageField(upload_to='images/', null=True)
    blog_image3= models.ImageField(upload_to='images/', null=True)
    blog_image4= models.ImageField(upload_to='images/', null=True)
    blog_image5= models.ImageField(upload_to='images/', null=True)


    class Meta:
      verbose_name_plural = "blog"

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

   
    def g_code(self):
        return self.body.splitlines()

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def uppercase(self):
        return self.title.upper()
# blog app to settingss
# create migrateion
# migrate
#add to admin