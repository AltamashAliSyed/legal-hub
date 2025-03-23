from django.shortcuts import render, redirect , get_object_or_404
from .models import FundamentalRights,CivilRights,EnvironmentalRights,EconomicRights,humanRights,LegalRights,politicalRights,DirectivePrincipleofOurStatePolicy , Lawyer,PersonalLaw,CriminalLaw,UnionTerritory
from django.http import JsonResponse,HttpResponse
from django.db.models import Q 
from .forms import LawyerForm 
from .models import Lawyer


# Create your views here.

def home(request):
    
    query = request.GET.get('q')
    if query:
        return redirect('searchresults', q=query)
    return render(request, 'home.html')


def searchresults(request):
    query = request.GET.get('q')

     # Initialize empty queryset for each model
    fundamental_right = FundamentalRights.objects.none()
    civil_right = CivilRights.objects.none()
    environmental_right = EnvironmentalRights.objects.none()
    economic_right = EconomicRights.objects.none()
    human_right = humanRights.objects.none()
    legal_right = LegalRights.objects.none()
    political_right = politicalRights.objects.none()
    directive = DirectivePrincipleofOurStatePolicy.objects.none()
    Criminallaw = CriminalLaw.objects.none()
    personallaw = PersonalLaw.objects.none()
    

    if query:
        # Search across all models using the query
        fundamental_right = FundamentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query) 
        )
        civil_right = CivilRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        environmental_right = EnvironmentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        economic_right = EconomicRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        human_right = humanRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        legal_right = LegalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        political_right = politicalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        directive = DirectivePrincipleofOurStatePolicy.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query) 
        )
        Criminallaw= CriminalLaw.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        personallaw = PersonalLaw.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )

    # Combine all results into context
    context = {
        'fundamental_right': fundamental_right,
        'civil_right': civil_right,
        'environmental_right': environmental_right,
        'economic_right': economic_right,
        'human_right': human_right,
        'legal_right': legal_right,
        'political_right': political_right,
        'directive': directive,
        'Criminallaw':Criminallaw,
        'personallaw':personallaw,
        'query': query,
        
    }
    
    return render(request, 'searchresults.html', context)

    
def Fundamental(request):
    query = request.GET.get('q')
    if query:
        fundamental_right = FundamentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        
    else:
        fundamental_right = FundamentalRights.objects.all()
    
    return render(request,'FundamentalRights.html',{'fundamental_right': fundamental_right})

def autocomplete_fundamental_rights(request):
    query = request.GET.get('q')
    if query:
        fundamental_right = FundamentalRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        rights = FundamentalRights.objects.all().values('name')
    return JsonResponse(list(rights), safe=False)

def examplefundamental(request, right_id):
    example = FundamentalRights.objects.filter(id=right_id)
    return render(request,'fundamentalexample.html', {'example',example})
 


def Civil(request):
    query = request.GET.get('q')
    if query:
        Civil_right = CivilRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        Civil_right = CivilRights.objects.all()

    return render(request,'CivilRights.html',{'Civil_right':Civil_right})


def autocomplete_civil_rights(request):
    query = request.GET.get('q')
    if query:
        Civil_right = CivilRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        Civil_right = CivilRights.objects.all().values('name')
    return JsonResponse(list(Civil_right), safe=False)

def examplecivil(request, right_id):
    example = CivilRights.objects.filter(id=right_id)
    return render(request,'Civilexample.html',{'example':example})







def Environmental(request):
    query = request.GET.get('q')
    if query:
        environmental_right = EnvironmentalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        environmental_right = EnvironmentalRights.objects.all()
    return render(request,'EnvironmentalRights.html',{'environmental_right':environmental_right})

def autocompleteenvironmental(request):
    query = request.GET.get('q')
    if query:
        environmental_right = EnvironmentalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        environmental_right = EnvironmentalRights.objects.all().values('name')
    return JsonResponse(list(environmental_right), safe=False)

def environmentalexample(request, right_id):
    example = EnvironmentalRights.objects.filter(id=right_id)
    return render(request, 'Environmentalexample.html', {'example':example})






def Economic(request):
    query = request.GET.get('q')
    if query:
        Economic_right = EconomicRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)    
        )
    else:
        Economic_right = EconomicRights.objects.all()
    return render(request,"Economicrights.html",{'Economic_right':Economic_right})

def autocompleteEconomic(request):
    query = request.GET.get('q')
    if query:
        Economic_right = EconomicRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)    
        )
    else:
        Economic_right = EconomicRights.objects.all().values('name')
    return JsonResponse(list(Economic_right), safe=False)


def economicexample(request, right_id):
    example = EconomicRights.objects.filter(id=right_id)
    return render(request,'Economicexample.html',{'example':example})





