from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        # 1. Capture Data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', 'N/A')
        service = request.POST.get('service')
        message = request.POST.get('message')

        if name and email and service and message:
            # 2. Prepare Admin Email
            admin_subject = f"New Inquiry: {service} from {name}"
            admin_body = f"""
New Inquiry Received:

Name: {name}
Email: {email}
Phone: {phone}
Service Requested: {service}

Project Details:
{message}
"""

            # 3. Prepare Customer Auto-responder
            customer_subject = "We've received your request - Real Life Experience LLC"
            customer_body = f"""
Hi {name},

Thank you for reaching out to Real Life Experience LLC! 

We have received your request for "{service}" and our team will review the details of your project shortly.

Best regards,
The RLECD Team
"""

            try:
                # Send to Admins
                send_mail(
                    subject=admin_subject,
                    message=admin_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=settings.ADMIN_EMAIL,
                    fail_silently=False,
                )

                # Send to Customer
                send_mail(
                    subject=customer_subject,
                    message=customer_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent successfully!")
                return redirect('/#contact')

            except Exception as e:
                # Log the error for your own debugging
                print(f"Email failed: {e}")
                messages.error(request, "There was an error sending your message. Please try again later.")
                return redirect('/#contact')
        else:
            messages.error(request, "Please fill out all required fields.")
            return redirect('/#contact')

    return render(request, "main/index.html")
    
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        # Grab data from the input name="" attributes in your HTML
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', 'Not provided')
        service_raw = request.POST.get('service')
        message = request.POST.get('message')

        # Clean up dropdown values for readable email display
        service_mapping = {
            'kitchen': 'Kitchen Remodel',
            'bath': 'Bathroom Remodel',
            'basement': 'Basement Finishing',
            'other': 'General Inquiry'
        }
        service_clean = service_mapping.get(service_raw, 'General Inquiry')

        # Ensure all required fields are present
        if name and email and service_clean and message:
            
            # Formatted email sent to the Admin team
            admin_body = f"""
New Inquiry Received:

Name: {name}
Email: {email}
Phone: {phone}
Service: {service_clean}

Project Details:
{message}
"""

            # Auto-responder email sent to the potential client
            customer_body = f"""
Hi {name},

Thank you for reaching out to Real Life Experience LLC! 

We have received your request for "{service_clean}". Our team will review your project details and get back to you shortly.

Best regards,
The RLECD Team
"""

            try:
                # 1. Send notice alert email to the admin addresses
                send_mail(
                    subject=f"New Web Inquiry – {service_clean}",
                    message=admin_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=settings.ADMIN_EMAIL, # Ensure this is a list in settings.py
                    fail_silently=False,
                )

                # 2. Send confirmation auto-responder to the customer
                send_mail(
                    subject="We've received your inquiry - Real Life Experience LLC",
                    message=customer_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent successfully!")
                return redirect('/contact/') 

            except Exception as e:
                print("SMTP Error:", e) # Check your terminal/logs for this
                messages.error(request, "There was an error sending your message. Please try again.")
                return redirect('/contact/')
        else:
            messages.error(request, "Please fill out all required fields.")
            return redirect('/contact/') 

    return render(request, 'main/contact.html')

def areas_we_serve(request):
    return render(request, 'main/areas_we_serve.html')

def bathroom_remodeling(request):
    return render(request, 'main/bathroom.html')

def kitchen_remodeling(request):
    return render(request, 'main/kitchen.html')

def basement_finishing(request):
    return render(request, 'main/basement.html')

def home_additions(request):
    return render(request, 'main/additions.html')
    
def painting(request):
    return render(request, 'main/painting.html')

def home_improvement(request):
    return render(request, 'main/home_improvement.html')

def patios_decks(request):
    return render(request, 'main/patios_decks.html')

def cabinets(request):
    return render(request, 'main/cabinets.html')

def woodworking(request):
    return render(request, 'main/woodworking.html')

def hardscaping(request):
    return render(request, 'main/hardscaping.html')

def walkway_designs(request):
    return render(request, 'main/walkways.html')

def pergolas(request):
    return render(request, 'main/pergolas.html')

def lead_removal(request):
    return render(request, 'main/lead_removal.html')

def shed_builder(request):
    return render(request, 'main/sheds.html')

def lead_renovator(request):
    return render(request, 'main/lead_renovator.html')