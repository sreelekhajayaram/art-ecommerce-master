from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Feedback
from .forms import FeedbackForm


def feedback_list(request):
    """Display approved feedbacks and feedback form."""
    # Get all approved feedbacks, ordered by rating (highest first) then by date
    feedbacks = Feedback.objects.filter(is_approved=True).order_by('-rating', '-created_at')
    
    # Add sample feedbacks if no feedbacks exist
    sample_feedbacks = []
    if feedbacks.count() == 0:
        sample_feedbacks = [
            {
                'name': 'Rajesh Kumar',
                'email': 'rajesh@email.com',
                'comment': 'Absolutely loved the portrait! The artist captured my personality perfectly. The attention to detail is remarkable. Highly recommend their work!',
                'rating': 5,
                'created_at': '2025-12-20'
            },
            {
                'name': 'Priya Sharma',
                'email': 'priya@email.com',
                'comment': 'Beautiful custom artwork! The artist was very professional and delivered on time. I\'m very satisfied with the result.',
                'rating': 5,
                'created_at': '2025-12-18'
            },
            {
                'name': 'Amit Patel',
                'email': 'amit@email.com',
                'comment': 'Great commission service. The artist understood my vision and created exactly what I wanted. Will definitely commission again!',
                'rating': 5,
                'created_at': '2025-12-15'
            },
            {
                'name': 'Sneha Desai',
                'email': 'sneha@email.com',
                'comment': 'Amazing artwork! The colors and composition are perfect. The artist was responsive and accommodating to all my requests.',
                'rating': 5,
                'created_at': '2025-12-12'
            },
            {
                'name': 'Vikram Singh',
                'email': 'vikram@email.com',
                'comment': 'Top-notch quality! The custom mural art is stunning. It has transformed my living room completely. Exceptional work!',
                'rating': 5,
                'created_at': '2025-12-10'
            }
        ]
        feedbacks = sample_feedbacks
    
    form = None
    user_feedbacks = None
    if request.user.is_authenticated:
        # Get user's own feedbacks (approved and pending)
        user_feedbacks = request.user.feedbacks.all().order_by('-created_at')
        
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.user = request.user
                feedback.save()
                messages.success(request, '✓ Thank you! Your feedback has been submitted and will be reviewed by our team.')
                return redirect('feedback:feedback_list')
        else:
            # Pre-fill name and email for logged-in users
            form = FeedbackForm(initial={
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email
            })
    
    # Calculate total and average based on whether using samples or real feedbacks
    if sample_feedbacks:
        total_count = len(sample_feedbacks)
        avg_rating_val = round(sum([f['rating'] for f in sample_feedbacks]) / len(sample_feedbacks), 1)
    else:
        real_feedbacks = Feedback.objects.filter(is_approved=True)
        total_count = real_feedbacks.count()
        avg_rating_val = calculate_avg_rating(real_feedbacks) if real_feedbacks.count() > 0 else 0
    
    context = {
        'feedbacks': feedbacks if feedbacks else [],
        'user_feedbacks': user_feedbacks,
        'form': form,
        'total_feedbacks': total_count,
        'avg_rating': avg_rating_val,
        'has_real_feedbacks': not sample_feedbacks
    }
    return render(request, 'feedback.html', context)


@login_required(login_url='login')
def delete_feedback(request, feedback_id):
    """Delete feedback - only user can delete their own feedback."""
    feedback = get_object_or_404(Feedback, id=feedback_id)
    
    # Check if the user owns this feedback
    if feedback.user != request.user:
        messages.error(request, '❌ You can only delete your own feedback.')
        return redirect('feedback:feedback_list')
    
    # Delete the feedback
    feedback.delete()
    messages.success(request, '✓ Your feedback has been deleted successfully.')
    return redirect('feedback:feedback_list')


def calculate_avg_rating(feedbacks):
    """Calculate average rating from feedbacks."""
    if not feedbacks.exists():
        return 0
    total = sum([f.rating for f in feedbacks])
    return round(total / feedbacks.count(), 1)
