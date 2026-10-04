from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    short_bio = models.TextField()
    about = models.TextField()

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True)

    cv = models.FileField(
        upload_to="cv/",
        blank=True,
        null=True
    )

    available_for_work = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("youtube", "YouTube"),
    ]

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES
    )

    url = models.URLField()
    icon = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.platform


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(default=50)

    category = models.CharField(
        max_length=100,
        default="Technical"
    )

    icon = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.TextField()

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    technologies = models.CharField(
        max_length=500,
        help_text="Example: Django, Python, HTML, CSS"
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)

    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    description = models.TextField(blank=True)
    result = models.CharField(max_length=100, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True
    )

    current = models.BooleanField(
        default=False
    )

    description = models.TextField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.position} - {self.company}"


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)

    description = models.TextField(
        blank=True
    )

    date = models.DateField(
        blank=True,
        null=True
    )

    certificate = models.FileField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=250)

    slug = models.SlugField(
        unique=True
    )

    excerpt = models.TextField()

    content = models.TextField()

    image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True
    )

    published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)

    message = models.TextField()

    image = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"