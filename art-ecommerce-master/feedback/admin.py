from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating_display', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved', 'created_at')
    search_fields = ('name', 'email', 'comment')
    readonly_fields = ('user', 'created_at', 'updated_at')
    fieldsets = (
        ('Feedback Information', {
            'fields': ('user', 'name', 'email', 'comment', 'rating')
        }),
        ('Admin Controls', {
            'fields': ('is_approved',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    actions = ['approve_feedback', 'reject_feedback']
    
    def rating_display(self, obj):
        """Display rating as stars."""
        stars = '⭐' * obj.rating
        return f"{stars} ({obj.rating}/5)"
    rating_display.short_description = 'Rating'
    
    def approve_feedback(self, request, queryset):
        """Admin action to approve feedbacks."""
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'✓ {updated} feedback(s) approved.')
    approve_feedback.short_description = 'Approve selected feedbacks'
    
    def reject_feedback(self, request, queryset):
        """Admin action to reject feedbacks."""
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'✗ {updated} feedback(s) rejected.')
    reject_feedback.short_description = 'Reject selected feedbacks'
