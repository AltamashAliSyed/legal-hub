from django.urls import path
from .views import home,Fundamental,Civil,Environmental,Economic,human,Legal,political,Directive,autocomplete_fundamental_rights,autocomplete_civil_rights,autocompleteDirective,autocompleteEconomic,autocompletehuman,autocompletelegal,autocompleteenvironmental,autocompletepolitical,searchresults,examplecivil,examplefundamental,environmentalexample,economicexample,humanexample,legalexample,politialexample,directiveexample,create_lawyer_profile,profilesuccess,approve_lawyer,unapproved_lawyer,lawyer_list,CriminalLawexample,autocompleteCriminalLaw,criminallaw,personallaw,peersonallawawexample,personallaw,autocompletepersonallaw,union_territory_list,autocomplete_union_territory,union_territory_detail,helpline_numbers,legal_news
urlpatterns= [ 
    path('',home,name="home"),
    path("FundamentalRights/",Fundamental,name='FundamentalRights'),
    path('autocomplete/fundamental-rights/',autocomplete_fundamental_rights, name="autocomplete_fundamental_rights"),
    path('examplefundamental/<int:right_id>/',examplefundamental,name='examplefundamental'),

    path("civilrights/",Civil,name="CivilRights"),
    path('autocomplete_civil_rights',autocomplete_civil_rights,name="autocomplete_civil_rights"),
    path('examplecivil/<int:right_id>/',examplecivil,name='examplecivil'),
    

    path("EnvironmentalRights/",Environmental,name="EnvironmentalRights"),
    path('autocompleteenvironmental',autocompleteenvironmental,name="autocompleteenvironmental"),
    path('exampleenvironmental/<int:right_id>/',environmentalexample,name='exampleenvironmental'),

    path("EconomicRights/",Economic,name="EconomicRights"),
    path("autocompleteEconomic",autocompleteEconomic,name="autocompleteEconomic"),
    path('Economicexample/<int:right_id>/',economicexample,name='economicexample'),

    path("humanRights/",human,name="humanRights"),
    path("autocompletehuman",autocompletehuman,name="autocompletehuman"),
    path('humanexample/<int:right_id>/',humanexample,name='humanexample'),

    path("LegalRights/",Legal,name="LegalRights"),
    path("autocompletelegal",autocompletelegal,name="autocompletelegal"),
    path('legalexample/<int:right_id>/',legalexample,name='legalexample'),

    path("TheUnionandItsTerritory/", union_territory_list, name="TheUnionandItsTerritory"),  
    path("autocompleteTheUnionandItsTerritory/", autocomplete_union_territory, name="autocompleteTheUnionandItsTerritory"),  
    path("TheUnionandItsTerritoryexample/<int:right_id>/", union_territory_detail, name="TheUnionandItsTerritoryexample"),  



    path("politicalRights/",political,name="politicalRights"),
    path("autocompletepolitical",autocompletepolitical,name="autocompletepolitical"),
    path('politicalexample/<int:right_id>/',politialexample,name='politicalexample'),

    path("Directive/",Directive,name='DirectivePrincipleofOurStatePolicy'),
    path("autocompleteDirective",autocompleteDirective,name="autocompleteDirective"),
    path('directiveexample/<int:right_id>/',directiveexample,name='directiveexample'),

    path("criminallaw/",criminallaw,name='criminallaw'),
    path("autocompletecriminallaw",autocompleteCriminalLaw,name="autocompletecriminallaw"),
    path('criminallawexample/<int:right_id>/',CriminalLawexample,name='Criminalexample'),

    path("personallaw/",personallaw,name='personallaw'),
    path("autocompletepersonallaw",autocompletepersonallaw,name="autocompletepersonallaw"),
    path('personallawexample/<int:right_id>/',peersonallawawexample,name='personalexample'),

    path('searhresults/',searchresults,name='searchresults'),
    path('create_lawyer/',create_lawyer_profile,name='create_lawyer'),
    path('profile_success/',profilesuccess,name='profilesuccess'),
    path('approve_lawyer/<int:id>/',approve_lawyer,name='approve_lawyer'),
    path('helplines/', helpline_numbers, name='helpline_numbers'),
    
    path('lawyer_list',lawyer_list,name='lawyer_list'),
    path('news/', legal_news, name='legal_news'),
                                                                                                                                        
    #path('signup/', signup_view, name='signup'),
    #path('login/', login_view, name='login'),
    #path('logout/', logout_view, name='logout'),

    # AJAX Comment & Reply
    #path('add-comment/', add_comment_ajax, name='add_comment_ajax'),
    #path('add-reply/', reply_ajax, name='reply_ajax'), 

   
    
]