def human(request):
    query = request.GET.get('q')
    if query:
        human_right = humanRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        human_right = humanRights.objects.all()
        
    return render(request,"humanrights.html",{'human_right':human_right})

def autocompletehuman(request):
    query = request.GET.get('q')
    if query:
        human_right = humanRights.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        human_right = humanRights.objects.all().values('name')
    JsonResponse(list(human_right), safe=False)

def humanexample(request, right_id):
    example = humanRights.objects.filter(id=right_id)
    return render(request,'humanexample.html',{'example':example})



def Legal(request):
    query = request.GET.get('q')
    if query:
         legal_right = LegalRights.objects.filter(
             Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
         legal_right = LegalRights.objects.all()
    
    return render(request,"legalrights.html",{'legal_right':legal_right})

def autocompletelegal(request):
    query = request.GET.get('q')
    if query:
         legal_right = LegalRights.objects.filter(
             Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
         legal_right = LegalRights.objects.all().values('name')
    JsonResponse(list(legal_right), safe=False)

def legalexample(request, right_id):
    example = LegalRights.objects.filter(id=right_id)
    return render(request,'legalexample.html',{'example':example})




    


def political(request):
    query = request.GET.get('q')
    if query:
        political_right = politicalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        political_right = politicalRights.objects.all()
        
    return render(request,"politicalRights.html",{'political_right':political_right})

def autocompletepolitical(request):
    query = request.GET.get('q')
    if query:
        political_right = politicalRights.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        political_right = politicalRights.objects.all().values('name')
        
    JsonResponse(list(political_right), safe=False)

def politialexample(request, right_id):
    example = politicalRights.objects.filter(id=right_id)
    return render(request,'politicalexample.html',{'example':example})



from .models import UnionTerritory 
def union_territory_list(request):  
    query = request.GET.get('q')  
    if query:  
        territories = UnionTerritory.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )  
    else:  
        territories = UnionTerritory.objects.all()  

    return render(request, "TheUnionanditsTerritory.html", {'territories': territories})  

def autocomplete_union_territory(request):  
    query = request.GET.get('q')  
    if query:  
        territories = UnionTerritory.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        ).values('title') 
    else:  
        territories = UnionTerritory.objects.all().values('name')  

    return JsonResponse(list(territories), safe=False)  

def union_territory_detail(request, right_id):  
    example = get_object_or_404(UnionTerritory, id=right_id)  
    return render(request, 'TheUnionandItsTerritory.html', {'example': example})  






def Directive(request):
    query = request.GET.get('q')
    if query:
        Directive = DirectivePrincipleofOurStatePolicy.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        Directive = DirectivePrincipleofOurStatePolicy.objects.all()

    return render(request,"Directiveprinciple.html",{'Directive':Directive})

def autocompleteDirective(request):
    query = request.GET.get('q')
    if query:
        Directive = DirectivePrincipleofOurStatePolicy.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        Directive = DirectivePrincipleofOurStatePolicy.objects.all().values('name')
    return JsonResponse(list(Directive), safe=False)


def directiveexample(request, right_id):
    example = DirectivePrincipleofOurStatePolicy.objects.filter(id=right_id)
    return render(request,'Directiveexample.html',{'example':example})





def criminallaw(request):
    query = request.GET.get('q')
    if query:
        Criminallaw= CriminalLaw.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        Criminallaw = CriminalLaw.objects.all()

    return render(request,"CriminalLaw.html",{'CriminalLaw':Criminallaw})

def autocompleteCriminalLaw(request):
    query = request.GET.get('q')
    if query:
        Criminallaw = CriminalLaw.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        Criminallaw = CriminalLaw.objects.all().values('name')
    return JsonResponse(list(Criminallaw), safe=False)


def CriminalLawexample(request, right_id):
    example = CriminalLaw.objects.filter(id=right_id)
    return render(request,'CriminalLawexample.html',{'example':example})


def personallaw(request):
    query = request.GET.get('q')
    if query:
        personallaw = PersonalLaw.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
    else:
        personallaw = PersonalLaw.objects.all()

    return render(request,"PersonalLaw.html",{'personallaw':personallaw})

def autocompletepersonallaw(request):
    query = request.GET.get('q')
    if query:
        personallaw = PersonalLaw.objects.filter(
            Q(Title__iconatins=query) | Q(Description__icontains=query)
        )
    else:
        personallaw = PersonalLaw.objects.all().values('name')
    return JsonResponse(list(personallaw), safe=False)


def peersonallawawexample(request, right_id):
    example = PersonalLaw.objects.filter(id=right_id)
    return render(request,'personallawexample.html',{'example':example})








from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
def create_lawyer_profile(request):
    if request.method == "POST":
        form = LawyerForm(request.POST, request.FILES)
        if form.is_valid():
            lawyer = form.save(commit = False)
            lawyer.is_approved = False
            lawyer.save()
            messages.success(request,'Your profile has been approved ')
            return redirect('profilesuccess')
        
    else:
        form = LawyerForm()
    return render(request, 'create_lawyer.html', {'form': form})

