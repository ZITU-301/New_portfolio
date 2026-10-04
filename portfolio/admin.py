from django.contrib import admin
from .models import (
    Profile,
    SocialLink,
    Skill,
    Service,
    Project,
    Education,
    Experience,
    Achievement,
    BlogPost,
    Testimonial,
    ContactMessage,
)


# =========================
# Profile
# =========================
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
        "email",
        "phone",
        "available_for_work",
        "updated_at",
    )

    search_fields = (
        "name",
        "title",
        "email",
    )

    list_filter = (
        "available_for_work",
        "updated_at",
    )


# =========================
# Social Links
# =========================
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        "platform",
        "url",
        "order",
        "is_active",
    )

    list_filter = (
        "platform",
        "is_active",
    )

    search_fields = (
        "platform",
        "url",
    )

    list_editable = (
        "order",
        "is_active",
    )


# =========================
# Skills
# =========================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "percentage",
        "order",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
        "category",
    )

    list_editable = (
        "percentage",
        "order",
    )


# =========================
# Services
# =========================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "order",
        "is_active",
    )


# =========================
# Projects
# =========================
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "featured",
        "created_at",
    )

    list_filter = (
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "technologies",
    )

    list_editable = (
        "featured",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
    )


# =========================
# Education
# =========================
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "institution",
        "start_year",
        "end_year",
        "result",
        "order",
    )

    search_fields = (
        "degree",
        "institution",
        "location",
    )

    list_filter = (
        "start_year",
        "end_year",
    )

    list_editable = (
        "order",
    )


# =========================
# Experience
# =========================
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "start_date",
        "end_date",
        "current",
        "order",
    )

    search_fields = (
        "position",
        "company",
        "description",
    )

    list_filter = (
        "current",
        "start_date",
    )

    list_editable = (
        "current",
        "order",
    )


# =========================
# Achievements
# =========================
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organization",
        "date",
    )

    search_fields = (
        "title",
        "organization",
    )

    list_filter = (
        "date",
    )


# =========================
# Blog Posts
# =========================
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "published",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "published",
        "created_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
    )

    list_editable = (
        "published",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )


# =========================
# Testimonials
# =========================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "role",
        "message",
    )

    list_editable = (
        "is_active",
    )


# =========================
# Contact Messages
# =========================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "is_read",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "name",
        "email",
        "subject",
        "message",
        "created_at",
    )