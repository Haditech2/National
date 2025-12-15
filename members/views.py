from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .models import Member
from .forms import UserRegistrationForm, MemberProfileForm
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os
from django.conf import settings
import requests

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('members:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        Member.objects.create(user=self.object)
        login(self.request, self.object)
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'members/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member, created = Member.objects.get_or_create(user=self.request.user)
        context['member'] = member
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberProfileForm
    template_name = 'members/profile_edit.html'
    success_url = reverse_lazy('members:profile')

    def get_object(self, queryset=None):
        member, created = Member.objects.get_or_create(user=self.request.user)
        return member


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'members/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member, created = Member.objects.get_or_create(user=self.request.user)
        context['member'] = member
        return context


class IDCardPreviewView(LoginRequiredMixin, TemplateView):
    template_name = 'members/id_card_preview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member, created = Member.objects.get_or_create(user=self.request.user)
        context['member'] = member
        return context


class VerifyMemberView(TemplateView):
    template_name = 'members/verify_member.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        membership_id = self.kwargs.get('membership_id')
        try:
            member = Member.objects.get(membership_id=membership_id)
            context['member'] = member
            context['verified'] = True
        except Member.DoesNotExist:
            context['verified'] = False
        return context


@login_required
def generate_id_card(request):
    member = get_object_or_404(Member, user=request.user)
    
    # Generate QR code
    verification_url = request.build_absolute_uri(
        reverse('members:verify_member', args=[member.membership_id])
    )
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(verification_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Create ID Card image (PNG)
    card_width = 638
    card_height = 1012
    
    # Create card background
    card = Image.new('RGB', (card_width, card_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(card)
    
    # Colors
    dark_green = (0, 100, 0)
    gold = (218, 165, 32)
    white = (255, 255, 255)
    
    # Header background
    draw.rectangle([(0, 0), (card_width, 200)], fill=dark_green)
    
    # Try to load fonts, fall back to default if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 28)
        name_font = ImageFont.truetype("arial.ttf", 26)
        detail_font = ImageFont.truetype("arial.ttf", 18)
    except:
        title_font = ImageFont.load_default()
        name_font = ImageFont.load_default()
        detail_font = ImageFont.load_default()
    
    # Add logo to header
    logo_path = os.path.join(settings.STATIC_ROOT or os.path.join(settings.BASE_DIR, 'static'), 'images', 'logo.png')
    logo_size = 80
    logo_x = 30
    logo_y = 20
    
    try:
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((logo_size, logo_size))
            # Handle transparency if PNG
            if logo_img.mode == 'RGBA':
                card.paste(logo_img, (logo_x, logo_y), logo_img)
            else:
                card.paste(logo_img, (logo_x, logo_y))
    except Exception as e:
        pass  # Logo not found, continue without it
    
    # Title (adjusted for logo)
    text_x = card_width//2 + 30
    draw.text((text_x, 35), "NATIONAL ASSOCIATION", fill=gold, font=title_font, anchor="mm")
    draw.text((text_x, 70), "OF ANKPA STUDENTS", fill=gold, font=title_font, anchor="mm")
    draw.text((text_x, 105), "(NATIONAL BODY)", fill=white, font=detail_font, anchor="mm")
    draw.text((card_width//2, 170), "MEMBER ID CARD", fill=gold, font=title_font, anchor="mm")
    
    # Passport photo placeholder
    passport_y = 240
    passport_size = 200
    draw.rectangle(
        [(card_width//2 - passport_size//2, passport_y), 
         (card_width//2 + passport_size//2, passport_y + passport_size)],
        outline=dark_green, width=3
    )
    
    # If member has passport photo, paste it
    if member.passport_photo:
        try:
            # Try to get the image - works with both local files and Cloudinary URLs
            try:
                # First try local file path
                passport_img = Image.open(member.passport_photo.path)
            except (ValueError, AttributeError, FileNotFoundError):
                # If that fails, try to fetch from URL (Cloudinary)
                photo_url = member.passport_photo.url
                response = requests.get(photo_url, timeout=10)
                response.raise_for_status()
                passport_img = Image.open(BytesIO(response.content))
            
            # Convert to RGB if necessary (handles RGBA and other modes)
            if passport_img.mode in ('RGBA', 'P'):
                passport_img = passport_img.convert('RGB')
            
            passport_img = passport_img.resize((passport_size - 6, passport_size - 6))
            card.paste(passport_img, (card_width//2 - passport_size//2 + 3, passport_y + 3))
        except Exception as e:
            draw.text((card_width//2, passport_y + passport_size//2), "Photo", fill=dark_green, font=detail_font, anchor="mm")
    else:
        draw.text((card_width//2, passport_y + passport_size//2), "Photo", fill=dark_green, font=detail_font, anchor="mm")
    
    # Member details
    details_y = 470
    line_height = 42
    
    full_name = member.user.get_full_name() or member.user.username
    draw.text((card_width//2, details_y), full_name.upper(), fill=dark_green, font=name_font, anchor="mm")
    
    draw.text((card_width//2, details_y + line_height), f"ID: {member.membership_id}", fill=dark_green, font=detail_font, anchor="mm")
    draw.text((card_width//2, details_y + line_height*2), f"School: {member.school or 'N/A'}", fill=dark_green, font=detail_font, anchor="mm")
    draw.text((card_width//2, details_y + line_height*3), f"Level: {member.level or 'N/A'}", fill=dark_green, font=detail_font, anchor="mm")
    draw.text((card_width//2, details_y + line_height*4), f"Department: {member.department or 'N/A'}", fill=dark_green, font=detail_font, anchor="mm")
    draw.text((card_width//2, details_y + line_height*5), f"Chapter: {member.chapter or 'N/A'}", fill=dark_green, font=detail_font, anchor="mm")
    
    # QR Code
    qr_size = 150
    qr_img = qr_img.resize((qr_size, qr_size))
    qr_y = details_y + line_height*6 + 20
    card.paste(qr_img, (card_width//2 - qr_size//2, qr_y))
    
    # Footer
    footer_y = card_height - 60
    draw.rectangle([(0, footer_y - 20), (card_width, card_height)], fill=dark_green)
    draw.text((card_width//2, footer_y + 10), "Scan QR Code to Verify", fill=white, font=detail_font, anchor="mm")
    
    # Update member record
    member.id_card_generated_at = timezone.now()
    member.save()
    
    # Create response
    buffer = BytesIO()
    card.save(buffer, format='PNG')
    buffer.seek(0)
    
    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="NAAS_ID_Card_{member.membership_id}.png"'
    
    return response