def profilesuccess(request):
    return render(request,'profilesuccess.html')



from django.conf import settings
@staff_member_required

def approve_lawyer(request, lawyer_id):
    lawyer = get_object_or_404(Lawyer, id=lawyer_id)
    if request.method == 'POST':
        lawyer.is_approved = True
        lawyer.save()

        messages.success(request,f'Lawyer {lawyer.name} has been approved')
        return redirect('lawyer_list')

        

    return render(request, 'approve_lawyer.html', {'lawyer': lawyer})


@staff_member_required
def unapproved_lawyer(request):
    unapproved = Lawyer.objects.filter(is_approved = False)
    return render(request , 'unapproved_lawyer.html',{'unapproved':unapproved})


def lawyer_list(request):
    query_name = request.GET.get('name', '')
    query_specialization = request.GET.get('specialization', '')
    query_location = request.GET.get('location', '')

    lawyers = Lawyer.objects.filter(is_approved=True)

    if query_name:
        lawyers = lawyers.filter(name__icontains=query_name)

    if query_specialization:
        lawyers = lawyers.filter(specialization__icontains=query_specialization)

    if query_location:
        lawyers = lawyers.filter(location__icontains=query_location)

    return render(request, 'lawyer_list.html', {
        'approved_lawyers': lawyers,
        'query_name': query_name,
        'query_specialization': query_specialization,
        'query_location':query_location
    })


def helpline_numbers(request):
    helplines = {
        "Police Helpline": "100",
        "Women’s Helpline": "1091",
        "Cybercrime Helpline": "1930",
        "Child Helpline": "1098",
        "Senior Citizens Helpline": "14567",
        "Consumer Helpline": "1800-11-4000",
        "Legal Aid (NALSA)": "15100",
    }
    return render(request, 'helplines_numbers.html', {"helplines": helplines})

import feedparser
import requests
def fetch_feed_with_headers(feed_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(feed_url, headers=headers)
    if response.status_code == 200:
        return feedparser.parse(response.content)
    return None  # If the request fails

def legal_news(request):
    rss_feeds = [
        "https://www.scobserver.in/feed/",  
    "https://www.livelaw.in/top-stories/feed",
    "https://www.barandbench.com/rss/news",
    "https://www.legallyindia.com/?format=feed&type=rss",
    "https://theleaflet.in/feed/"
    ]

    articles = []
    for feed_url in rss_feeds:
        feed = fetch_feed_with_headers(feed_url)
        if feed and hasattr(feed, "entries"):
            print(f"Fetched {len(feed.entries)} articles from {feed_url}")
            for entry in feed.entries:
                articles.append({
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.published if hasattr(entry, 'published') else "Unknown Date",
                })
        else:
            print(f"Failed to fetch news from {feed_url}")

    return render(request, "legal_news.html", {"articles": articles})
""""
#authentication

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .decorators import custom_login

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        if not username or not password or not confirm_password:
            messages.error(request, "All fields are required")
            return render(request, 'signup.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registered successfully!")
            return redirect('login')
    
    return render(request,'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('login')



@custom_login
def add_comment_ajax(request):
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        post_id = request.POST.get("post_id")

        if comment_text and post_id:
            comment = Comment.objects.create(user=request.user, post_id=post_id, text=comment_text)
            return JsonResponse({"success": True, "comment": comment.text, "username": request.user.username})

    return JsonResponse({"success": False, "error": "Invalid data"})


@custom_login
def reply_ajax(request):
    if request.method == "POST":
        comment_id = request.POST.get("comment_id")
        message = request.POST.get("message")

        print(f"Received comment_id: {comment_id}")
        print(f"Received message: {message}")
        print(f"User: {request.user}, ID: {request.user.id}")

        comment = get_object_or_404(Comment, id=comment_id)

        lawyer = Lawyer.objects.filter(user=request.user).first()
        if not lawyer:
            print("❌ Lawyer does not exist!")
            return JsonResponse({"success": False, "error": "Only lawyers can reply."})

        print(f"Lawyer found: {lawyer.name}, Approved: {lawyer.is_approved}")

        if not lawyer.is_approved:
            print("❌ Lawyer is NOT approved!")
            return JsonResponse({"success": False, "error": "Only approved lawyers can reply."})

        reply = Reply.objects.create(comment=comment, lawyer=lawyer, message=message)
        print(f"✅ Reply saved: {reply.lawyer.name}: {reply.message}")

        return JsonResponse({"success": True, "lawyer_name": lawyer.name, "message": message})

    print("❌ Invalid request method")
    return JsonResponse({"success": False})"
"""